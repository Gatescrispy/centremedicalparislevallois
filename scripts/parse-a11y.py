#!/usr/bin/env python3
import json
f = '/tmp/lighthouse-audit/Accueil.json'
with open(f) as fh:
    d = json.load(fh)
audits = d.get('audits', {})

# Contrast
c = audits.get('color-contrast', {})
print("=== CONTRASTE ===")
for item in c.get('details', {}).get('items', []):
    node = item.get('node', {})
    print(f"  {node.get('snippet', '?')[:100]}")
    print(f"    Selector: {node.get('selector', '?')}")

# Heading order
h = audits.get('heading-order', {})
print("\n=== HEADING ORDER ===")
for item in h.get('details', {}).get('items', []):
    print(f"  {item}")

# Button name
b = audits.get('button-name', {})
print("\n=== BUTTON NAME ===")
for item in b.get('details', {}).get('items', []):
    node = item.get('node', {})
    print(f"  {node.get('snippet', '?')[:120]}")

# Image aspect ratio
img = audits.get('image-aspect-ratio', {})
print("\n=== IMAGE ASPECT RATIO ===")
for item in img.get('details', {}).get('items', []):
    print(f"  {item.get('url', '?')[-60:]}")
    print(f"    displayed: {item.get('displayedAspectRatio','?')} vs actual: {item.get('actualAspectRatio','?')}")
