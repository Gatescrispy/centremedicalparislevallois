#!/usr/bin/env python3
"""
SEA Batch Fix: Integrate Consent Mode V2 + Ads Tracking on all pages.
- P1: Add consent mode defaults (inline) BEFORE GTM + consent banner JS/CSS
- P2: Add cm-ads-tracking.js (conversion functions + auto-listeners)
- P4: Dual tracking structure (already in cm-ads-tracking.js)
- Also removes old inline gtagSendEvent functions from 3 pages
"""
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Consent Mode V2 inline block (MUST be before GTM) ──
CONSENT_INLINE = '''    <!-- Consent Mode V2 — defaults avant GTM -->
    <script>
    window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
    gtag('consent','default',{
        'analytics_storage':'granted','ad_storage':'granted',
        'ad_user_data':'granted','ad_personalization':'granted',
        'functionality_storage':'granted','security_storage':'granted',
        'wait_for_update':2000
    });
    </script>
'''


def get_asset_prefix(filepath):
    """Compute relative path from page to site root (where assets/ lives)."""
    rel = os.path.relpath(filepath, ROOT)
    depth = rel.count(os.sep)
    if depth == 0:
        return ''
    return '../' * depth


def add_consent_defaults(content, filepath):
    """Insert consent mode inline block BEFORE GTM snippet."""
    if "gtag('consent','default'" in content or "gtag('consent', 'default'" in content:
        return content, False  # Already has consent defaults

    # Find GTM snippet and insert before it
    # Pattern: <!-- Google Tag Manager --> or the GTM script directly
    gtm_markers = [
        '<!-- Google Tag Manager -->',
        "(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start'"
    ]
    
    for marker in gtm_markers:
        idx = content.find(marker)
        if idx != -1:
            # Find the start of the line containing the marker
            line_start = content.rfind('\n', 0, idx)
            if line_start == -1:
                line_start = 0
            else:
                line_start += 1
            content = content[:line_start] + CONSENT_INLINE + content[line_start:]
            return content, True
    
    return content, False


def add_consent_banner_assets(content, prefix):
    """Add consent banner CSS and JS references."""
    if 'cm-consent-banner.css' in content:
        return content, False

    css_tag = f'    <link rel="stylesheet" href="{prefix}assets/css/cm-consent-banner.css">\n'
    js_tag = f'    <script src="{prefix}assets/js/cm-consent-v2.js" defer></script>\n'

    # Insert before </head>
    if '</head>' in content:
        insert = css_tag + js_tag
        content = content.replace('</head>', insert + '</head>')
        return content, True
    return content, False


def add_ads_tracking(content, prefix):
    """Add cm-ads-tracking.js before </body>."""
    if 'cm-ads-tracking.js' in content:
        return content, False

    tag = f'    <script src="{prefix}assets/js/cm-ads-tracking.js"></script>\n'

    if '</body>' in content:
        content = content.replace('</body>', tag + '</body>')
        return content, True
    return content, False


def remove_old_inline_conversions(content, filepath):
    """Remove old inline gtagSendEvent functions from pages that had them."""
    changes = 0

    # Remove the inline conversion function definitions
    # Pattern: from "// Conversion Google Ads - RDV CDS" to the end of gtagSendEventTelephone
    pattern = r'\n\s*// Conversion Google Ads - RDV CDS \(Doctolib\)\s*\n\s*function gtagSendEventDoctolib\(\).*?return false;\s*\n\s*\}'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        changes += 1

    # Remove old inline Doctolib/Phone tracking listeners that are now handled by cm-ads-tracking.js
    # Pattern: "// Tracking conversions Google Ads" block or similar
    # Be careful to only remove the specific blocks

    # Pattern for index.html and le-centre.html style listeners
    patterns_to_remove = [
        # Block: "// Tracking conversions Google Ads" ... doctolibLinks + phoneLinks
        r'\n\s*// Tracking conversions Google Ads\s*\n\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*\n\s*// Conversion Doctolib.*?gtagSendEventTelephone\(this\.href\);\s*\n\s*\}\);\s*\n\s*\}\);\s*\n\s*\}\);',
        # Simpler block without outer DOMContentLoaded
        r'\n\s*// Tracking conversions Google Ads\s*\n\s*// Conversion Doctolib.*?gtagSendEventTelephone\(this\.href\);\s*\n\s*\}\);\s*\n\s*\}\);',
    ]

    for pat in patterns_to_remove:
        if re.search(pat, content, re.DOTALL):
            content = re.sub(pat, '', content, flags=re.DOTALL)
            changes += 1
            break

    return content, changes


def main():
    print("=" * 60)
    print("  SEA BATCH FIX — P1 + P2 + P4")
    print("=" * 60)

    html_files = glob.glob(os.path.join(ROOT, '*.html'))
    html_files += glob.glob(os.path.join(ROOT, 'pages', '*.html'))
    html_files += glob.glob(os.path.join(ROOT, 'pages', '*', '*.html'))
    html_files = sorted(set(html_files))

    # Exclude test files
    html_files = [f for f in html_files if 'test_' not in os.path.basename(f)]

    stats = {'consent_defaults': 0, 'consent_assets': 0, 'ads_tracking': 0, 'old_removed': 0}

    for filepath in html_files:
        rel = os.path.relpath(filepath, ROOT)
        prefix = get_asset_prefix(filepath)
        changes = []

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # P1: Add consent mode defaults inline
        content, changed = add_consent_defaults(content, filepath)
        if changed:
            changes.append('consent-defaults')
            stats['consent_defaults'] += 1

        # P1: Add consent banner CSS + JS
        content, changed = add_consent_banner_assets(content, prefix)
        if changed:
            changes.append('consent-banner')
            stats['consent_assets'] += 1

        # P2+P4: Add ads tracking JS
        content, changed = add_ads_tracking(content, prefix)
        if changed:
            changes.append('ads-tracking')
            stats['ads_tracking'] += 1

        # Remove old inline conversion functions (from 3 pages)
        content, n = remove_old_inline_conversions(content, filepath)
        if n > 0:
            changes.append(f'removed-old({n})')
            stats['old_removed'] += n

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ {rel}: {', '.join(changes)}")
        else:
            print(f"  ⏭️  {rel}: already up to date")

    print(f"\n📊 Résultats:")
    print(f"  - Consent defaults ajoutés:  {stats['consent_defaults']}")
    print(f"  - Consent banner ajouté:     {stats['consent_assets']}")
    print(f"  - Ads tracking ajouté:       {stats['ads_tracking']}")
    print(f"  - Ancien code supprimé:      {stats['old_removed']} blocs")


if __name__ == "__main__":
    main()
