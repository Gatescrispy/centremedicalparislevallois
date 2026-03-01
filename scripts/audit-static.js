const fs = require('fs');
const path = require('path');

const BASE = path.join(__dirname, '..');
const PAGES = [
  'index.html',
  'pages/ophtalmologie.html','pages/kinesitherapie.html','pages/soins-infirmiers.html','pages/medecine-generale.html',
  'pages/le-centre.html','pages/contact.html','pages/tarifs.html','pages/urgences.html','pages/equipe.html',
  'pages/mentions-legales.html','pages/politique-confidentialite.html','pages/politique-cookies.html',
  'pages/landing/google-ads.html',
  'pages/ophtalmologie/premiere-consultation.html','pages/ophtalmologie/premiere-consultation-enfant.html',
  'pages/ophtalmologie/consultation-suivi.html','pages/ophtalmologie/renouvellement-lunettes-lentilles.html',
  'pages/ophtalmologie/champ-visuel-humphrey.html','pages/ophtalmologie/urgence.html',
  'pages/kinesitherapie/premiere-consultation.html','pages/kinesitherapie/consultation-suivi.html',
  'pages/kinesitherapie/reeducation-post-operatoire.html','pages/kinesitherapie/reeducation-membres-superieurs.html',
  'pages/kinesitherapie/reeducation-membres-inferieurs.html','pages/kinesitherapie/rachis-cervical-dorsal-lombaire.html',
  'pages/kinesitherapie/traumatisme-adulte.html','pages/kinesitherapie/traumatisme-adolescent.html',
  'pages/kinesitherapie/scoliose-adolescent.html','pages/kinesitherapie/drainage-lymphatique.html',
  'pages/kinesitherapie/femme-enceinte.html','pages/kinesitherapie/electrotherapie.html',
  'pages/kinesitherapie/renforcement-abdominal.html','pages/kinesitherapie/rhumatologie.html',
  'pages/kinesitherapie/seance-sans-ordonnance.html',
  'pages/soins-infirmiers/vaccination-adulte.html','pages/soins-infirmiers/vaccination-pediatrique.html',
  'pages/soins-infirmiers/bilan-sanguin-ecbu.html','pages/soins-infirmiers/injection.html',
  'pages/soins-infirmiers/pansement-simple.html','pages/soins-infirmiers/pansement-post-chirurgical.html',
  'pages/soins-infirmiers/retrait-fils-agrafes.html','pages/soins-infirmiers/surveillance-constantes.html',
  'pages/soins-infirmiers/test-antigenique.html','pages/soins-infirmiers/bilan-prevention.html',
  'pages/medecine-generale/consultation.html','pages/medecine-generale/urgence.html',
];

function extractAll(html, regex) {
  const matches = [];
  let m;
  const r = new RegExp(regex.source, 'gi');
  while ((m = r.exec(html)) !== null) matches.push(m[1] || m[0]);
  return matches;
}

function checkImageExists(imgSrc, pageFile) {
  if (!imgSrc || imgSrc.startsWith('http') || imgSrc.startsWith('data:')) return true;
  const absPath = path.join(BASE, imgSrc.replace(/^\//, ''));
  return fs.existsSync(absPath);
}

const issues = {};
const allIssues = [];

for (const rel of PAGES) {
  const full = path.join(BASE, rel);
  if (!fs.existsSync(full)) {
    allIssues.push({ page: rel, type: 'MISSING_FILE', detail: 'File does not exist' });
    continue;
  }
  const html = fs.readFileSync(full, 'utf8');
  const pageIssues = [];

  // H1
  if (!/<h1[\s>]/i.test(html)) pageIssues.push({ type: 'SEO', detail: 'Missing <h1>' });

  // Meta description
  if (!/<meta\s+name="description"/i.test(html)) pageIssues.push({ type: 'SEO', detail: 'Missing meta description' });

  // Canonical
  if (!/<link\s+rel="canonical"/i.test(html)) pageIssues.push({ type: 'SEO', detail: 'Missing canonical link' });

  // Title
  const titleMatch = html.match(/<title>([^<]*)<\/title>/i);
  if (!titleMatch) pageIssues.push({ type: 'SEO', detail: 'Missing <title>' });

  // OG tags
  if (!html.includes('og:title')) pageIssues.push({ type: 'SEO', detail: 'Missing og:title' });
  if (!html.includes('og:description')) pageIssues.push({ type: 'SEO', detail: 'Missing og:description' });

  // Broken image src refs (local only)
  const imgSrcs = extractAll(html, /src="([^"]+\.(jpg|jpeg|png|webp|gif|svg))"/i);
  for (const src of imgSrcs) {
    if (!checkImageExists(src, rel)) {
      pageIssues.push({ type: 'BROKEN_IMG', detail: src });
    }
  }

  // Check for header-placeholder
  if (!html.includes('header-placeholder')) pageIssues.push({ type: 'LAYOUT', detail: 'Missing header-placeholder' });

  // Check for footer-placeholder
  if (!html.includes('footer-placeholder')) pageIssues.push({ type: 'LAYOUT', detail: 'Missing footer-placeholder' });

  // Check tailwind / stylesheet
  if (!html.includes('tailwind') && !html.includes('output.css') && !html.includes('cdn.tailwind')) {
    pageIssues.push({ type: 'CSS', detail: 'No Tailwind CSS reference' });
  }

  // Check source=profile (old Doctolib param)
  if (html.includes('source=profile')) pageIssues.push({ type: 'DOCTOLIB', detail: 'source=profile found (should be deep_link)' });

  // Check for bilan-sanguin.html (old wrong link)
  if (html.includes('bilan-sanguin.html"') && !html.includes('bilan-sanguin-ecbu')) {
    pageIssues.push({ type: 'BROKEN_LINK', detail: 'Link to old bilan-sanguin.html (should be bilan-sanguin-ecbu.html)' });
  }

  // Breadcrumb check for exam pages
  if (rel.includes('/ophtalmologie/') || rel.includes('/kinesitherapie/') || rel.includes('/soins-infirmiers/') || rel.includes('/medecine-generale/')) {
    if (!html.includes('breadcrumb') && !html.includes('Accueil')) {
      pageIssues.push({ type: 'LAYOUT', detail: 'Missing breadcrumb' });
    }
  }

  if (pageIssues.length) {
    issues[rel] = pageIssues;
    allIssues.push(...pageIssues.map(i => ({ page: rel, ...i })));
  }
}

// Summary
let totalIssues = 0;
for (const [page, pIssues] of Object.entries(issues)) {
  console.log(`\n❌ ${page}`);
  for (const i of pIssues) {
    console.log(`   [${i.type}] ${i.detail}`);
    totalIssues++;
  }
}

// Group by type
const byType = {};
for (const i of allIssues) {
  byType[i.type] = (byType[i.type] || 0) + 1;
}
console.log('\n=== SUMMARY BY TYPE ===');
for (const [t, c] of Object.entries(byType).sort((a,b) => b[1]-a[1])) {
  console.log(`  ${t}: ${c}`);
}
console.log(`\nTotal: ${totalIssues} issues across ${Object.keys(issues).length} pages`);
