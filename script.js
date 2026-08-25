// Language switcher
(function () {
  var btnCn = document.getElementById('btn-cn');
  var btnEn = document.getElementById('btn-en');
  var contentCn = document.getElementById('lang-cn');
  var contentEn = document.getElementById('lang-en');

  // Default language from URL hash or browser setting
  var defaultLang = window.location.hash === '#en' ? 'en' : 'cn';
  setLang(defaultLang);

  btnCn.addEventListener('click', function () { setLang('cn'); });
  btnEn.addEventListener('click', function () { setLang('en'); });
  window.addEventListener('hashchange', function () {
    setLang(window.location.hash === '#en' ? 'en' : 'cn');
  });

  function setLang(lang) {
    if (lang === 'cn') {
      contentCn.style.display = '';
      contentEn.style.display = 'none';
      btnCn.classList.add('active');
      btnEn.classList.remove('active');
      btnCn.setAttribute('aria-pressed', 'true');
      btnEn.setAttribute('aria-pressed', 'false');
      contentCn.setAttribute('aria-hidden', 'false');
      contentEn.setAttribute('aria-hidden', 'true');
      window.location.hash = '';
      document.documentElement.lang = 'zh-CN';
    } else {
      contentCn.style.display = 'none';
      contentEn.style.display = '';
      btnCn.classList.remove('active');
      btnEn.classList.add('active');
      btnCn.setAttribute('aria-pressed', 'false');
      btnEn.setAttribute('aria-pressed', 'true');
      contentCn.setAttribute('aria-hidden', 'true');
      contentEn.setAttribute('aria-hidden', 'false');
      window.location.hash = '#en';
      document.documentElement.lang = 'en';
    }
    // Re-render MathJax after language switch
    if (window.MathJax && window.MathJax.typeset) {
      window.MathJax.typeset();
    }
  }
})();
