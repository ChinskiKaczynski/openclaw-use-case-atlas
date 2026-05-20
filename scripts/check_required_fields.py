#!/usr/bin/env python3
"""
Check that all use case card markdown files have required frontmatter fields.
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
USE_CASES_DIR = REPO_ROOT / "use-cases"

REQUIRED_FIELDS = [
    "## Status",
    "## One-liner",
    "## Best for",
    "## Workflow",
    "## MVP",
    "## Scores",
    "## Evidence Tier",
    "## Safety Level",
    "## Risks",
    "## Required safeguards",
    "## Source quality",
    "## Sources",
    "## Related use cases",
    "## MVP Path",
    "## Changelog",
]

errors = []
warnings = []

def check_file(filepath):
    content = filepath.read_text()
    missing = []

    for field in REQUIRED_FIELDS:
        if field not in content:
            missing.append(field)

    if missing:
        errors.append(f"{filepath.relative_to(REPO_ROOT)}: missing {len(missing)} required sections: {', '.join(missing)}")

    # Check for scores YAML block
    if "```yaml" not in content and "scores:" in content:
        warnings.append(f"{filepath.relative_to(REPO_ROOT)}: scores section may not have YAML block")

    # Check for evidence tier value
    evidence_match = re.search(r'Evidence Tier\s*\n\s*(E[0-5])', content)
    if not evidence_match and "## Evidence Tier" in content:
        warnings.append(f"{filepath.relative_to(REPO_ROOT)}: evidence tier value not found")

    # Check for safety level value
    safety_match = re.search(r'Safety Level\s*\n\s*(L[0-4])', content)
    if not safety_match and "## Safety Level" in content:
        warnings.append(f"{filepath.relative_to(REPO_ROOT)}: safety level value not found")

def main():
    print("=" * 60)
    print("Required Fields Check — OpenClaw Use Case Atlas")
    print("=" * 60)

    md_files = list(USE_CASES_DIR.rglob("*.md"))
    print(f"Checking {len(md_files)} use case card files...\n")

    for f in md_files:
        check_file(f)

    if warnings:
        print(f"⚠️  Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print(f"\n❌ Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        return 1
    else:
        print("✅ All use case cards have required fields!")
        if warnings:
            print(f"   ({len(warnings)} warning(s) — non-blocking)")
        return 0

if __name__ == "__main__":
    exit(main())
