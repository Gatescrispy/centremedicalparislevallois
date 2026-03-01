const fs = require('fs');
const path = require('path');

// Configuration complète de TOUTES les pages d'examens
const allPages = [
  // ── KINÉSITHÉRAPIE ──────────────────────────────────────────────────────
  { path: 'kinesitherapie/premiere-consultation.html',         ctaTitle: "Prêt pour votre première séance ?",            ctaText: "Prenez rendez-vous avec notre kinésithérapeute", ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/consultation-suivi.html',            ctaTitle: "Continuez votre rééducation",                  ctaText: "Prenez rendez-vous pour votre séance de suivi",  ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/reeducation-post-operatoire.html',   ctaTitle: "Récemment opéré(e) ?",                         ctaText: "Démarrez votre rééducation post-opératoire",     ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/reeducation-membres-superieurs.html',ctaTitle: "Douleur à l'épaule, au coude ou à la main ?",  ctaText: "Prenez rendez-vous avec notre kinésithérapeute", ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/reeducation-membres-inferieurs.html',ctaTitle: "Douleur au genou, à la hanche ou à la cheville ?", ctaText: "Prenez rendez-vous avec notre kinésithérapeute", ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/rachis-cervical-dorsal-lombaire.html',ctaTitle: "Mal au dos ou au cou ?",                      ctaText: "Prenez rendez-vous avec notre kinésithérapeute", ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/traumatisme-adulte.html',            ctaTitle: "Blessé(e) suite à un accident ?",              ctaText: "Démarrez votre rééducation avec notre kinésithérapeute", ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/traumatisme-adolescent.html',        ctaTitle: "Votre ado est blessé ?",                       ctaText: "Prise en charge adaptée pour adolescents",       ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/scoliose-adolescent.html',           ctaTitle: "Votre adolescent a une scoliose ?",            ctaText: "Prenez rendez-vous avec notre kinésithérapeute", ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/drainage-lymphatique.html',          ctaTitle: "Besoin d'un drainage lymphatique ?",           ctaText: "Prenez rendez-vous avec notre kinésithérapeute", ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/femme-enceinte.html',                ctaTitle: "Enceinte ou jeune maman ?",                    ctaText: "Kiné prénatale et post-partum sur rendez-vous",  ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/electrotherapie.html',               ctaTitle: "Douleurs rebelles ou tendinites ?",            ctaText: "L'électrothérapie peut vous soulager rapidement", ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/renforcement-abdominal.html',        ctaTitle: "Renforcez votre sangle abdominale",            ctaText: "Programme personnalisé avec notre kinésithérapeute", ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/rhumatologie.html',                  ctaTitle: "Douleurs articulaires ou rhumatismes ?",       ctaText: "Prenez rendez-vous avec notre kinésithérapeute", ctaBtn: "Prendre RDV Kiné" },
  { path: 'kinesitherapie/seance-sans-ordonnance.html',        ctaTitle: "Besoin de kiné sans ordonnance ?",             ctaText: "Accès direct, jusqu'à 8 séances par an",        ctaBtn: "Prendre RDV Kiné" },

  // ── OPHTALMOLOGIE ────────────────────────────────────────────────────────
  { path: 'ophtalmologie/premiere-consultation.html',          ctaTitle: "Besoin d'un examen de vue ?",                  ctaText: "Prenez rendez-vous avec notre ophtalmologue",    ctaBtn: "Prendre RDV Ophtalmo" },
  { path: 'ophtalmologie/premiere-consultation-enfant.html',   ctaTitle: "Faites contrôler la vue de votre enfant",      ctaText: "Prenez rendez-vous avec notre ophtalmologue",    ctaBtn: "Prendre RDV Ophtalmo" },
  { path: 'ophtalmologie/consultation-suivi.html',             ctaTitle: "Suivi ophtalmologique à prévoir ?",            ctaText: "Prenez rendez-vous avec notre ophtalmologue",    ctaBtn: "Prendre RDV Ophtalmo" },
  { path: 'ophtalmologie/renouvellement-lunettes-lentilles.html', ctaTitle: "Renouveler vos lunettes ou lentilles ?",   ctaText: "Prenez rendez-vous avec notre ophtalmologue",    ctaBtn: "Prendre RDV Ophtalmo" },
  { path: 'ophtalmologie/champ-visuel-humphrey.html',          ctaTitle: "Champ visuel prescrit ?",                      ctaText: "Prenez rendez-vous pour réaliser votre examen",  ctaBtn: "Prendre RDV" },
  { path: 'ophtalmologie/urgence.html',                        ctaTitle: "Problème oculaire urgent ?",                   ctaText: "Consultez rapidement notre ophtalmologue",       ctaBtn: "Prendre RDV Urgent" },

  // ── MÉDECINE GÉNÉRALE ─────────────────────────────────────────────────────
  { path: 'medecine-generale/consultation.html',               ctaTitle: "Besoin d'une consultation médicale ?",         ctaText: "Prenez rendez-vous avec notre médecin généraliste", ctaBtn: "Prendre RDV Médecin" },
  { path: 'medecine-generale/urgence.html',                    ctaTitle: "Urgence médicale ?",                           ctaText: "Des créneaux urgents sont disponibles sur Doctolib", ctaBtn: "Prendre RDV Urgent" },

  // ── SOINS INFIRMIERS ──────────────────────────────────────────────────────
  { path: 'soins-infirmiers/vaccination-adulte.html',          ctaTitle: "Besoin d'une vaccination ?",                   ctaText: "Prenez rendez-vous avec notre équipe infirmière", ctaBtn: "Prendre RDV Vaccination" },
  { path: 'soins-infirmiers/vaccination-pediatrique.html',     ctaTitle: "Vacciner votre enfant ?",                      ctaText: "Calendrier vaccinal respecté par nos infirmiers",  ctaBtn: "Prendre RDV Vaccination" },
  { path: 'soins-infirmiers/bilan-sanguin-ecbu.html',          ctaTitle: "Besoin d'une prise de sang ?",                 ctaText: "Prenez rendez-vous avec notre équipe infirmière", ctaBtn: "Prendre RDV" },
  { path: 'soins-infirmiers/injection.html',                   ctaTitle: "Besoin d'une injection ?",                     ctaText: "Prenez rendez-vous avec notre équipe infirmière", ctaBtn: "Prendre RDV" },
  { path: 'soins-infirmiers/pansement-simple.html',            ctaTitle: "Besoin d'un pansement ?",                      ctaText: "Prenez rendez-vous avec notre équipe infirmière", ctaBtn: "Prendre RDV" },
  { path: 'soins-infirmiers/pansement-post-chirurgical.html',  ctaTitle: "Suivi post-opératoire ?",                      ctaText: "Nos infirmiers s'occupent de vos pansements complexes", ctaBtn: "Prendre RDV" },
  { path: 'soins-infirmiers/retrait-fils-agrafes.html',        ctaTitle: "Retrait de fils ou agrafes prévu ?",           ctaText: "Prenez rendez-vous avec notre équipe infirmière", ctaBtn: "Prendre RDV" },
  { path: 'soins-infirmiers/surveillance-constantes.html',     ctaTitle: "Suivi de vos constantes vitales ?",            ctaText: "Prenez rendez-vous avec notre équipe infirmière", ctaBtn: "Prendre RDV" },
  { path: 'soins-infirmiers/bilan-prevention.html',            ctaTitle: "Profitez de votre bilan prévention gratuit !", ctaText: "Disponible pour les 18-25, 45-50, 60-65 et 70-75 ans", ctaBtn: "Prendre RDV Bilan" },
  { path: 'soins-infirmiers/test-antigenique.html',            ctaTitle: "Besoin d'un test antigénique ?",               ctaText: "Prenez rendez-vous avec notre équipe infirmière", ctaBtn: "Prendre RDV Test" },
];

// Génère le nouveau CTA unifié
function generateCTA(config, doctolibUrl) {
  return `<section class="text-center rounded-2xl p-8 md:p-12" style="background-color: #00a7de;">
            <h2 class="text-2xl md:text-3xl font-bold mb-4 text-white">${config.ctaTitle}</h2>
            <p class="text-lg mb-6 text-white/90">${config.ctaText}</p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="${doctolibUrl}" 
                   target="_blank" rel="noopener"
                   class="inline-flex items-center justify-center gap-2 bg-white px-8 py-4 rounded-lg font-bold transition shadow-lg"
                   style="color: #00a7de; text-decoration: none;"
                   onmouseover="this.style.backgroundColor='#f3f4f6'" 
                   onmouseout="this.style.backgroundColor='white'">
                    <i class="fas fa-calendar-check"></i> ${config.ctaBtn}
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

// Patterns des CTA existants à remplacer (toutes variantes possibles)
const ctaPatterns = [
  // Style gradient coloré (rouge, orange, vert, violet, etc.)
  /<section class="text-center bg-gradient-to-r[^"]*rounded-2xl[^"]*"[^>]*>[\s\S]*?<\/section>/,
  // Style fond bleu unifié déjà existant (mis par les scripts précédents)
  /<section class="text-center rounded-2xl[^"]*"[^>]*>[\s\S]*?<\/section>/,
  // Style avec style inline bg
  /<section[^>]*style="background-color: #00a7de;"[^>]*class="text-center[^"]*"[^>]*>[\s\S]*?<\/section>/,
];

function processFile(filePath, config) {
  let content = fs.readFileSync(filePath, 'utf8');

  // Extraire l'URL Doctolib (prend la première occurrence dans le hero)
  const doctolibMatch = content.match(/href="(https:\/\/www\.doctolib\.fr\/[^"]+availabilities[^"]+)"/);
  if (!doctolibMatch) {
    console.warn(`  ⚠️  Aucune URL Doctolib trouvée`);
    return false;
  }
  const doctolibUrl = doctolibMatch[1];

  // Trouver et remplacer le CTA (dernier <section> avant </main>)
  // On cherche la section CTA finale - généralement la dernière section dans <main>
  let replaced = false;

  for (const pattern of ctaPatterns) {
    // On veut uniquement le dernier match (le CTA final, pas les autres sections)
    const matches = [...content.matchAll(new RegExp(pattern.source, 'g'))];
    if (matches.length > 0) {
      const lastMatch = matches[matches.length - 1];
      const matchedStr = lastMatch[0];

      // Vérification : doit contenir un lien Doctolib ou un h2 qui ressemble à un CTA
      if (matchedStr.includes('doctolib') || matchedStr.includes('fa-calendar') || matchedStr.includes('fa-phone')) {
        const newCTA = generateCTA(config, doctolibUrl);
        // Remplacer uniquement la dernière occurrence
        const lastIndex = content.lastIndexOf(matchedStr);
        content = content.substring(0, lastIndex) + newCTA + content.substring(lastIndex + matchedStr.length);
        replaced = true;
        break;
      }
    }
  }

  if (replaced) {
    fs.writeFileSync(filePath, content, 'utf8');
    return true;
  }
  return false;
}

// Main
const basePath = path.join(__dirname, '..', 'pages');
let updated = 0;
let skipped = 0;

for (const page of allPages) {
  const filePath = path.join(basePath, page.path);
  if (!fs.existsSync(filePath)) {
    console.warn(`⚠️  Fichier introuvable : ${page.path}`);
    skipped++;
    continue;
  }

  try {
    const ok = processFile(filePath, page);
    if (ok) {
      console.log(`✅ ${page.path}`);
      updated++;
    } else {
      console.log(`⏭️  Ignoré (pattern non trouvé) : ${page.path}`);
      skipped++;
    }
  } catch (err) {
    console.error(`❌ Erreur sur ${page.path} : ${err.message}`);
  }
}

console.log(`\n🎉 Terminé ! ${updated} pages mises à jour, ${skipped} ignorées.`);
