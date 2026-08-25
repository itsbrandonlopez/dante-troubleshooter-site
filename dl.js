(function () {
  var ua = navigator.userAgent;
  var isWin = /Windows/i.test(ua);
  var isMac = !isWin && /Macintosh|Mac OS X/i.test(ua);

  document.querySelectorAll('a[data-dl]').forEach(function (a) {
    var kind = a.dataset.dl;
    if (kind === 'win') {
      a.classList.remove('cta-alt');
      a.classList.add('cta');
      a.textContent = 'Download for Windows';
      a.style.order = '-1';
    } else if (kind === 'mac-arm' && isWin) {
      a.classList.remove('cta');
      a.classList.add('cta-alt');
      a.textContent = 'Apple Silicon Mac';
    }
  });

  function keepOs(os) {
    document.querySelectorAll('.step[data-os]').forEach(function (el) {
      if (el.dataset.os !== os) el.style.display = 'none';
    });
  }
  if (isWin) {
    keepOs('win');
  } else if (isMac) {
    keepOs('mac');
  }
})();
