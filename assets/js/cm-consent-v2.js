/*!
 * Consent Mode V2 — Centre Médical Paris-Levallois
 * Conforme Google Consent Mode v2 + RGPD
 * @version 1.0
 */
(function() {
    var COOKIE_NAME = 'cm_consent_v2';
    var COOKIE_DAYS = 395; // 13 mois max Google

    // ── Utilitaires cookies ──
    function getCookie(name) {
        var m = document.cookie.match('(^|;)\\s*' + name + '=([^;]*)');
        return m ? decodeURIComponent(m[2]) : null;
    }
    function setCookie(name, val, days) {
        var d = new Date();
        d.setTime(d.getTime() + days * 864e5);
        document.cookie = name + '=' + encodeURIComponent(val) + ';expires=' + d.toUTCString() + ';path=/;SameSite=Lax;Secure';
    }

    // ── Lire consentement sauvegardé ──
    function getSaved() {
        var c = getCookie(COOKIE_NAME);
        if (!c) return null;
        try { return JSON.parse(c); } catch(e) { return null; }
    }

    // ── Appliquer le consentement via gtag ──
    function applyConsent(c) {
        gtag('consent', 'update', {
            'analytics_storage':        c.analytics ? 'granted' : 'denied',
            'ad_storage':               c.advertising ? 'granted' : 'denied',
            'ad_user_data':             c.advertising ? 'granted' : 'denied',
            'ad_personalization':       c.personalization ? 'granted' : 'denied',
            'personalization_storage':  c.personalization ? 'granted' : 'denied',
            'functionality_storage':    'granted',
            'security_storage':         'granted'
        });
    }

    // ── Sauvegarder et appliquer ──
    function saveAndApply(c) {
        c.timestamp = new Date().toISOString();
        c.version = '1.0';
        setCookie(COOKIE_NAME, JSON.stringify(c), COOKIE_DAYS);
        applyConsent(c);
        hideBanner();
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({ 'event': 'consent_update', 'consent_analytics': c.analytics, 'consent_advertising': c.advertising, 'consent_personalization': c.personalization });
    }

    // ── Créer la bannière ──
    function createBanner() {
        var el = document.getElementById('cm-consent-banner');
        if (el) el.remove();

        // Déterminer chemin vers politique-confidentialite
        var path = window.location.pathname;
        var prefix = '';
        if (path.match(/\/pages\/[^/]+\/[^/]+\//)) prefix = '../../../';
        else if (path.match(/\/pages\/[^/]+\//)) prefix = '../../';
        else if (path.match(/\/pages\//)) prefix = '../';

        var banner = document.createElement('div');
        banner.id = 'cm-consent-banner';
        banner.innerHTML =
            '<div class="cm-cb-container">' +
                '<div class="cm-cb-content">' +
                    '<div class="cm-cb-header">' +
                        '<h3>Gestion des cookies</h3>' +
                        '<p>Nous utilisons des cookies pour am\u00e9liorer votre exp\u00e9rience et mesurer l\u2019efficacit\u00e9 de nos services.</p>' +
                    '</div>' +
                    '<div class="cm-cb-options">' +
                        '<label class="cm-cb-opt"><input type="checkbox" checked disabled><span><strong>Cookies n\u00e9cessaires</strong> <em>Requis</em></span></label>' +
                        '<label class="cm-cb-opt"><input type="checkbox" id="cm-cb-analytics" checked><span><strong>Analytiques</strong> <em>Google Analytics</em></span></label>' +
                        '<label class="cm-cb-opt"><input type="checkbox" id="cm-cb-advertising" checked><span><strong>Publicitaires</strong> <em>Google Ads</em></span></label>' +
                        '<label class="cm-cb-opt"><input type="checkbox" id="cm-cb-personalization" checked><span><strong>Personnalisation</strong> <em>Contenu adapt\u00e9</em></span></label>' +
                    '</div>' +
                    '<div class="cm-cb-actions">' +
                        '<button id="cm-cb-accept" class="cm-cb-btn cm-cb-btn-primary">Tout accepter</button>' +
                        '<button id="cm-cb-save" class="cm-cb-btn cm-cb-btn-secondary">Enregistrer</button>' +
                        '<button id="cm-cb-reject" class="cm-cb-btn cm-cb-btn-minimal">Refuser les optionnels</button>' +
                    '</div>' +
                    '<a href="' + prefix + 'pages/politique-confidentialite.html" class="cm-cb-link" target="_blank">Politique de confidentialit\u00e9</a>' +
                '</div>' +
            '</div>';
        document.body.appendChild(banner);
        setTimeout(function() { banner.classList.add('cm-cb-visible'); }, 50);
    }

    function hideBanner() {
        var b = document.getElementById('cm-consent-banner');
        if (b) { b.classList.add('cm-cb-hiding'); setTimeout(function() { b.remove(); }, 300); }
    }

    // ── Event delegation pour les boutons ──
    document.addEventListener('click', function(e) {
        var id = e.target.id;
        if (id === 'cm-cb-accept') {
            saveAndApply({ necessary: true, analytics: true, advertising: true, personalization: true });
        } else if (id === 'cm-cb-save') {
            saveAndApply({
                necessary: true,
                analytics: !!document.getElementById('cm-cb-analytics').checked,
                advertising: !!document.getElementById('cm-cb-advertising').checked,
                personalization: !!document.getElementById('cm-cb-personalization').checked
            });
        } else if (id === 'cm-cb-reject') {
            saveAndApply({ necessary: true, analytics: false, advertising: false, personalization: false });
        }
    });

    // ── Init au DOM ready ──
    document.addEventListener('DOMContentLoaded', function() {
        var saved = getSaved();
        if (saved) {
            applyConsent(saved);
        } else {
            applyConsent({ analytics: true, advertising: true, personalization: true });
            createBanner();
        }
    });

    // ── API globale ──
    window.showCMConsentBanner = createBanner;
    window.showConsentManager = createBanner;
    window.resetCMConsent = function() {
        document.cookie = COOKIE_NAME + '=;expires=Thu,01 Jan 1970 00:00:01 GMT;path=/';
        applyConsent({ analytics: true, advertising: true, personalization: true });
        createBanner();
    };
})();
