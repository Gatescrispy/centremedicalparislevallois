const fs = require('fs');
const path = require('path');

const dirs = [
    'pages/kinesitherapie',
    'pages/ophtalmologie',
    'pages/medecine-generale',
    'pages/soins-infirmiers',
];

let fixed = 0;

dirs.forEach(dir => {
    const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));
    files.forEach(file => {
        const fp = path.join(dir, file);
        let content = fs.readFileSync(fp, 'utf8');
        const before = content;

        // 1. Retirer overflow-x: hidden du tag <main>
        content = content.replace(
            /(<main\b[^>]*?)\s*style="([^"]*?);\s*overflow-x:\s*hidden;?\s*"([^>]*>)/g,
            (match, tag, styleContent, rest) => {
                const cleaned = styleContent.replace(/;\s*overflow-x:\s*hidden/g, '').replace(/overflow-x:\s*hidden\s*;?/g, '').trim();
                if (cleaned) return `${tag} style="${cleaned}"${rest}`;
                return `${tag}${rest}`;
            }
        );
        // Cas où overflow-x: hidden est le seul style
        content = content.replace(
            /(<main\b[^>]*?)\s*style="overflow-x:\s*hidden;?\s*"([^>]*>)/g,
            '$1$2'
        );

        // 2. Ajouter html { overflow-x: hidden; } dans le <style id="cm-stable-layout">
        if (!content.includes('html{overflow-x:hidden') && !content.includes('html { overflow-x: hidden')) {
            content = content.replace(
                /(<style[^>]*id="cm-stable-layout"[^>]*>)/,
                '$1html{overflow-x:hidden;}'
            );
        }

        if (content !== before) {
            fs.writeFileSync(fp, content, 'utf8');
            console.log(`  FIXED: ${fp}`);
            fixed++;
        } else {
            console.log(`  SKIP: ${fp}`);
        }
    });
});

console.log(`\nDone: ${fixed} pages fixed.`);
