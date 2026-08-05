// Meta Conversions API — серверная отправка событий.
//
// Зачем: события из браузера теряются на iPhone (ITP от Apple, отказ от
// отслеживания, блокировщики). Эта функция шлёт то же событие с сервера
// напрямую в Meta, поэтому оно доходит.
//
// Дубли не возникают: браузерное и серверное событие имеют одинаковый
// event_id, и Meta их склеивает (дедупликация).
//
// Токен берётся из переменной окружения FB_CAPI_TOKEN (настраивается
// в Vercel → Settings → Environment Variables). В репозитории его нет.

const crypto = require('crypto');

const PIXEL_ID = '973100958791977';
const API_VERSION = 'v21.0';

// Meta требует SHA-256 от нормализованного значения
function hash(value) {
  if (!value) return undefined;
  return crypto.createHash('sha256').update(String(value)).digest('hex');
}

function normalizeEmail(email) {
  if (!email) return undefined;
  return String(email).trim().toLowerCase();
}

// Телефон: только цифры, с кодом страны. Немецкие номера без кода
// приводим к формату 49XXXXXXXXX.
function normalizePhone(phone) {
  if (!phone) return undefined;
  let digits = String(phone).replace(/\D/g, '');
  if (!digits) return undefined;
  if (digits.startsWith('00')) digits = digits.slice(2);
  else if (digits.startsWith('0')) digits = '49' + digits.slice(1);
  return digits;
}

function firstIp(req) {
  const forwarded = req.headers['x-forwarded-for'];
  if (!forwarded) return undefined;
  return String(forwarded).split(',')[0].trim();
}

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }

  const token = process.env.FB_CAPI_TOKEN;
  if (!token) {
    // Не роняем форму из-за проблем с аналитикой
    console.error('FB_CAPI_TOKEN не задан');
    res.status(200).json({ ok: false, reason: 'token_missing' });
    return;
  }

  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch (e) { body = {}; }
  }
  body = body || {};

  const eventName = body.event_name || 'Lead';
  const eventId = body.event_id;
  if (!eventId) {
    res.status(400).json({ error: 'event_id обязателен для дедупликации' });
    return;
  }

  const userData = {
    client_ip_address: firstIp(req),
    client_user_agent: req.headers['user-agent'],
  };

  const em = hash(normalizeEmail(body.email));
  if (em) userData.em = [em];

  const ph = hash(normalizePhone(body.phone));
  if (ph) userData.ph = [ph];

  // Куки пикселя — сильнее всего повышают качество сопоставления
  if (body.fbp) userData.fbp = body.fbp;
  if (body.fbc) userData.fbc = body.fbc;

  const payload = {
    data: [
      {
        event_name: eventName,
        event_time: Math.floor(Date.now() / 1000),
        event_id: eventId,
        event_source_url: body.event_source_url,
        action_source: 'website',
        user_data: userData,
        custom_data: body.custom_data || {},
      },
    ],
  };

  if (body.test_event_code) payload.test_event_code = body.test_event_code;

  try {
    const response = await fetch(
      `https://graph.facebook.com/${API_VERSION}/${PIXEL_ID}/events?access_token=${encodeURIComponent(token)}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      }
    );

    const result = await response.json();

    if (!response.ok) {
      console.error('Meta CAPI ошибка:', JSON.stringify(result));
      res.status(200).json({ ok: false, meta: result });
      return;
    }

    res.status(200).json({ ok: true, meta: result });
  } catch (err) {
    console.error('Meta CAPI исключение:', err && err.message);
    res.status(200).json({ ok: false, reason: 'exception' });
  }
};
