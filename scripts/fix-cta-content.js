const fs = require('fs');
const path = require('path');

// Configuration des CTA par spécialité
const ctaConfig = {
  'soins-infirmiers': {
    title: 'Besoin d\'un soin infirmier ?',
    text: 'Prenez rendez-vous avec notre équipe infirmière',
    btnText: 'Prendre RDV Infirmier'
  },
  'ophtalmologie': {
    title: 'Besoin d\'un examen de vue ?',
    text: 'Prenez rendez-vous avec notre ophtalmologue',
    btnText: 'Prendre RDV Ophtalmo'
  },
  'kinesitherapie': {
    title: 'Besoin de kinésithérapie ?',
    text: 'Prenez rendez-vous en ligne avec notre kinésithérapeute',
    btnText: 'Prendre RDV Kiné'
  },
  'medecine-generale': {
    title: 'Besoin d\'une consultation ?',
    text: 'Prenez rendez-vous avec notre médecin généraliste',
    btnText: 'Prendre RDV Médecin'
  }
};

// CTA personnalisés par page (surcharge)
const customCTA = {
  'vaccination-adulte.html': { title: 'Besoin d\'une vaccination ?', text: 'Prenez rendez-vous avec notre équipe d\'infirmiers', btnText: 'Prendre RDV Vaccination' },
  'vaccination-pediatrique.html': { title: 'Vaccination pour votre enfant ?', text: 'Prenez rendez-vous avec notre équipe d\'infirmiers', btnText: 'Prendre RDV Vaccination' },
  'bilan-sanguin-ecbu.html': { title: 'Besoin d\'une prise de sang ?', text: 'Prenez rendez-vous avec notre équipe infirmière', btnText: 'Prendre RDV' },
  'injection.html': { title: 'Besoin d\'une injection ?', text: 'Prenez rendez-vous avec notre équipe infirmière', btnText: 'Prendre RDV' },
  'pansement-simple.html': { title: 'Besoin d\'un pansement ?', text: 'Prenez rendez-vous avec notre équipe infirmière', btnText: 'Prendre RDV' },
  'pansement-post-chirurgical.html': { title: 'Pansement post-opératoire ?', text: 'Prenez rendez-vous avec notre équipe infirmière', btnText: 'Prendre RDV' },
  'retrait-fils-agrafes.html': { title: 'Retrait de fils ou agrafes ?', text: 'Prenez rendez-vous avec notre équipe infirmière', btnText: 'Prendre RDV' },
  'surveillance-constantes.html': { title: 'Surveillance de vos constantes ?', text: 'Prenez rendez-vous avec notre équipe infirmière', btnText: 'Prendre RDV' },
  'bilan-prevention.html': { title: 'Éligible au bilan prévention ?', text: 'Prenez rendez-vous pour votre bilan gratuit', btnText: 'Prendre RDV Bilan' },
  'test-antigenique.html': { title: 'Besoin d\'un test COVID ?', text: 'Prenez rendez-vous avec notre équipe infirmière', btnText: 'Prendre RDV Test' },
  
  'premiere-consultation.html': { title: 'Besoin d\'un examen de vue ?', text: 'Prenez rendez-vous avec notre ophtalmologue', btnText: 'Prendre RDV Ophtalmo' },
  'premiere-consultation-enfant.html': { title: 'Examen de vue pour votre enfant ?', text: 'Prenez rendez-vous avec notre ophtalmologue', btnText: 'Prendre RDV Ophtalmo' },
  'consultation-suivi.html': { title: 'Suivi ophtalmologique ?', text: 'Prenez rendez-vous avec notre ophtalmologue', btnText: 'Prendre RDV Ophtalmo' },
  'renouvellement-lunettes-lentilles.html': { title: 'Renouveler vos lunettes ?', text: 'Prenez rendez-vous avec notre ophtalmologue', btnText: 'Prendre RDV Ophtalmo' },
  'champ-visuel-humphrey.html': { title: 'Champ visuel prescrit ?', text: 'Prenez rendez-vous pour réaliser votre examen', btnText: 'Prendre RDV' },
  'urgence.html': { title: 'Urgence médicale ?', text: 'Consultez rapidement notre équipe médicale', btnText: 'Prendre RDV Urgent' },
  
  'consultation.html': { title: 'Besoin d\'une consultation ?', text: 'Prenez rendez-vous avec notre médecin généraliste', btnText: 'Prendre RDV Médecin' },
};

function generateCTASection(config, doctolibUrl) {
  return `<section class="text-center rounded-2xl p-8 md:p-12" style="background-color: #00a7de;">
            <h2 class="text-2xl md:text-3xl font-bold mb-4 text-white">${config.title}</h2>
            <p class="text-lg mb-6 text-white/90">${config.text}</p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="${doctolibUrl}" 
                   target="_blank" rel="noopener"
                   class="inline-flex items-center justify-center gap-2 bg-white px-8 py-4 rounded-lg font-bold transition shadow-lg"
                   style="color: #00a7de; text-decoration: none;"
                   onmouseover="this.style.backgroundColor='#f3f4f6'" 
                   onmouseout="this.style.backgroundColor='white'">
                    <i class="fas fa-calendar-check"></i> ${config.btnText}
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

function findHtmlFiles(dir) {
  let results = [];
  const items = fs.readdirSync(dir);
  
  for (const item of items) {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);
    
    if (stat.isDirectory()) {
      results = results.concat(findHtmlFiles(fullPath));
    } else if (item.endsWith('.html')) {
      results.push(fullPath);
    }
  }
  
  return results;
}

function fixCTA(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');
  const fileName = path.basename(filePath);
  const parentDir = path.basename(path.dirname(filePath));
  
  // Déterminer la config CTA à utiliser
  let ctaConf = customCTA[fileName] || ctaConfig[parentDir];
  
  if (!ctaConf) {
    return false; // Pas de config pour ce fichier
  }
  
  // Trouver l'URL Doctolib existante dans le hero
  const doctolibMatch = content.match(/href="(https:\/\/www\.doctolib\.fr\/[^"]+availabilities[^"]+)"/);
  const doctolibUrl = doctolibMatch ? doctolibMatch[1] : 'https://www.doctolib.fr/centre-de-sante/levallois-perret/centre-medical-paris-levallois';
  
  // Pattern pour trouver le CTA incorrect (celui généré par le script précédent)
  const badCTAPattern = /<section class="text-center rounded-2xl p-8 md:p-12" style="background-color: #00a7de;">[\s\S]*?<h2[^>]*>Besoin de kinésithérapie \?<\/h2>[\s\S]*?<\/section>/;
  
  if (badCTAPattern.test(content)) {
    const newCTA = generateCTASection(ctaConf, doctolibUrl);
    content = content.replace(badCTAPattern, newCTA);
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`✅ Fixed CTA: ${parentDir}/${fileName}`);
    return true;
  }
  
  return false;
}

// Main
const basePath = path.join(__dirname, '..', 'pages');
const htmlFiles = findHtmlFiles(basePath);
let fixedCount = 0;

for (const file of htmlFiles) {
  try {
    if (fixCTA(file)) {
      fixedCount++;
    }
  } catch (err) {
    console.error(`❌ Error: ${path.basename(file)} - ${err.message}`);
  }
}

console.log(`\n🎉 CTA fix complete! ${fixedCount} files updated.`);
