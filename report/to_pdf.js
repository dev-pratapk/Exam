const { chromium } = require('playwright');
(async () => {
  const [,, src, out, title = 'MA3354 Discrete Mathematics — Exam Pattern Analysis'] = process.argv;
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + src, { waitUntil: 'load' });
  await p.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:7pt;color:#777;width:100%;text-align:center;font-family:DejaVu Sans">' + title + ' · page <span class="pageNumber"></span> of <span class="totalPages"></span></div>' });
  await b.close();
})();
