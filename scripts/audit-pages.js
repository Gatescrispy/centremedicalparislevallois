const { chromium } = require('playwright');

const BASE = 'http://localhost:3333';
const PAGES = [
  'index.html',
  'pages/ophtalmologie.html',
  'pages/kinesitherapie.html',
  'pages/soins-infirmiers.html',
  'pages/medecine-generale.html',
  'pages/le-centre.html',
  'pages/contact.html',
  'pages/tarifs.html',
  'pages/urgences.html',
  'pages/equipe.html',
  'pages/mentions-legales.html',
  'pages/politique-confidentialite.html',
  'pages/politique-cookies.html',
  'pages/landing/google-ads.html',
  'pages/ophtalmologie/premiere-consultation.html',
  'pages/ophtalmologie/premiere-consultation-enfant.html',
  'pages/ophtalmologie/consultation-suivi.html',
  'pages/ophtalmologie/renouvellement-lunettes-lentilles.html',
  'pages/ophtalmologie/champ-visuel-humphrey.html',
  'pages/ophtalmologie/urgence.html',
  'pages/kinesitherapie/premiere-consultation.html',
  'pages/kinesitherapie/consultation-suivi.html',
  'pages/kinesitherapie/reeducation-post-operatoire.html',
  'pages/kinesitherapie/reeducation-membres-superieurs.html',
  'pages/kinesitherapie/reeducation-membres-inferieurs.html',
  'pages/kinesitherapie/rachis-cervical-dorsal-lombaire.html',
  'pages/kinesitherapie/traumatisme-adulte.html',
  'pages/kinesitherapie/traumatisme-adolescent.html',
  'pages/kinesitherapie/scoliose-adolescent.html',
  'pages/kinesitherapie/drainage-lymphatique.html',
  'pages/kinesitherapie/femme-enceinte.html',
  'pages/kinesitherapie/electrotherapie.html',
  'pages/kinesitherapie/renforcement-abdominal.html',
  'pages/kinesitherapie/rhumatologie.html',
  'pages/kinesitherapie/seance-sans-ordonnance.html',
  'pages/soins-infirmiers/vaccination-adulte.html',
  'pages/soins-infirmiers/vaccination-pediatrique.html',
  'pages/soins-infirmiers/bilan-sanguin-ecbu.html',
  'pages/soins-infirmiers/injection.html',
  'pages/soins-infirmiers/pansement-simple.html',
  'pages/soins-infirmiers/pansement-post-chirurgical.html',
  'pages/soins-infirmiers/retrait-fils-agrafes.html',
  'pages/soins-infirmiers/surveillance-constantes.html',
  'pages/soins-infirmiers/test-antigenique.html',
  'pages/soins-infirmiers/bilan-prevention.html',
  'pages/medecine-generale/consultation.html',
  'pages/medecine-generale/urgence.html',
];

(async () => {
  const browser = await chromium.launch();
  const results = [];

  for (const p of PAGES) {
    const url = `${BASE}/${p}`;
    const page = await browser.newPage();
    const errors = [];
    const missing404 = [];

    page.on('console', msg => {
      if (msg.type() === 'error') errors.push(msg.text());
    });
    page.on('response', resp => {
      if (resp.status() === 404 && !resp.url().includes('favicon')) {
        missing404.push(resp.url().replace(BASE, ''));
      }
    });

    let status = 200;
    try {
      const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 10000 });
      status = resp ? resp.status() : 0;
      await page.waitForTimeout(800);
    } catch (e) {
      status = 0;
      errors.push('LOAD ERROR: ' + e.message);
    }

    // Check title
    const title = await page.title().catch(() => '');

    // Check h1
    const h1 = await page.$eval('h1', el => el.textContent.trim()).catch(() => 'MISSING H1');

    // Check canonical
    const canonical = await page.$eval('link[rel="canonical"]', el => el.href).catch(() => 'MISSING CANONICAL');

    // Check meta description
    const metaDesc = await page.$eval('meta[name="description"]', el => el.content).catch(() => 'MISSING META DESC');

    // Check header loaded
    const headerLoaded = await page.$eval('#header-placeholder nav', el => !!el).catch(() => false);

    // Check footer loaded
    const footerLoaded = await page.$eval('#footer-placeholder', el => el.innerHTML.length > 100).catch(() => false);

    // Check broken images (img with naturalWidth === 0)
    const brokenImgs = await page.evaluate(() => {
      return Array.from(document.querySelectorAll('img'))
        .filter(img => img.complete && img.naturalWidth === 0 && img.src && !img.src.includes('favicon'))
        .map(img => img.src.replace(window.location.origin, ''));
    });

    results.push({
      page: p,
      status,
      title,
      h1,
      canonical: canonical.replace(BASE, '').replace('https://www.centremedicalparislevallois.fr', ''),
      metaDescLength: metaDesc === 'MISSING META DESC' ? 'MISSING' : metaDesc.length,
      headerLoaded,
      footerLoaded,
      errors: errors.filter(e => !e.includes('favicon')),
      missing404: missing404.filter(u => !u.includes('favicon')),
      brokenImgs,
    });

    await page.close();
  }

  await browser.close();

  // Print report
  let issueCount = 0;
  for (const r of results) {
    const issues = [];
    if (r.status !== 200) issues.push(`HTTP ${r.status}`);
    if (r.h1 === 'MISSING H1') issues.push('No H1');
    if (r.canonical === 'MISSING CANONICAL') issues.push('No canonical');
    if (r.metaDescLength === 'MISSING') issues.push('No meta description');
    if (!r.headerLoaded) issues.push('Header not loaded');
    if (!r.footerLoaded) issues.push('Footer not loaded');
    if (r.errors.length) issues.push(`${r.errors.length} console error(s)`);
    if (r.missing404.length) issues.push(`404: ${r.missing404.join(', ')}`);
    if (r.brokenImgs.length) issues.push(`Broken imgs: ${r.brokenImgs.join(', ')}`);

    if (issues.length) {
      issueCount++;
      console.log(`\n❌ ${r.page}`);
      issues.forEach(i => console.log(`   → ${i}`));
      if (r.errors.length) r.errors.forEach(e => console.log(`   [ERR] ${e.substring(0, 120)}`));
    } else {
      console.log(`✅ ${r.page}`);
    }
  }

  console.log(`\n=== ${issueCount} pages with issues / ${results.length} total ===`);
})();
