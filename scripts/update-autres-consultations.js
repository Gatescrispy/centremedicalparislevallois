const fs = require('fs');
const path = require('path');

const MOTIF_CARD_CSS = `.motif-card{background:white;border-radius:12px;box-shadow:0 4px 15px rgba(0,0,0,0.1);overflow:hidden;transition:all 0.3s;border:2px solid transparent;display:flex;flex-direction:column;text-decoration:none;}.motif-card:hover{border-color:#00a7de;box-shadow:0 12px 30px rgba(0,167,222,0.15);transform:translateY(-4px);text-decoration:none;}.motif-card h3,.motif-card p,.motif-card span{text-decoration:none;}.motif-card-img{height:160px;object-fit:cover;width:100%;}.motif-card-content{padding:1.25rem;display:flex;flex-direction:column;flex-grow:1;}`;

const CARDS = {
  ophtalmologie: [
    { href: 'premiere-consultation.html',         img: '/img-premiere-consultation.jpg',                          alt: 'Examen ophtalmologique',             title: 'Première consultation',            desc: 'Examen complet de la vue, fond d\'œil, dépistage pathologies oculaires.' },
    { href: 'premiere-consultation-enfant.html',  img: '/img-consultation-enfant.jpg',                            alt: 'Consultation ophtalmologie enfant',   title: 'Consultation enfant',              desc: 'Examen ophtalmologique pédiatrique, dépistage amblyopie, strabisme.' },
    { href: 'consultation-suivi.html',            img: '/img-consultation-suivi.jpg',                             alt: 'Consultation de suivi',               title: 'Consultation de suivi',            desc: 'Suivi pathologies : glaucome, DMLA, cataracte, diabète oculaire.' },
    { href: 'renouvellement-lunettes-lentilles.html', img: '/img-lunettes-lentilles.webp',                        alt: 'Lunettes et lentilles',               title: 'Renouvellement lunettes/lentilles', desc: 'Nouvelle prescription de verres correcteurs ou lentilles de contact.' },
    { href: 'champ-visuel-humphrey.html',         img: '/img-champ-visuel.jpg',                                   alt: 'Champ visuel Humphrey',               title: 'Champ visuel',                     desc: 'Examen du champ visuel. Dépistage et suivi du glaucome.' },
    { href: 'urgence.html',                       img: '/img-urgence-ophtalmo.webp',                              alt: 'Urgence ophtalmologique',             title: 'Urgence ophtalmologique',          desc: 'Corps étranger, baisse brutale de vision, œil rouge douloureux.' },
  ],
  kinesitherapie: [
    { href: 'premiere-consultation.html',         img: '/Brisbane Shoulder Pain Physio.jpg',                     alt: 'Première consultation kinésithérapie', title: 'Première consultation',           desc: 'Bilan et évaluation kinésithérapique initial.' },
    { href: 'consultation-suivi.html',            img: '/Consultation physiothérapie.jpg',                       alt: 'Consultation de suivi kinésithérapie', title: 'Consultation de suivi',           desc: 'Suivi régulier de votre rééducation kinésithérapique.' },
    { href: 'reeducation-post-operatoire.html',   img: '/Réhabilitation post-opératoire.jpeg',                      alt: 'Rééducation post-opératoire',         title: 'Rééducation post-opératoire',     desc: 'Traumatologie, orthopédie. Récupération après chirurgie.' },
    { href: 'reeducation-membres-superieurs.html',img: '/Physiothérapie membres supérieurs.jpg',                 alt: 'Rééducation membres supérieurs',      title: 'Membres supérieurs',              desc: 'Épaule, coude, poignet, main. Tendinites, capsulites.' },
    { href: 'reeducation-membres-inferieurs.html',img: '/Réhabilitation membre inférieur.jpg',                   alt: 'Rééducation membres inférieurs',      title: 'Membres inférieurs',              desc: 'Hanche, genou, cheville, pied. Prothèses, ligaments.' },
    { href: 'rachis-cervical-dorsal-lombaire.html',img: '/Physiothérapie de la colonne vertébrale.webp',         alt: 'Rachis colonne vertébrale',           title: 'Rachis (colonne vertébrale)',      desc: 'Cervical, dorsal, lombaire. Hernies, lombalgies.' },
    { href: 'traumatisme-adulte.html',            img: '/Physiothérapie Trauma Adulte.jpg.webp',                 alt: 'Traumatisme adulte',                  title: 'Traumatisme adulte',              desc: 'Fractures, entorses. Rééducation après immobilisation.' },
    { href: 'traumatisme-adolescent.html',        img: '/Santé Adolescent Injuries.jpg',                         alt: 'Traumatisme adolescent',              title: 'Traumatisme adolescent',          desc: 'Fractures, entorses. Prise en charge adaptée aux jeunes.' },
    { href: 'scoliose-adolescent.html',           img: '/Scoliose adolescent physiothérapie.jpeg',               alt: 'Scoliose adolescent',                 title: 'Scoliose adolescent',             desc: 'Correction posturale, renforcement musculaire.' },
    { href: 'drainage-lymphatique.html',          img: '/Drainage Lymphatique Physiothérapie.jpg',               alt: 'Drainage lymphatique',                title: 'Drainage lymphatique',            desc: 'Post-opératoire ou femme enceinte. Membres supérieurs/inférieurs.' },
    { href: 'femme-enceinte.html',                img: '/Physiothérapie femmes enceintes et postpartum.jpg',     alt: 'Femme enceinte',                      title: 'Femme enceinte',                  desc: 'Kiné prénatale, drainage jambes lourdes, préparation.' },
    { href: 'electrotherapie.html',               img: '/Electrothérapie physiothérapie.jpg',                    alt: 'Électrothérapie',                     title: 'Électrothérapie',                 desc: 'Antalgique, renforcement musculaire, jambes lourdes.' },
    { href: 'renforcement-abdominal.html',        img: '/Physiothérapie Renforcement Abdominal.jpeg',            alt: 'Renforcement abdominal',              title: 'Renforcement abdominal',          desc: 'Gainage, rééducation abdominale, post-partum.' },
    { href: 'rhumatologie.html',                  img: '/Rhumatisme articulaire.jpg',                            alt: 'Rhumatologie',                        title: 'Rhumatologie',                    desc: 'Arthrose, polyarthrite, fibromyalgie.' },
    { href: 'seance-sans-ordonnance.html',        img: '/Physiothérapie sans prescription.jpeg',                 alt: 'Séance sans ordonnance',              title: 'Séance sans ordonnance',          desc: "Jusqu'à 8 séances sans prescription médicale." },
  ],
  'soins-infirmiers': [
    { href: 'vaccination-adulte.html',            img: '/Vaccination Adulte.jpg',                                alt: 'Vaccination adulte',                  title: 'Vaccination adulte',              desc: 'Grippe, COVID-19, rappels DTP, hépatite, fièvre jaune...' },
    { href: 'vaccination-pediatrique.html',       img: '/Vaccination pédiatrique.jpeg',                          alt: 'Vaccination pédiatrique',             title: 'Vaccination pédiatrique',         desc: 'Vaccins obligatoires et recommandés pour enfants et nourrissons.' },
    { href: 'bilan-sanguin-ecbu.html',            img: '/Test de Sang.webp',                                     alt: 'Bilan sanguin',                       title: 'Bilan sanguin / ECBU',            desc: 'Prises de sang sur ordonnance, analyses urinaires.' },
    { href: 'injection.html',                     img: "/Préparation d'injection.jpg",                           alt: 'Injection',                           title: 'Injection',                       desc: 'Injections intramusculaires, sous-cutanées, intraveineuses.' },
    { href: 'pansement-simple.html',              img: '/Cutiplast Steril Island Dressing.jpg',                  alt: 'Pansement simple',                    title: 'Pansement simple',                desc: 'Soins de plaies, cicatrisation, changement de pansement.' },
    { href: 'pansement-post-chirurgical.html',    img: '/Types de pansements post-chirurgicaux.jpg',             alt: 'Pansement post-chirurgical',          title: 'Pansement post-chirurgical',      desc: 'Pansements complexes après opération, suivi cicatrisation.' },
    { href: 'retrait-fils-agrafes.html',          img: '/Retrait de points de suture abdomen.webp',             alt: 'Retrait de fils ou agrafes',          title: 'Retrait de fils ou agrafes',      desc: 'Ablation des points de suture après cicatrisation.' },
    { href: 'surveillance-constantes.html',       img: '/Nursing Constant Monitoring.webp',                     alt: 'Surveillance des constantes',         title: 'Surveillance des constantes',     desc: 'Tension, glycémie, température, saturation en oxygène.' },
    { href: 'test-antigenique.html',              img: '/Test Antigène Nursing.jpeg',                            alt: 'Test antigénique',                    title: 'Test antigénique',                desc: 'Tests rapides COVID-19, grippe. Résultat en 15 minutes.' },
    { href: 'bilan-prevention.html',              img: '/Bilan Prévention Santé.jpg',                            alt: 'Bilan prévention',                    title: 'Mon Bilan Prévention',            desc: 'Bilan de prévention selon votre tranche d\'âge (18 à 75 ans).' },
  ],
  'medecine-generale': [
    { href: 'consultation.html',                  img: '/Consultation docteur patient.jpg',                      alt: 'Consultation médecine générale',      title: 'Consultation de médecine générale', desc: 'Diagnostic, traitement, ordonnances, certificats médicaux.' },
    { href: 'urgence.html',                       img: '/Soins main blessée.jpg',                                alt: 'Consultation urgence',                title: 'Consultation urgence',            desc: 'Fièvre, infection, douleur aiguë, symptômes inhabituels. Créneaux réservés.' },
  ],
};

const SECTION_TITLES = {
  ophtalmologie: 'Autres consultations ophtalmo',
  kinesitherapie: 'Autres soins kiné',
  'soins-infirmiers': 'Autres soins infirmiers',
  'medecine-generale': 'Autres soins',
};

function buildScrollSection(specialty, currentFilename, title) {
  const allCards = CARDS[specialty];
  const otherCards = allCards.filter(c => c.href !== currentFilename);

  const cardsHtml = otherCards.map(c => `            <a href="${c.href}" class="motif-card flex-shrink-0" style="width: 260px; scroll-snap-align: start;">
                <img src="${c.img}" alt="${c.alt}" class="motif-card-img">
                <div class="motif-card-content">
                    <h3 class="font-bold text-lg mb-2" style="color: #252525;">${c.title}</h3>
                    <p class="text-gray-600 text-sm mb-4 flex-grow">${c.desc}</p>
                    <span class="inline-flex items-center gap-2 text-sm font-semibold" style="color: #00a7de;">En savoir plus <i class="fas fa-arrow-right"></i></span>
                </div>
            </a>`).join('\n');

  return `        <section class="mb-12">
            <h2 class="text-2xl font-bold mb-6" style="color: #252525;">${title}</h2>
            <div class="flex gap-5 overflow-x-auto pb-4" style="scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: thin; scrollbar-color: #00a7de #f3f4f6;">
${cardsHtml}
            </div>
        </section>`;
}

function processFile(filePath, specialty) {
  let content = fs.readFileSync(filePath, 'utf8');
  const filename = path.basename(filePath);

  // Skip if already has overflow-x-auto in "Autres" section
  if (/Autres[\s\S]{0,300}overflow-x-auto/.test(content)) {
    console.log(`  SKIP (already scroll): ${filename}`);
    return;
  }

  // Add motif-card CSS if missing
  if (!content.includes('motif-card')) {
    content = content.replace(
      /(<style[^>]*>)([\s\S]*?)<\/style>/,
      (match, open, body) => `${open}${body}${MOTIF_CARD_CSS}</style>`
    );
  }

  // Replace the "Autres" section (simple pill-link style)
  const sectionTitle = SECTION_TITLES[specialty];
  const newSection = buildScrollSection(specialty, filename, sectionTitle);

  // Match: <section class="mb-12"> ... <h2...>Autres...</h2> ... </section>
  const sectionRegex = /<section class="mb-12">\s*<h2[^>]*>Autres[\s\S]*?<\/section>/;
  if (sectionRegex.test(content)) {
    content = content.replace(sectionRegex, newSection);
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`  UPDATED: ${filename}`);
  } else {
    console.log(`  NOT FOUND: ${filename} - no matching section`);
  }
}

const BASE = path.join(__dirname, '..');

const PAGES = {
  ophtalmologie: [
    'pages/ophtalmologie/premiere-consultation.html',
    'pages/ophtalmologie/premiere-consultation-enfant.html',
    'pages/ophtalmologie/consultation-suivi.html',
    'pages/ophtalmologie/renouvellement-lunettes-lentilles.html',
    'pages/ophtalmologie/champ-visuel-humphrey.html',
    'pages/ophtalmologie/urgence.html',
  ],
  kinesitherapie: [
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
  ],
  'soins-infirmiers': [
    'pages/soins-infirmiers/injection.html',
  ],
  'medecine-generale': [
    'pages/medecine-generale/consultation.html',
    'pages/medecine-generale/urgence.html',
  ],
};

Object.entries(PAGES).forEach(([specialty, files]) => {
  console.log(`\n=== ${specialty} ===`);
  files.forEach(rel => {
    const full = path.join(BASE, rel);
    if (fs.existsSync(full)) {
      processFile(full, specialty);
    } else {
      console.log(`  MISSING: ${rel}`);
    }
  });
});

console.log('\nDone.');
