/*!
 * Google Ads Conversion Tracking — Centre Médical Paris-Levallois
 * Dual tracking: VT Imagerie (actuel) + futur compte dédié
 * Envoie aussi les événements via dataLayer.push pour GTM
 * @version 2.0
 */
(function() {
    // ── COMPTES GOOGLE ADS ──
    // Chaque entrée = un compte avec ses conversion labels
    var ADS_ACCOUNTS = [
        // VT Imagerie (actif — NE PAS SUPPRIMER tant que la migration n'est pas terminée)
        {
            id: 'AW-11456521545',
            conversions: {
                doctolib: 'AW-11456521545/ypsQCO_RwuEbEMnK8tYq',
                phone:    'AW-11456521545/xTpdCNWFw-EbEMnK8tYq'
            }
        }
        // ── FUTUR COMPTE DÉDIÉ ──
        // Décommenter quand le nouveau compte Google Ads est créé :
        // ,{
        //     id: 'AW-NEW_ACCOUNT_ID',
        //     conversions: {
        //         doctolib: 'AW-NEW_ACCOUNT_ID/NEW_DOCTOLIB_LABEL',
        //         phone:    'AW-NEW_ACCOUNT_ID/NEW_PHONE_LABEL'
        //     }
        // }
    ];

    // ── Fonctions de conversion globales ──
    window.gtagSendEventDoctolib = function() {
        // gtag direct (VT Imagerie — ancienne landing page)
        if (typeof gtag === 'function') {
            ADS_ACCOUNTS.forEach(function(account) {
                gtag('event', 'conversion', { 'send_to': account.conversions.doctolib });
            });
            gtag('event', 'clic_doctolib', {
                'event_category': 'conversion',
                'centre': 'Centre-Medical-Paris-Levallois'
            });
        }
        // dataLayer.push pour GTM (déclenche les tags GTM)
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
            'event': 'clic_doctolib',
            'event_category': 'conversion',
            'centre': 'Centre-Medical-Paris-Levallois'
        });
    };

    window.gtagSendEventTelephone = function(url) {
        // gtag direct (VT Imagerie — ancienne landing page)
        if (typeof gtag === 'function') {
            ADS_ACCOUNTS.forEach(function(account) {
                gtag('event', 'conversion', { 'send_to': account.conversions.phone });
            });
            gtag('event', 'clic_telephone', {
                'event_category': 'conversion',
                'centre': 'Centre-Medical-Paris-Levallois'
            });
        }
        // dataLayer.push pour GTM (déclenche les tags GTM)
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
            'event': 'clic_telephone',
            'event_category': 'conversion',
            'phone_number': url || '',
            'centre': 'Centre-Medical-Paris-Levallois'
        });
    };

    // ── Auto-attach via event delegation (fonctionne avec header/footer dynamiques) ──
    document.addEventListener('click', function(e) {
        var link = e.target.closest ? e.target.closest('a') : null;
        if (!link) return;

        var href = link.getAttribute('href') || '';

        // Clic Doctolib
        if (href.indexOf('doctolib.fr') !== -1) {
            window.gtagSendEventDoctolib();
        }

        // Clic téléphone
        if (href.indexOf('tel:') === 0) {
            window.gtagSendEventTelephone(href);
        }
    });
})();
