const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Trouver tous les fichiers HTML dans pages/
const basePath = path.join(__dirname, '..', 'pages');

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

function fixBreadcrumb(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');
  let modified = false;
  
  // Pattern 1: ol sans style inline (le plus courant dans les sous-pages)
  // <ol class="flex items-center space-x-2 text-sm flex-wrap">
  const pattern1 = /<ol class="flex items-center space-x-2 text-sm flex-wrap">/g;
  if (pattern1.test(content)) {
    content = content.replace(pattern1, '<ol class="flex items-center space-x-2 text-sm flex-wrap" style="list-style: none; margin: 0; padding: 0;">');
    modified = true;
  }
  
  // Pattern 2: ol avec gap au lieu de space-x (pages spécialités)
  // <ol class="flex items-center gap-2 text-sm" style="list-style: none; margin: 0; padding: 0;">
  // Déjà correct, ne pas modifier
  
  // Pattern 3: ol class qui n'a pas encore le style
  const pattern3 = /<ol class="([^"]*)"(?!\s*style)/g;
  if (pattern3.test(content) && !content.includes('style="list-style: none;')) {
    content = content.replace(pattern3, '<ol class="$1" style="list-style: none; margin: 0; padding: 0;">');
    modified = true;
  }
  
  // Éviter les doublons de style
  content = content.replace(/style="list-style: none; margin: 0; padding: 0;"\s*style="list-style: none; margin: 0; padding: 0;"/g, 
    'style="list-style: none; margin: 0; padding: 0;"');
  
  if (modified) {
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`✅ Fixed: ${path.relative(basePath, filePath)}`);
    return true;
  }
  
  return false;
}

// Main
const htmlFiles = findHtmlFiles(basePath);
let fixedCount = 0;

for (const file of htmlFiles) {
  try {
    if (fixBreadcrumb(file)) {
      fixedCount++;
    }
  } catch (err) {
    console.error(`❌ Error: ${path.basename(file)} - ${err.message}`);
  }
}

console.log(`\n🎉 Breadcrumb fix complete! ${fixedCount} files updated.`);
