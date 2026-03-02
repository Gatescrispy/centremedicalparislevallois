#!/usr/bin/env python3
"""
Audit SEO complet du site Centre Médical Paris-Levallois.
Vérifie : meta tags, schema.org, hiérarchie Hn, images, liens, canonical, OG, robots/sitemap.
"""
import os
import re
import json
import glob
from html.parser import HTMLParser
from collections import defaultdict
from urllib.parse import urljoin

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = "https://www.centremedicalparislevallois.fr"

# ============================================================
# HTML Parser
# ============================================================
class SEOParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta_description = ""
        self.meta_keywords = ""
        self.meta_robots = ""
        self.canonical = ""
        self.og_title = ""
        self.og_description = ""
        self.og_url = ""
        self.og_type = ""
        self.og_image = ""
        self.og_site_name = ""
        self.headings = []  # [(level, text)]
        self.images = []    # [(src, alt)]
        self.links = []     # [(href, text)]
        self.schemas = []   # [json_str]
        self.has_viewport = False
        self.has_charset = False
        self.has_lang = False
        self.lang = ""
        self.has_gtm = False
        self.has_ga4 = False
        self.has_favicon = False
        self.has_tailwind = False
        self.has_fontawesome = False
        
        self._in_title = False
        self._in_heading = False
        self._heading_level = 0
        self._heading_text = ""
        self._in_a = False
        self._a_href = ""
        self._a_text = ""
        self._in_script = False
        self._script_type = ""
        self._script_text = ""
        self._current_tag = ""
    
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self._current_tag = tag
        
        if tag == "html":
            lang = attrs_dict.get("lang", "")
            if lang:
                self.has_lang = True
                self.lang = lang
        
        elif tag == "meta":
            name = attrs_dict.get("name", "").lower()
            prop = attrs_dict.get("property", "").lower()
            content = attrs_dict.get("content", "")
            charset = attrs_dict.get("charset", "")
            
            if charset:
                self.has_charset = True
            if name == "description":
                self.meta_description = content
            elif name == "keywords":
                self.meta_keywords = content
            elif name == "robots":
                self.meta_robots = content
            elif name == "viewport":
                self.has_viewport = True
            elif prop == "og:title":
                self.og_title = content
            elif prop == "og:description":
                self.og_description = content
            elif prop == "og:url":
                self.og_url = content
            elif prop == "og:type":
                self.og_type = content
            elif prop == "og:image":
                self.og_image = content
            elif prop == "og:site_name":
                self.og_site_name = content
        
        elif tag == "link":
            rel = attrs_dict.get("rel", "")
            href = attrs_dict.get("href", "")
            if rel == "canonical":
                self.canonical = href
            elif rel == "icon" or rel == "shortcut icon":
                self.has_favicon = True
            if "tailwind" in href.lower():
                self.has_tailwind = True
            if "font-awesome" in href.lower() or "fontawesome" in href.lower():
                self.has_fontawesome = True
        
        elif tag == "title":
            self._in_title = True
        
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._in_heading = True
            self._heading_level = int(tag[1])
            self._heading_text = ""
        
        elif tag == "img":
            src = attrs_dict.get("src", "")
            alt = attrs_dict.get("alt", "")
            self.images.append((src, alt))
        
        elif tag == "a":
            href = attrs_dict.get("href", "")
            self._in_a = True
            self._a_href = href
            self._a_text = ""
        
        elif tag == "script":
            self._in_script = True
            self._script_type = attrs_dict.get("type", "")
            self._script_text = ""
            src = attrs_dict.get("src", "")
            if "gtm.js" in src or "googletagmanager" in src:
                self.has_gtm = True
            if "gtag" in src and "G-" in src:
                self.has_ga4 = True
    
    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_heading:
            self._heading_text += data.strip()
        if self._in_a:
            self._a_text += data.strip()
        if self._in_script:
            self._script_text += data
            if "GTM-" in data:
                self.has_gtm = True
            if "G-XHP0ZF8ZSF" in data or "gtag(" in data:
                self.has_ga4 = True
    
    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            if self._in_heading:
                self.headings.append((self._heading_level, self._heading_text))
                self._in_heading = False
        elif tag == "a":
            if self._in_a:
                self.links.append((self._a_href, self._a_text))
                self._in_a = False
        elif tag == "script":
            if self._in_script and self._script_type == "application/ld+json":
                try:
                    schema = json.loads(self._script_text.strip())
                    self.schemas.append(schema)
                except json.JSONDecodeError:
                    self.schemas.append({"_error": "Invalid JSON-LD", "_raw": self._script_text[:200]})
            self._in_script = False


def audit_page(filepath):
    """Audit a single HTML page and return issues dict."""
    rel_path = os.path.relpath(filepath, ROOT)
    issues = {"critical": [], "warning": [], "info": []}
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parser = SEOParser()
    try:
        parser.feed(content)
    except Exception as e:
        issues["critical"].append(f"HTML parse error: {e}")
        return rel_path, parser, issues
    
    # === CRITICAL CHECKS ===
    
    # Title
    title = parser.title.strip()
    if not title:
        issues["critical"].append("❌ Pas de <title>")
    elif len(title) < 30:
        issues["warning"].append(f"⚠️ Title trop court ({len(title)} chars): \"{title}\"")
    elif len(title) > 65:
        issues["warning"].append(f"⚠️ Title trop long ({len(title)} chars, max ~60): \"{title[:65]}...\"")
    
    # Meta description
    if not parser.meta_description:
        issues["critical"].append("❌ Pas de meta description")
    elif len(parser.meta_description) < 70:
        issues["warning"].append(f"⚠️ Meta description trop courte ({len(parser.meta_description)} chars)")
    elif len(parser.meta_description) > 160:
        issues["warning"].append(f"⚠️ Meta description trop longue ({len(parser.meta_description)} chars, max ~155)")
    
    # Canonical
    if not parser.canonical:
        issues["critical"].append("❌ Pas de canonical URL")
    elif not parser.canonical.startswith("https://"):
        issues["warning"].append(f"⚠️ Canonical non-HTTPS: {parser.canonical}")
    
    # H1
    h1_list = [h for h in parser.headings if h[0] == 1]
    if len(h1_list) == 0:
        issues["critical"].append("❌ Pas de H1")
    elif len(h1_list) > 1:
        issues["warning"].append(f"⚠️ {len(h1_list)} H1 trouvés (idéalement 1 seul)")
    
    # Heading hierarchy
    prev_level = 0
    for level, text in parser.headings:
        if level > prev_level + 1 and prev_level > 0:
            issues["warning"].append(f"⚠️ Saut de niveau heading: H{prev_level} → H{level} (\"{text[:40]}\")")
            break
        prev_level = level
    
    # lang attribute
    if not parser.has_lang:
        issues["critical"].append("❌ Pas d'attribut lang sur <html>")
    elif parser.lang != "fr":
        issues["warning"].append(f"⚠️ lang=\"{parser.lang}\" (attendu: \"fr\")")
    
    # charset
    if not parser.has_charset:
        issues["warning"].append("⚠️ Pas de meta charset")
    
    # viewport
    if not parser.has_viewport:
        issues["critical"].append("❌ Pas de meta viewport (mobile)")
    
    # === OG TAGS ===
    if not parser.og_title:
        issues["warning"].append("⚠️ Pas de og:title")
    if not parser.og_description:
        issues["warning"].append("⚠️ Pas de og:description")
    if not parser.og_url:
        issues["warning"].append("⚠️ Pas de og:url")
    
    # === SCHEMA.ORG ===
    if not parser.schemas:
        issues["warning"].append("⚠️ Aucun schema.org (JSON-LD) trouvé")
    else:
        schema_types = []
        for s in parser.schemas:
            if "_error" in s:
                issues["critical"].append(f"❌ JSON-LD invalide: {s['_raw'][:100]}")
            else:
                t = s.get("@type", "unknown")
                schema_types.append(t)
        if schema_types:
            issues["info"].append(f"ℹ️ Schemas: {', '.join(schema_types)}")
        
        # Check for BreadcrumbList
        has_breadcrumb = any(s.get("@type") == "BreadcrumbList" for s in parser.schemas)
        if not has_breadcrumb and rel_path != "index.html":
            issues["warning"].append("⚠️ Pas de BreadcrumbList schema")
    
    # === IMAGES ===
    images_no_alt = [(src, alt) for src, alt in parser.images if not alt]
    if images_no_alt:
        for src, _ in images_no_alt[:3]:
            issues["warning"].append(f"⚠️ Image sans alt: {src[:60]}")
        if len(images_no_alt) > 3:
            issues["warning"].append(f"⚠️ ...et {len(images_no_alt)-3} autres images sans alt")
    
    # === TRACKING ===
    if not parser.has_gtm:
        issues["warning"].append("⚠️ GTM non détecté")
    if not parser.has_ga4:
        issues["warning"].append("⚠️ GA4 non détecté")
    
    # === FAVICON ===
    if not parser.has_favicon:
        issues["info"].append("ℹ️ Pas de favicon déclaré")
    
    # === TAILWIND / FONT AWESOME ===
    if not parser.has_tailwind:
        issues["info"].append("ℹ️ Tailwind CSS non détecté")
    if not parser.has_fontawesome:
        issues["info"].append("ℹ️ Font Awesome non détecté")
    
    # === BROKEN TAILWIND ARBITRARY CLASSES ===
    arbitrary_pattern = re.findall(r'class="[^"]*(?:text-white/\d|bg-\w+-\d+/\d|border-\w+-\d+/\d|backdrop-blur-\w+|bg-black/\d)[^"]*"', content)
    if arbitrary_pattern:
        issues["warning"].append(f"⚠️ {len(arbitrary_pattern)} classes Tailwind arbitraires potentiellement cassées")
    
    # === META KEYWORDS ===
    if not parser.meta_keywords:
        issues["info"].append("ℹ️ Pas de meta keywords")
    
    return rel_path, parser, issues


def audit_robots_txt():
    """Check robots.txt"""
    issues = []
    robots_path = os.path.join(ROOT, "robots.txt")
    if not os.path.exists(robots_path):
        issues.append("❌ robots.txt manquant")
        return issues
    
    with open(robots_path, 'r') as f:
        content = f.read()
    
    if "User-agent" not in content:
        issues.append("❌ robots.txt: pas de User-agent")
    if "Sitemap" not in content:
        issues.append("⚠️ robots.txt: pas de référence au sitemap")
    if "Disallow: /" in content and content.count("Disallow") == 1:
        issues.append("❌ robots.txt: bloque tout le site!")
    
    issues.append(f"ℹ️ robots.txt présent ({len(content)} chars)")
    return issues


def audit_sitemap():
    """Check sitemap.xml"""
    issues = []
    sitemap_path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        issues.append("❌ sitemap.xml manquant")
        return issues, []
    
    with open(sitemap_path, 'r') as f:
        content = f.read()
    
    urls_in_sitemap = re.findall(r'<loc>(.*?)</loc>', content)
    issues.append(f"ℹ️ sitemap.xml: {len(urls_in_sitemap)} URLs")
    
    if not urls_in_sitemap:
        issues.append("❌ sitemap.xml vide (aucune URL)")
    
    return issues, urls_in_sitemap


def check_sitemap_coverage(html_files, sitemap_urls):
    """Check if all HTML pages are in the sitemap."""
    issues = []
    missing = []
    
    for f in html_files:
        rel = os.path.relpath(f, ROOT)
        # Skip non-indexable pages
        if any(skip in rel for skip in ["landing/", "test_", "index-v1"]):
            continue
        
        expected_url = SITE_URL + "/" + rel.replace("\\", "/")
        if rel == "index.html":
            expected_url = SITE_URL + "/"
        
        found = False
        for sitemap_url in sitemap_urls:
            # Normalize comparison
            if rel.replace("\\", "/") in sitemap_url or expected_url == sitemap_url:
                found = True
                break
        
        if not found:
            missing.append(rel)
    
    if missing:
        issues.append(f"❌ {len(missing)} pages absentes du sitemap:")
        for m in sorted(missing):
            issues.append(f"   - {m}")
    else:
        issues.append("✅ Toutes les pages sont dans le sitemap")
    
    return issues


def check_duplicate_titles(all_results):
    """Find duplicate titles across pages."""
    titles = defaultdict(list)
    for rel_path, parser, _ in all_results:
        t = parser.title.strip()
        if t:
            titles[t].append(rel_path)
    
    issues = []
    for title, pages in titles.items():
        if len(pages) > 1:
            issues.append(f"❌ Title dupliqué \"{title[:50]}...\" sur: {', '.join(pages)}")
    return issues


def check_duplicate_descriptions(all_results):
    """Find duplicate meta descriptions."""
    descs = defaultdict(list)
    for rel_path, parser, _ in all_results:
        d = parser.meta_description.strip()
        if d:
            descs[d[:100]].append(rel_path)
    
    issues = []
    for desc, pages in descs.items():
        if len(pages) > 1:
            issues.append(f"❌ Description dupliquée \"{desc[:50]}...\" sur: {', '.join(pages)}")
    return issues


def check_canonical_consistency(all_results):
    """Check canonical URLs match expected patterns."""
    issues = []
    for rel_path, parser, _ in all_results:
        if parser.canonical:
            expected = SITE_URL + "/" + rel_path.replace("\\", "/")
            if rel_path == "index.html":
                expected = SITE_URL + "/"
            # Normalize
            canon = parser.canonical.rstrip("/")
            exp = expected.rstrip("/")
            if canon != exp and not (rel_path == "index.html" and canon == SITE_URL):
                issues.append(f"⚠️ Canonical mismatch sur {rel_path}: {parser.canonical} (attendu: {expected})")
    return issues


# ============================================================
# MAIN
# ============================================================
def main():
    print("=" * 70)
    print("  AUDIT SEO COMPLET — Centre Médical Paris-Levallois")
    print("=" * 70)
    
    # Collect all HTML files
    html_files = sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True))
    html_files = [f for f in html_files if
                  "node_modules" not in f and
                  ".git" not in f and
                  "components/" not in f.replace(ROOT, "") and
                  "test_" not in os.path.basename(f) and
                  "index-v1" not in os.path.basename(f)]
    
    print(f"\n📄 {len(html_files)} pages HTML à auditer\n")
    
    # Audit each page
    all_results = []
    total_critical = 0
    total_warning = 0
    total_info = 0
    
    for filepath in html_files:
        rel_path, parser, issues = audit_page(filepath)
        all_results.append((rel_path, parser, issues))
        
        nc = len(issues["critical"])
        nw = len(issues["warning"])
        ni = len(issues["info"])
        total_critical += nc
        total_warning += nw
        total_info += ni
    
    # === PAGE-BY-PAGE REPORT ===
    print("\n" + "=" * 70)
    print("  RÉSULTATS PAR PAGE")
    print("=" * 70)
    
    for rel_path, parser, issues in all_results:
        nc = len(issues["critical"])
        nw = len(issues["warning"])
        
        if nc == 0 and nw == 0:
            status = "✅"
        elif nc > 0:
            status = "🔴"
        else:
            status = "🟡"
        
        print(f"\n{status} {rel_path}")
        print(f"   Title: \"{parser.title.strip()[:60]}\"")
        
        for c in issues["critical"]:
            print(f"   {c}")
        for w in issues["warning"]:
            print(f"   {w}")
        for i in issues["info"]:
            print(f"   {i}")
    
    # === CROSS-PAGE CHECKS ===
    print("\n\n" + "=" * 70)
    print("  VÉRIFICATIONS CROSS-PAGES")
    print("=" * 70)
    
    # Duplicate titles
    print("\n--- Titles dupliqués ---")
    dup_titles = check_duplicate_titles(all_results)
    if dup_titles:
        for i in dup_titles:
            print(f"  {i}")
    else:
        print("  ✅ Aucun title dupliqué")
    
    # Duplicate descriptions
    print("\n--- Descriptions dupliquées ---")
    dup_descs = check_duplicate_descriptions(all_results)
    if dup_descs:
        for i in dup_descs:
            print(f"  {i}")
    else:
        print("  ✅ Aucune description dupliquée")
    
    # Canonical consistency
    print("\n--- Canonical URLs ---")
    canon_issues = check_canonical_consistency(all_results)
    if canon_issues:
        for i in canon_issues:
            print(f"  {i}")
    else:
        print("  ✅ Toutes les canonical URLs sont cohérentes")
    
    # === ROBOTS & SITEMAP ===
    print("\n\n" + "=" * 70)
    print("  ROBOTS.TXT & SITEMAP.XML")
    print("=" * 70)
    
    print("\n--- robots.txt ---")
    robots_issues = audit_robots_txt()
    for i in robots_issues:
        print(f"  {i}")
    
    print("\n--- sitemap.xml ---")
    sitemap_issues, sitemap_urls = audit_sitemap()
    for i in sitemap_issues:
        print(f"  {i}")
    
    print("\n--- Couverture sitemap ---")
    coverage = check_sitemap_coverage(html_files, sitemap_urls)
    for i in coverage:
        print(f"  {i}")
    
    # === SUMMARY ===
    print("\n\n" + "=" * 70)
    print("  RÉSUMÉ DE L'AUDIT")
    print("=" * 70)
    print(f"\n  📄 Pages auditées:     {len(html_files)}")
    print(f"  🔴 Problèmes critiques: {total_critical}")
    print(f"  🟡 Avertissements:      {total_warning}")
    print(f"  ℹ️  Informations:        {total_info}")
    
    # Pages with most issues
    pages_by_issues = sorted(all_results, key=lambda x: len(x[2]["critical"]) * 10 + len(x[2]["warning"]), reverse=True)
    print(f"\n  📋 Top 10 pages avec le plus de problèmes:")
    for rel_path, parser, issues in pages_by_issues[:10]:
        nc = len(issues["critical"])
        nw = len(issues["warning"])
        if nc + nw > 0:
            print(f"     {rel_path}: {nc} critiques, {nw} avertissements")
    
    print("\n" + "=" * 70)
    print("  FIN DE L'AUDIT")
    print("=" * 70)


if __name__ == "__main__":
    main()
