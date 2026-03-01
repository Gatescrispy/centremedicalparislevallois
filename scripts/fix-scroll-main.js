const fs = require('fs');
const path = require('path');

const dirs = [
    'pages/kinesitherapie',
    'pages/ophtalmologie',
    'pages/medecine-generale',
    'pages/soins-infirmiers',
];

let fixed = 0, skipped = 0;

dirs.forEach(dir => {
    const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));
    files.forEach(file => {
        const fp = path.join(dir, file);
        let content = fs.readFileSync(fp, 'utf8');

        // Already fixed
        if (content.includes('overflow-x: hidden') && content.includes('<main')) {
            skipped++;
            return;
        }

        // Add overflow-x: hidden to <main ...> tag
        const before = content;
        content = content.replace(
            /(<main\s[^>]*)(>)/,
            (match, tag, close) => {
                if (tag.includes('style=')) {
                    return tag.replace(/style="([^"]*)"/, 'style="$1; overflow-x: hidden;"') + close;
                }
                return tag + ' style="overflow-x: hidden;"' + close;
            }
        );

        if (content !== before) {
            fs.writeFileSync(fp, content, 'utf8');
            console.log(`  FIXED: ${fp}`);
            fixed++;
        } else {
            console.log(`  SKIP (no <main> found): ${fp}`);
            skipped++;
        }
    });
});

console.log(`\nDone: ${fixed} fixed, ${skipped} skipped.`);
