// SPDX-License-Identifier: MIT
// The upstream theme handles switching and persistence. Keep toggle semantics
// synchronized with its data-mode attribute for keyboard/screen-reader users.
(() => {
  const update = () => {
    const mode = document.documentElement.dataset.mode;
    document.querySelectorAll('.oh-theme-picker button').forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.mode === mode));
    });
  };
  const setup = () => {
    update();
    new MutationObserver(update).observe(document.documentElement, {
      attributes: true, attributeFilter: ['data-mode']
    });
  };
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setup, {once: true});
  } else { setup(); }
})();
