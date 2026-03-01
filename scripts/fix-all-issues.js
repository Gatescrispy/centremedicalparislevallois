const fs = require('fs');
const path = require('path');

const BASE = path.join(__dirname, '..');
const SITE = 'https://www.centremedicalparislevallois.fr';

// ═══════════════════════════════════════════
// 1. BROKEN IMAGE FIXES
// ═══════════════════════════════════════════
const IMG_FIXES = [
  // Hero images
  { file: 'pages/soins-infirmiers/test-antigenique.html',  from: '/covid-test.jpg',                 to: '/Test Antigène Nursing.jpeg' },
  { file: 'pages/soins-infirmiers/bilan-prevention.html',  from: '/Senior health checkup.jpeg',      to: '/Nursing Constant Monitoring.webp' },
  // Carousel card images
  { from: '/Bilan Prévention Santé.jpg',    to: '/Nursing Constant Monitoring.webp',        files: 'all' },
  { from: '/Mon Bilan Prévention.jpg',      to: '/Nursing Constant Monitoring.webp',        files: 'all' },
  { from: '/Retrait Fils Sutures.jpg',      to: '/Retrait de points de suture abdomen.webp', files: 'all' },
];

// ═══════════════════════════════════════════
// 2. BROKEN LINK FIX
// ═══════════════════════════════════════════
const LINK_FIXES = [
  { file: 'pages/soins-infirmiers.html', from: 'bilan-sanguin.html"', to: 'bilan-sanguin-ecbu.html"' },
];

// ═══════════════════════════════════════════
// 3. OG TAGS — per page data
// ═══════════════════════════════════════════
const OG_DATA = {
  'pages/mentions-legales.html':            { title: 'Mentions légales | Centre Médical Paris-Levallois',           desc: 'Mentions légales du Centre Médical Paris-Levallois, 60 rue Victor Hugo, Levallois-Perret.',                              img: '/hero-centre-medical.jpg' },
  'pages/politique-confidentialite.html':   { title: 'Politique de confidentialité | Centre Médical Paris-Levallois', desc: 'Politique de confidentialité et protection des données personnelles du Centre Médical Paris-Levallois.',             img: '/hero-centre-medical.jpg' },
  'pages/politique-cookies.html':           { title: 'Politique cookies | Centre Médical Paris-Levallois',           desc: 'Politique de gestion des cookies du Centre Médical Paris-Levallois.',                                                img: '/hero-centre-medical.jpg' },
  'pages/landing/google-ads.html':          { title: 'Centre Médical Paris-Levallois | Médecin, Kiné, Ophtalmo',    desc: 'Centre médical pluridisciplinaire à Levallois-Perret. Ophtalmologie, kinésithérapie, soins infirmiers, médecine générale.', img: '/hero-centre-medical.jpg' },

  'pages/ophtalmologie/premiere-consultation.html':           { title: 'Première Consultation Ophtalmologue Levallois | Bilan Vue',                    desc: 'Bilan ophtalmologique complet à Levallois-Perret : acuité visuelle, fond d\'œil, dépistage pathologies. RDV en ligne.',   img: '/img-premiere-consultation.jpg' },
  'pages/ophtalmologie/premiere-consultation-enfant.html':    { title: 'Consultation Ophtalmologie Enfant Levallois | Dépistage',                       desc: 'Examen ophtalmologique pédiatrique à Levallois. Dépistage amblyopie, strabisme, suivi de la vue de l\'enfant.',             img: '/img-consultation-enfant.jpg' },
  'pages/ophtalmologie/consultation-suivi.html':              { title: 'Consultation Suivi Ophtalmologique Levallois | Glaucome, DMLA',                  desc: 'Suivi ophtalmologique à Levallois-Perret : glaucome, DMLA, cataracte, diabète oculaire. Prenez RDV en ligne.',              img: '/img-consultation-suivi.jpg' },
  'pages/ophtalmologie/renouvellement-lunettes-lentilles.html':{ title: 'Renouvellement Lunettes & Lentilles Levallois | Ophtalmologue',                desc: 'Renouvellement d\'ordonnance lunettes ou lentilles à Levallois-Perret. Consultation ophtalmologue ou orthoptiste.',          img: '/img-lunettes-lentilles.webp' },
  'pages/ophtalmologie/champ-visuel-humphrey.html':           { title: 'Champ Visuel Levallois | Examen Glaucome Humphrey',                              desc: 'Examen du champ visuel à Levallois-Perret. Dépistage et suivi du glaucome par périmétrie Humphrey.',                       img: '/img-champ-visuel.jpg' },
  'pages/ophtalmologie/urgence.html':                         { title: 'Urgence Ophtalmologique Levallois | Corps Étranger, Œil Rouge',                  desc: 'Consultation urgence ophtalmo à Levallois : corps étranger, baisse de vision, œil rouge, traumatisme oculaire.',           img: '/img-urgence-ophtalmo.webp' },

  'pages/kinesitherapie/premiere-consultation.html':          { title: 'Première Consultation Kinésithérapie Levallois | Bilan Kiné',                   desc: 'Bilan kinésithérapique initial à Levallois-Perret. Évaluation complète et prescription de séances de rééducation.',        img: '/Brisbane Shoulder Pain Physio.jpg' },
  'pages/kinesitherapie/consultation-suivi.html':             { title: 'Consultation Suivi Kiné Levallois | Rééducation',                                desc: 'Séances de suivi kinésithérapique à Levallois-Perret. Progression et ajustement de votre rééducation.',                    img: '/Consultation physiothérapie.jpg' },
  'pages/kinesitherapie/reeducation-post-operatoire.html':    { title: 'Rééducation Post-Opératoire Levallois | Kinésithérapie',                        desc: 'Rééducation après chirurgie à Levallois : orthopédie, traumatologie. Reprise de la mobilité avec notre kinésithérapeute.',  img: '/Réhabilitation post-opératoire.jpeg' },
  'pages/kinesitherapie/reeducation-membres-superieurs.html': { title: 'Rééducation Membres Supérieurs Levallois | Épaule, Coude',                      desc: 'Kiné épaule, coude, poignet, main à Levallois-Perret. Tendinites, capsulites, fractures membres supérieurs.',               img: '/Physiothérapie membres supérieurs.jpg' },
  'pages/kinesitherapie/reeducation-membres-inferieurs.html': { title: 'Rééducation Membres Inférieurs Levallois | Hanche, Genou',                      desc: 'Kiné hanche, genou, cheville à Levallois-Perret. Prothèses, ligaments, entorses membres inférieurs.',                      img: '/Réhabilitation membre inférieur.jpg' },
  'pages/kinesitherapie/rachis-cervical-dorsal-lombaire.html':{ title: 'Kiné Rachis Levallois | Cervical, Lombaire, Hernie',                             desc: 'Kinésithérapie colonne vertébrale à Levallois-Perret. Hernie discale, lombalgie, cervicalgie, dorsalgie.',                   img: '/Physiothérapie de la colonne vertébrale.webp' },
  'pages/kinesitherapie/traumatisme-adulte.html':             { title: 'Kiné Traumatologie Levallois | Entorse, Fracture, Luxation',                     desc: 'Rééducation après traumatisme à Levallois : entorse, fracture, luxation, accident de sport. Prise en charge rapide.',        img: '/Physiothérapie Trauma Adulte.jpg.webp' },
  'pages/kinesitherapie/traumatisme-adolescent.html':         { title: 'Kiné Traumatisme Adolescent Levallois | Rééducation Jeune',                      desc: 'Kinésithérapie pour adolescents à Levallois-Perret. Fractures, entorses, blessures sportives chez les jeunes.',            img: '/Santé Adolescent Injuries.jpg' },
  'pages/kinesitherapie/scoliose-adolescent.html':            { title: 'Kiné Scoliose Adolescent Levallois | Rééducation Posturale',                     desc: 'Kinésithérapie pour la scoliose à Levallois-Perret. Correction posturale, renforcement musculaire chez l\'adolescent.',      img: '/Scoliose adolescent physiothérapie.jpeg' },
  'pages/kinesitherapie/drainage-lymphatique.html':           { title: 'Drainage Lymphatique Levallois | Post-Op, Femme Enceinte',                       desc: 'Drainage lymphatique à Levallois-Perret : membres supérieurs et inférieurs, post-opératoire ou grossesse.',                  img: '/Drainage Lymphatique Physiothérapie.jpg' },
  'pages/kinesitherapie/femme-enceinte.html':                 { title: 'Kiné Femme Enceinte Levallois | Prénatale, Jambes Lourdes',                      desc: 'Kinésithérapie prénatale à Levallois-Perret. Drainage jambes lourdes, préparation à l\'accouchement pendant la grossesse.',   img: '/Physiothérapie femmes enceintes et postpartum.jpg' },
  'pages/kinesitherapie/electrotherapie.html':                { title: 'Électrothérapie Levallois | Antalgique, Renforcement Musculaire',                 desc: 'Électrothérapie kinésithérapique à Levallois-Perret : antalgique, renforcement musculaire, traitement jambes lourdes.',       img: '/Electrothérapie physiothérapie.jpg' },
  'pages/kinesitherapie/renforcement-abdominal.html':         { title: 'Renforcement Abdominal Levallois | Kiné Gainage',                                 desc: 'Séances de renforcement abdominal à Levallois-Perret. Gainage, rééducation post-partum, abdominaux avec kinésithérapeute.',  img: '/Physiothérapie Renforcement Abdominal.jpeg' },
  'pages/kinesitherapie/rhumatologie.html':                   { title: 'Kiné Rhumatologie Levallois | Arthrose, Polyarthrite',                            desc: 'Kinésithérapie rhumatologique à Levallois-Perret. Arthrose, polyarthrite rhumatoïde, fibromyalgie. Prise en charge globale.',  img: '/Rhumatisme articulaire.jpg' },
  'pages/kinesitherapie/seance-sans-ordonnance.html':         { title: 'Kiné Sans Ordonnance Levallois | Séance Libre',                                   desc: 'Séances de kinésithérapie sans ordonnance à Levallois-Perret. Jusqu\'à 8 séances libres, bien-être et prévention.',          img: '/Physiothérapie sans prescription.jpeg' },

  'pages/soins-infirmiers/vaccination-adulte.html':           { title: 'Vaccination Adulte Levallois | Grippe, COVID, DTP',                               desc: 'Vaccination adulte à Levallois-Perret : grippe, COVID-19, rappels DTP, hépatite, fièvre jaune. Sans ordonnance.',            img: '/Vaccination Adulte.jpg' },
  'pages/soins-infirmiers/vaccination-pediatrique.html':      { title: 'Vaccination Pédiatrique Levallois | Vaccins Enfants',                             desc: 'Vaccination pédiatrique à Levallois-Perret. Vaccins obligatoires et recommandés pour nourrissons et enfants.',               img: '/Vaccination pédiatrique.jpeg' },
  'pages/soins-infirmiers/bilan-sanguin-ecbu.html':           { title: 'Bilan Sanguin & ECBU Levallois | Prise de Sang',                                  desc: 'Prise de sang et ECBU à Levallois-Perret sur ordonnance. Bilan sanguin, glycémie, NFS, analyses urinaires.',                 img: '/Test de Sang.webp' },
  'pages/soins-infirmiers/injection.html':                    { title: 'Injection Infirmière Levallois | IM, SC, IV',                                      desc: 'Injections intramusculaires, sous-cutanées et intraveineuses à Levallois-Perret. Sur ordonnance médicale.',                  img: "/Préparation d'injection.jpg" },
  'pages/soins-infirmiers/pansement-simple.html':             { title: 'Pansement Simple Levallois | Soins de Plaies',                                    desc: 'Soins de plaies et pansements simples à Levallois-Perret. Brûlures, plaies légères, cicatrisation.',                         img: '/Cutiplast Steril Island Dressing.jpg' },
  'pages/soins-infirmiers/pansement-post-chirurgical.html':   { title: 'Pansement Post-Chirurgical Levallois | Soins Complexes',                          desc: 'Pansements post-chirurgicaux complexes à Levallois-Perret. Suivi cicatrisation après opération, soins infirmiers.',          img: '/Types de pansements post-chirurgicaux.jpg' },
  'pages/soins-infirmiers/retrait-fils-agrafes.html':         { title: 'Retrait Fils & Agrafes Levallois | Soins Infirmiers',                             desc: 'Retrait de fils et agrafes à Levallois-Perret. Ablation des points de suture après cicatrisation, sur ordonnance.',          img: '/Retrait de points de suture abdomen.webp' },
  'pages/soins-infirmiers/surveillance-constantes.html':      { title: 'Surveillance Constantes Levallois | Tension, Glycémie',                            desc: 'Surveillance des constantes à Levallois-Perret : tension artérielle, glycémie, température, saturation. Sur ordonnance.',    img: '/Nursing Constant Monitoring.webp' },
  'pages/soins-infirmiers/test-antigenique.html':             { title: 'Test Antigénique Levallois | COVID, Grippe',                                       desc: 'Tests antigéniques rapides à Levallois-Perret : COVID-19, grippe. Résultat en 15 minutes, sans ordonnance.',                 img: '/Test Antigène Nursing.jpeg' },
  'pages/soins-infirmiers/bilan-prevention.html':             { title: 'Mon Bilan Prévention Levallois | 18-25, 45-50, 60-65, 70-75 ans',                 desc: 'Bilan de prévention gratuit à Levallois-Perret. Pris en charge par l\'Assurance Maladie selon votre tranche d\'âge.',        img: '/Nursing Constant Monitoring.webp' },

  'pages/medecine-generale/consultation.html':                { title: 'Médecin Généraliste Levallois | Consultation, Ordonnance',                        desc: 'Consultation médecine générale à Levallois-Perret. Diagnostic, traitement, ordonnances, certificats médicaux. Secteur 1.',   img: '/Consultation docteur patient.jpg' },
  'pages/medecine-generale/urgence.html':                     { title: 'Consultation Urgence Médecin Levallois | Sans RDV',                               desc: 'Consultation urgence médicale à Levallois-Perret. Fièvre, infection, douleur aiguë. Créneaux urgence sans rendez-vous.',     img: '/Soins main blessée.jpg' },
};

// ═══════════════════════════════════════════
// APPLY FIXES
// ═══════════════════════════════════════════

let fixedCount = 0;

// --- 1. Broken images ---
function fixImages(content, fixes, filePath) {
  let changed = false;
  for (const fix of fixes) {
    if (fix.file && fix.file !== filePath) continue;
    if (content.includes(fix.from)) {
      content = content.split(fix.from).join(fix.to);
      changed = true;
    }
  }
  return { content, changed };
}

// --- 2. OG tags ---
function addOgTags(content, ogData) {
  if (content.includes('og:title')) return { content, changed: false };

  const ogBlock = `
    <meta property="og:type" content="website">
    <meta property="og:title" content="${ogData.title}">
    <meta property="og:description" content="${ogData.desc}">
    <meta property="og:image" content="${SITE}${ogData.img}">
    <meta property="og:locale" content="fr_FR">`;

  // Insert before </head>
  const newContent = content.replace('</head>', ogBlock + '\n</head>');
  return { content: newContent, changed: newContent !== content };
}

// --- 3. Broken link fixes ---
function fixLinks(content, fixes, filePath) {
  let changed = false;
  for (const fix of fixes) {
    if (fix.file !== filePath) continue;
    if (content.includes(fix.from)) {
      content = content.split(fix.from).join(fix.to);
      changed = true;
    }
  }
  return { content, changed };
}

// --- 4. Canonical for landing page ---
function addCanonical(content, filePath) {
  if (content.includes('rel="canonical"')) return { content, changed: false };
  const url = `${SITE}/${filePath}`;
  const tag = `    <link rel="canonical" href="${url}">\n`;
  const newContent = content.replace('</head>', tag + '</head>');
  return { content: newContent, changed: newContent !== content };
}

// Process all files
const ALL_FILES = [
  ...Object.keys(OG_DATA),
  'pages/soins-infirmiers.html',
  'pages/soins-infirmiers/injection.html',
  'pages/soins-infirmiers/pansement-simple.html',
  'pages/soins-infirmiers/pansement-post-chirurgical.html',
  'pages/soins-infirmiers/surveillance-constantes.html',
  'pages/soins-infirmiers/test-antigenique.html',
  'pages/soins-infirmiers/bilan-prevention.html',
];
const uniqueFiles = [...new Set(ALL_FILES)];

for (const rel of uniqueFiles) {
  const full = path.join(BASE, rel);
  if (!fs.existsSync(full)) { console.log(`MISSING: ${rel}`); continue; }

  let content = fs.readFileSync(full, 'utf8');
  const changes = [];

  // Image fixes (global - apply to all files)
  const globalImgFixes = IMG_FIXES.filter(f => f.files === 'all');
  const fileImgFixes = IMG_FIXES.filter(f => f.file === rel);
  const allImgFixes = [...globalImgFixes, ...fileImgFixes];
  const imgResult = fixImages(content, allImgFixes, rel);
  if (imgResult.changed) { content = imgResult.content; changes.push('fixed images'); }

  // Link fixes
  const linkResult = fixLinks(content, LINK_FIXES, rel);
  if (linkResult.changed) { content = linkResult.content; changes.push('fixed links'); }

  // OG tags
  if (OG_DATA[rel]) {
    const ogResult = addOgTags(content, OG_DATA[rel]);
    if (ogResult.changed) { content = ogResult.content; changes.push('added OG tags'); }
  }

  // Canonical (only landing)
  if (rel === 'pages/landing/google-ads.html') {
    const canonResult = addCanonical(content, rel);
    if (canonResult.changed) { content = canonResult.content; changes.push('added canonical'); }
  }

  if (changes.length) {
    fs.writeFileSync(full, content, 'utf8');
    console.log(`✅ ${rel} → ${changes.join(', ')}`);
    fixedCount++;
  }
}

console.log(`\n✅ ${fixedCount} files updated`);
