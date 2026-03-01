const fs = require('fs');
const path = require('path');

// Configuration des pages à mettre à jour avec leurs images et infos
const pagesConfig = {
  kinesitherapie: [
    { file: 'reeducation-membres-superieurs.html', title: 'Membres Supérieurs', subtitle: 'Épaule • Coude • Poignet • Main', image: '/Physiothérapie membres supérieurs.jpg', icon: 'fa-hand', duration: '30-45 min', description: 'Rééducation des membres supérieurs : épaule, coude, poignet, main. Tendinites, capsulites, fractures.', ctaTitle: 'Besoin de kinésithérapie ?', ctaText: 'Prenez rendez-vous en ligne avec notre kinésithérapeute', ctaBtn: 'Prendre RDV Kiné' },
    { file: 'reeducation-membres-inferieurs.html', title: 'Membres Inférieurs', subtitle: 'Hanche • Genou • Cheville • Pied', image: '/Réhabilitation membre inférieur.jpg', icon: 'fa-shoe-prints', duration: '30-45 min', description: 'Rééducation des membres inférieurs : hanche, genou, cheville, pied. Prothèses, ligaments.', ctaTitle: 'Besoin de kinésithérapie ?', ctaText: 'Prenez rendez-vous en ligne avec notre kinésithérapeute', ctaBtn: 'Prendre RDV Kiné' },
    { file: 'rachis-cervical-dorsal-lombaire.html', title: 'Rachis (Colonne vertébrale)', subtitle: 'Cervical • Dorsal • Lombaire', image: '/Physiothérapie de la colonne vertébrale.webp', icon: 'fa-spine', duration: '30-45 min', description: 'Rééducation du rachis cervical, dorsal et lombaire. Hernies discales, lombalgies, cervicalgies.', ctaTitle: 'Besoin de kinésithérapie ?', ctaText: 'Prenez rendez-vous en ligne avec notre kinésithérapeute', ctaBtn: 'Prendre RDV Kiné' },
    { file: 'traumatisme-adulte.html', title: 'Traumatisme Adulte', subtitle: 'Fractures • Entorses • Luxations', image: '/Physiothérapie Trauma Adulte.jpg.webp', icon: 'fa-bone', duration: '30-45 min', description: 'Rééducation après traumatisme : fractures, entorses, luxations. Reprise progressive de la mobilité.', ctaTitle: 'Besoin de kinésithérapie ?', ctaText: 'Prenez rendez-vous en ligne avec notre kinésithérapeute', ctaBtn: 'Prendre RDV Kiné' },
    { file: 'traumatisme-adolescent.html', title: 'Traumatisme Adolescent', subtitle: 'Fractures • Entorses • Sport', image: '/Santé Adolescent Injuries.jpg', icon: 'fa-child', duration: '30-45 min', description: 'Prise en charge adaptée aux adolescents : fractures, entorses sportives, croissance.', ctaTitle: 'Besoin de kinésithérapie ?', ctaText: 'Prenez rendez-vous en ligne avec notre kinésithérapeute', ctaBtn: 'Prendre RDV Kiné' },
    { file: 'scoliose-adolescent.html', title: 'Scoliose Adolescent', subtitle: 'Correction posturale • Renforcement', image: '/Scoliose adolescent physiothérapie.jpeg', icon: 'fa-user-injured', duration: '30-45 min', description: 'Rééducation de la scoliose chez l\'adolescent : correction posturale, renforcement musculaire.', ctaTitle: 'Besoin de kinésithérapie ?', ctaText: 'Prenez rendez-vous en ligne avec notre kinésithérapeute', ctaBtn: 'Prendre RDV Kiné' },
    { file: 'renforcement-abdominal.html', title: 'Renforcement Abdominal', subtitle: 'Gainage • Rééducation • Post-partum', image: '/Physiothérapie Renforcement Abdominal.jpeg', icon: 'fa-dumbbell', duration: '30-45 min', description: 'Renforcement de la sangle abdominale : gainage, rééducation post-partum, préparation sportive.', ctaTitle: 'Besoin de kinésithérapie ?', ctaText: 'Prenez rendez-vous en ligne avec notre kinésithérapeute', ctaBtn: 'Prendre RDV Kiné' },
    { file: 'rhumatologie.html', title: 'Rhumatologie', subtitle: 'Arthrose • Polyarthrite • Fibromyalgie', image: '/Rhumatisme articulaire.jpg', icon: 'fa-bone', duration: '30-45 min', description: 'Prise en charge des pathologies rhumatismales : arthrose, polyarthrite, fibromyalgie.', ctaTitle: 'Besoin de kinésithérapie ?', ctaText: 'Prenez rendez-vous en ligne avec notre kinésithérapeute', ctaBtn: 'Prendre RDV Kiné' },
    { file: 'seance-sans-ordonnance.html', title: 'Séance sans Ordonnance', subtitle: 'Accès direct • 8 séances max', image: '/Physiothérapie sans prescription.jpeg', icon: 'fa-door-open', duration: '30-45 min', description: 'Consultation kiné en accès direct sans ordonnance, jusqu\'à 8 séances par an.', ctaTitle: 'Besoin de kinésithérapie ?', ctaText: 'Prenez rendez-vous en ligne avec notre kinésithérapeute', ctaBtn: 'Prendre RDV Kiné' },
  ],
  ophtalmologie: [
    { file: 'premiere-consultation.html', title: 'Première Consultation', subtitle: 'Examen complet • Fond d\'œil • Dépistage', image: '/img-premiere-consultation.jpg', icon: 'fa-eye', duration: '30 min', description: 'Examen ophtalmologique complet : acuité visuelle, fond d\'œil, dépistage des pathologies oculaires.', ctaTitle: 'Besoin d\'un examen de vue ?', ctaText: 'Prenez rendez-vous avec notre ophtalmologue', ctaBtn: 'Prendre RDV Ophtalmo' },
    { file: 'premiere-consultation-enfant.html', title: 'Consultation Enfant', subtitle: 'Pédiatrie • Amblyopie • Strabisme', image: '/img-consultation-enfant.jpg', icon: 'fa-child', duration: '30 min', description: 'Examen ophtalmologique pédiatrique : dépistage amblyopie, strabisme, troubles de la vision chez l\'enfant.', ctaTitle: 'Votre enfant a besoin d\'un examen ?', ctaText: 'Prenez rendez-vous avec notre ophtalmologue', ctaBtn: 'Prendre RDV Ophtalmo' },
    { file: 'consultation-suivi.html', title: 'Consultation de Suivi', subtitle: 'Glaucome • DMLA • Diabète', image: '/img-consultation-suivi.jpg', icon: 'fa-eye', duration: '20 min', description: 'Suivi des pathologies oculaires : glaucome, DMLA, cataracte, rétinopathie diabétique.', ctaTitle: 'Besoin d\'un suivi ophtalmologique ?', ctaText: 'Prenez rendez-vous avec notre ophtalmologue', ctaBtn: 'Prendre RDV Ophtalmo' },
    { file: 'renouvellement-lunettes-lentilles.html', title: 'Renouvellement Lunettes/Lentilles', subtitle: 'Prescription • Verres • Lentilles', image: '/img-lunettes-lentilles.webp', icon: 'fa-glasses', duration: '15-20 min', description: 'Renouvellement de votre prescription de lunettes ou lentilles de contact.', ctaTitle: 'Besoin de renouveler vos lunettes ?', ctaText: 'Prenez rendez-vous avec notre ophtalmologue', ctaBtn: 'Prendre RDV Ophtalmo' },
    { file: 'champ-visuel-humphrey.html', title: 'Champ Visuel', subtitle: 'Humphrey • Glaucome • Dépistage', image: '/img-champ-visuel.jpg', icon: 'fa-bullseye', duration: '20-30 min', description: 'Examen du champ visuel Humphrey pour le dépistage et le suivi du glaucome.', ctaTitle: 'Besoin d\'un champ visuel ?', ctaText: 'Prenez rendez-vous avec notre ophtalmologue', ctaBtn: 'Prendre RDV Ophtalmo' },
    { file: 'urgence.html', title: 'Urgence Ophtalmologique', subtitle: 'Corps étranger • Baisse de vision', image: '/img-urgence-ophtalmo.webp', icon: 'fa-exclamation-triangle', duration: '15-30 min', description: 'Prise en charge urgente : corps étranger, baisse brutale de vision, œil rouge douloureux.', ctaTitle: 'Urgence ophtalmologique ?', ctaText: 'Consultez rapidement notre ophtalmologue', ctaBtn: 'Prendre RDV Urgent' },
  ],
  'medecine-generale': [
    { file: 'consultation.html', title: 'Consultation Médecine Générale', subtitle: 'Tous âges • Suivi • Médecin traitant', image: '/angle-eleve-de-femme-medecin-ecrit-une-ordonnance-au-bureau.jpg', icon: 'fa-stethoscope', duration: '15-20 min', description: 'Consultation médicale tous âges, suivi de pathologies chroniques, renouvellement d\'ordonnances.', ctaTitle: 'Besoin d\'une consultation ?', ctaText: 'Prenez rendez-vous avec notre médecin généraliste', ctaBtn: 'Prendre RDV Médecin' },
    { file: 'urgence.html', title: 'Urgence Médicale', subtitle: 'Consultation rapide • Semi-urgence', image: '/angle-eleve-de-femme-medecin-ecrit-une-ordonnance-au-bureau.jpg', icon: 'fa-bolt', duration: '15-20 min', description: 'Consultation rapide pour urgences médicales non vitales. Pour urgences vitales, appelez le 15.', ctaTitle: 'Urgence médicale ?', ctaText: 'Consultez rapidement notre médecin généraliste', ctaBtn: 'Prendre RDV Urgent' },
  ],
  'soins-infirmiers': [
    { file: 'vaccination-pediatrique.html', title: 'Vaccination Pédiatrique', subtitle: 'Nourrissons • Enfants • Obligatoires', image: '/Vaccination pédiatrique.jpeg', icon: 'fa-baby', duration: '15-20 min', description: 'Vaccinations obligatoires et recommandées pour nourrissons et enfants selon le calendrier vaccinal.', ctaTitle: 'Besoin d\'une vaccination ?', ctaText: 'Prenez rendez-vous avec notre équipe infirmière', ctaBtn: 'Prendre RDV Vaccination' },
    { file: 'bilan-sanguin-ecbu.html', title: 'Bilan Sanguin / ECBU', subtitle: 'Prise de sang • Analyses • Ordonnance', image: '/Test de Sang.webp', icon: 'fa-vial', duration: '10-15 min', description: 'Prises de sang sur ordonnance, analyses urinaires (ECBU). Résultats envoyés au laboratoire.', ctaTitle: 'Besoin d\'une prise de sang ?', ctaText: 'Prenez rendez-vous avec notre équipe infirmière', ctaBtn: 'Prendre RDV' },
    { file: 'injection.html', title: 'Injection', subtitle: 'IM • SC • IV • Sur ordonnance', image: '/Préparation d\'injection.jpg', icon: 'fa-syringe', duration: '10 min', description: 'Injections intramusculaires, sous-cutanées ou intraveineuses sur ordonnance médicale.', ctaTitle: 'Besoin d\'une injection ?', ctaText: 'Prenez rendez-vous avec notre équipe infirmière', ctaBtn: 'Prendre RDV' },
    { file: 'pansement-simple.html', title: 'Pansement Simple', subtitle: 'Plaies • Cicatrisation • Soins', image: '/Cutiplast Steril Island Dressing.jpg', icon: 'fa-bandage', duration: '15 min', description: 'Soins de plaies simples, changement de pansement, suivi de cicatrisation.', ctaTitle: 'Besoin d\'un pansement ?', ctaText: 'Prenez rendez-vous avec notre équipe infirmière', ctaBtn: 'Prendre RDV' },
    { file: 'pansement-post-chirurgical.html', title: 'Pansement Post-chirurgical', subtitle: 'Complexe • Opération • Suivi', image: '/Types de pansements post-chirurgicaux.jpg', icon: 'fa-hospital', duration: '20-30 min', description: 'Pansements complexes après intervention chirurgicale, suivi de cicatrisation post-opératoire.', ctaTitle: 'Besoin d\'un pansement post-op ?', ctaText: 'Prenez rendez-vous avec notre équipe infirmière', ctaBtn: 'Prendre RDV' },
    { file: 'retrait-fils-agrafes.html', title: 'Retrait Fils ou Agrafes', subtitle: 'Ablation • Points de suture', image: '/Retrait de points de suture abdomen.webp', icon: 'fa-scissors', duration: '15 min', description: 'Ablation des points de suture ou agrafes chirurgicales après cicatrisation complète.', ctaTitle: 'Besoin de retirer vos fils ?', ctaText: 'Prenez rendez-vous avec notre équipe infirmière', ctaBtn: 'Prendre RDV' },
    { file: 'surveillance-constantes.html', title: 'Surveillance Constantes', subtitle: 'Tension • Glycémie • Saturation', image: '/Nursing Constant Monitoring.webp', icon: 'fa-heartbeat', duration: '10 min', description: 'Surveillance des constantes vitales : tension artérielle, glycémie, saturation en oxygène.', ctaTitle: 'Besoin d\'un contrôle ?', ctaText: 'Prenez rendez-vous avec notre équipe infirmière', ctaBtn: 'Prendre RDV' },
    { file: 'bilan-prevention.html', title: 'Mon Bilan Prévention', subtitle: '18-75 ans • Assurance Maladie • Gratuit', image: '/Senior health checkup.jpeg', icon: 'fa-clipboard-check', duration: '30-45 min', description: 'Bilan de prévention gratuit proposé par l\'Assurance Maladie pour les 18-25, 45-50, 60-65 et 70-75 ans.', ctaTitle: 'Éligible au bilan prévention ?', ctaText: 'Prenez rendez-vous avec notre équipe infirmière', ctaBtn: 'Prendre RDV Bilan' },
    { file: 'test-antigenique.html', title: 'Test Antigénique', subtitle: 'COVID-19 • Résultat rapide', image: '/covid-test.jpg', icon: 'fa-vial-virus', duration: '15 min', description: 'Test antigénique COVID-19 avec résultat en 15 minutes. Sans rendez-vous selon disponibilité.', ctaTitle: 'Besoin d\'un test COVID ?', ctaText: 'Prenez rendez-vous avec notre équipe infirmière', ctaBtn: 'Prendre RDV Test' },
  ]
};

// Template pour le hero section
function generateHeroSection(config) {
  return `<section class="py-12 md:py-16" style="background-color: #00a7de;">
        <div class="max-w-6xl mx-auto px-4">
            <div class="grid md:grid-cols-2 gap-8 items-center">
                <div class="text-white">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="w-14 h-14 rounded-full bg-white/20 flex items-center justify-center">
                            <i class="fas ${config.icon} text-2xl"></i>
                        </div>
                        <div>
                            <h1 class="text-3xl md:text-4xl font-bold">${config.title}</h1>
                            <p class="text-white/80">${config.subtitle}</p>
                        </div>
                    </div>
                    <p class="text-lg opacity-90 mb-6">
                        ${config.description}
                    </p>
                    <div class="flex flex-wrap gap-3 mb-6">
                        <span class="bg-white/20 px-4 py-2 rounded-full text-sm"><i class="fas fa-clock mr-2"></i>${config.duration}</span>
                        <span class="bg-white/20 px-4 py-2 rounded-full text-sm"><i class="fas fa-check mr-2"></i>Secteur 1</span>
                        <span class="bg-white/20 px-4 py-2 rounded-full text-sm"><i class="fas fa-file-prescription mr-2"></i>Ordonnance</span>
                    </div>
                    <div class="flex flex-col sm:flex-row gap-3">
                        <a href="{{DOCTOLIB_URL}}" 
                           target="_blank" rel="noopener"
                           class="inline-flex items-center justify-center gap-2 bg-white px-6 py-3 rounded-lg font-bold transition"
                           style="color: #00a7de; text-decoration: none;"
                           onmouseover="this.style.backgroundColor='#f3f4f6'" 
                           onmouseout="this.style.backgroundColor='white'">
                            <i class="fas fa-calendar-check"></i> Prendre RDV
                        </a>
                        <a href="tel:+33180883716" 
                           class="inline-flex items-center justify-center gap-2 border-2 border-white px-6 py-3 rounded-lg font-bold transition text-white"
                           style="text-decoration: none;"
                           onmouseover="this.style.backgroundColor='rgba(255,255,255,0.1)'" 
                           onmouseout="this.style.backgroundColor='transparent'">
                            <i class="fas fa-phone"></i> 01 80 88 37 16
                        </a>
                    </div>
                </div>
                <div class="order-first md:order-last">
                    <img src="${config.image}" alt="${config.title}" class="rounded-2xl shadow-2xl w-full object-cover" style="max-height: 350px;">
                </div>
            </div>
        </div>
    </section>`;
}

// Template pour le CTA section
function generateCTASection(config) {
  return `<section class="text-center rounded-2xl p-8 md:p-12" style="background-color: #00a7de;">
            <h2 class="text-2xl md:text-3xl font-bold mb-4 text-white">Besoin de kinésithérapie ?</h2>
            <p class="text-lg mb-6 text-white/90">Prenez rendez-vous en ligne avec notre kinésithérapeute</p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="{{DOCTOLIB_URL}}" 
                   target="_blank" rel="noopener"
                   class="inline-flex items-center justify-center gap-2 bg-white px-8 py-4 rounded-lg font-bold transition shadow-lg"
                   style="color: #00a7de; text-decoration: none;"
                   onmouseover="this.style.backgroundColor='#f3f4f6'" 
                   onmouseout="this.style.backgroundColor='white'">
                    <i class="fas fa-calendar-check"></i> Prendre RDV Kiné
                </a>
                <a href="tel:+33180883716" 
                   class="inline-flex items-center justify-center gap-2 border-2 border-white px-8 py-4 rounded-lg font-bold transition text-white"
                   style="text-decoration: none;"
                   onmouseover="this.style.backgroundColor='rgba(255,255,255,0.1)'" 
                   onmouseout="this.style.backgroundColor='transparent'">
                    <i class="fas fa-phone"></i> 01 80 88 37 16
                </a>
            </div>
        </section>`;
}

function updateFile(filePath, config) {
  let content = fs.readFileSync(filePath, 'utf8');
  
  // Extraire l'URL Doctolib existante
  const doctolibMatch = content.match(/href="(https:\/\/www\.doctolib\.fr\/[^"]+availabilities[^"]+)"/);
  const doctolibUrl = doctolibMatch ? doctolibMatch[1] : 'https://www.doctolib.fr/centre-de-sante/levallois-perret/centre-medical-paris-levallois/booking/motives?specialityId=9&telehealth=false&placeId=practice-714912&source=deep_link';
  
  // Supprimer le style motif-hero du head
  content = content.replace(/\.motif-hero\{background:linear-gradient\([^}]+\}\s*/g, '');
  
  // Mettre à jour la couleur du breadcrumb
  content = content.replace(/text-\[#[A-Fa-f0-9]+\] font-medium/g, 'text-[#00a7de] font-medium');
  
  // Remplacer le hero section (pattern générique)
  const heroPattern = /<section class="(?:motif-hero|py-12)[^"]*"[^>]*>[\s\S]*?<\/section>\s*(?:<section class="bg-white border-b shadow-sm sticky[^>]*>[\s\S]*?<\/section>)?/;
  const newHero = generateHeroSection(config).replace(/\{\{DOCTOLIB_URL\}\}/g, doctolibUrl);
  
  if (heroPattern.test(content)) {
    content = content.replace(heroPattern, newHero);
  }
  
  // Remplacer le CTA section (pattern générique)
  const ctaPattern = /<section class="text-center (?:bg-gradient-to-r[^"]+|rounded-2xl)[^"]*"[^>]*>[\s\S]*?<h2[^>]*>(?:Besoin|Douleurs|Enceinte|Problèmes)[^<]*<\/h2>[\s\S]*?<\/section>/;
  const newCTA = generateCTASection(config).replace(/\{\{DOCTOLIB_URL\}\}/g, doctolibUrl);
  
  if (ctaPattern.test(content)) {
    content = content.replace(ctaPattern, newCTA);
  }
  
  // Uniformiser les couleurs des icônes
  content = content.replace(/text-(?:amber|purple|teal|red|orange|green|pink|yellow|indigo|blue)-\d{3}/g, 'text-[#00a7de]');
  
  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`✅ Updated: ${path.basename(filePath)}`);
}

// Main
const basePath = path.join(__dirname, '..', 'pages');

Object.entries(pagesConfig).forEach(([specialty, pages]) => {
  pages.forEach(pageConfig => {
    const filePath = path.join(basePath, specialty, pageConfig.file);
    if (fs.existsSync(filePath)) {
      try {
        updateFile(filePath, pageConfig);
      } catch (err) {
        console.error(`❌ Error updating ${pageConfig.file}:`, err.message);
      }
    } else {
      console.warn(`⚠️ File not found: ${filePath}`);
    }
  });
});

console.log('\n🎉 Style update complete!');
