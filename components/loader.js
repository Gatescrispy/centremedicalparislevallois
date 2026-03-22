// Loader dynamique header/footer — Centre Médical Paris-Levallois
async function loadComponent(id, path) {
    try {
        const r = await fetch(path);
        if (!r.ok) throw new Error('HTTP ' + r.status);
        document.getElementById(id).innerHTML = await r.text();
    } catch (e) { console.error('Erreur chargement composant:', e); }
}

document.addEventListener('DOMContentLoaded', async function() {
    // Détecter la profondeur relative pour trouver les composants
    var scripts = document.getElementsByTagName('script');
    var basePath = '';
    for (var i = 0; i < scripts.length; i++) {
        var src = scripts[i].getAttribute('src') || '';
        if (src.indexOf('loader.js') !== -1) {
            basePath = src.replace('loader.js', '');
            break;
        }
    }
    var v = '?v=' + Date.now();
    await loadComponent('header-placeholder', basePath + 'header.html' + v);
    await loadComponent('footer-placeholder', basePath + 'footer.html' + v);
    setTimeout(function() {
        var btn = document.getElementById('mobile-menu-button');
        var menu = document.getElementById('mobile-menu');
        if (btn && menu) btn.addEventListener('click', function() { menu.classList.toggle('hidden'); });
    }, 100);
});
