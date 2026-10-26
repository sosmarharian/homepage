/* Custom round "cookie settings" badge — replaces CCM19's default square
   icon site-wide. Clicking it opens the same CCM19 widget as the existing
   footer "Cookie-Einstellungen" link (CCM.openWidget()); hiding CCM19's own
   badge via CSS doesn't affect that function or GDPR consent-withdrawal.

   Position: sits bottom-right. If the page has a bottom-anchored fixed
   element (the sticky "Preis anfragen" CTA bar, or — on thanks/danke/
   preisanfrage pages only — the round bottom WhatsApp FAB; on main pages
   .wa-fab is a top-right pill and is ignored), the badge is pinned a fixed
   gap above it, measured live so it tracks correctly even as iOS Safari's
   toolbar collapses/expands during scroll. Otherwise it uses a static
   bottom-right spot.

   Include on every page that loads CCM19:
   <script src="/ccm-badge.js" defer></script>
*/
(function () {
  var SIZE = 48;
  var GAP = 14;
  var BASE_BOTTOM = 24;
  var RIGHT_DESKTOP = 40;
  var RIGHT_MOBILE = 16;

  var style = document.createElement('style');
  style.textContent =
    '.ccm-settings-summoner{display:none!important;}' +
    '.ccm-custom-badge{position:fixed;z-index:99999998;width:' + SIZE + 'px;height:' + SIZE + 'px;' +
      'right:' + RIGHT_DESKTOP + 'px;bottom:' + BASE_BOTTOM + 'px;' +
      'border-radius:50%;background:#1a1a1a;border:none;padding:0;cursor:pointer;' +
      'display:flex;align-items:center;justify-content:center;' +
      'box-shadow:0 2px 10px rgba(0,0,0,.35);transition:transform .2s ease;}' +
    '.ccm-custom-badge:hover{transform:scale(1.06);}' +
    '.ccm-custom-badge svg{width:24px;height:24px;display:block;}' +
    '@media (max-width:768px){.ccm-custom-badge{right:' + RIGHT_MOBILE + 'px;}}';
  document.head.appendChild(style);

  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'ccm-custom-badge';
  btn.setAttribute('aria-label', 'Cookie-Einstellungen');
  btn.innerHTML =
    '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">' +
    '<path fill="#fff" d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58a.49.49 0 0 0 .12-.61l-1.92-3.32a.488.488 0 0 0-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94L14.4 2.81a.484.484 0 0 0-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96a.488.488 0 0 0-.59.22L2.74 8.86a.49.49 0 0 0 .12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58a.49.49 0 0 0-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/>' +
    '</svg>';
  btn.addEventListener('click', function () {
    if (window.CCM) { CCM.openWidget(); }
  });
  document.body.appendChild(btn);

  var candidates = Array.prototype.slice.call(document.querySelectorAll('[data-sticky-cta], .wa-fab'));

  function isBottomAnchored(el) {
    var r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0 && r.bottom >= window.innerHeight - 40 && r.bottom <= window.innerHeight + 40;
  }
  function findAvoid() {
    for (var i = 0; i < candidates.length; i++) {
      if (isBottomAnchored(candidates[i])) return candidates[i];
    }
    return null;
  }
  function reposition() {
    var avoid = findAvoid();
    if (!avoid) { btn.style.removeProperty('bottom'); return; }
    var rect = avoid.getBoundingClientRect();
    var visible = rect.top < window.innerHeight && rect.bottom > 0 && !avoid.classList.contains('is-hidden');
    if (!visible) { btn.style.removeProperty('bottom'); return; }
    btn.style.setProperty('bottom', (window.innerHeight - rect.top + GAP) + 'px', 'important');
  }
  window.addEventListener('scroll', reposition, { passive: true });
  window.addEventListener('resize', reposition);
  window.addEventListener('load', reposition);
  reposition();
})();
