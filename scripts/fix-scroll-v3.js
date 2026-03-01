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

        // Remplacer class="flex gap-[n] overflow-x-auto pb-4"
        // par class="flex gap-[n] pb-4" + overflow-x:auto dans le style inline
        content = content.replace(
            /class="(flex gap-\d+ )overflow-x-auto( pb-\d+)"\s*style="([^"]*)"/g,
            'class="$1$2" style="overflow-x: auto; $3"'
        );

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
