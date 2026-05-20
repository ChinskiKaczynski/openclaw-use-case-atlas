#!/usr/bin/env python3
"""
Check for duplicate IDs, slugs, and file paths across the atlas.
"""

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
JSON_PATH = REPO_ROOT / "data" / "use_cases.json"
CSV_PATH = REPO_ROOT / "data" / "use_cases.csv"

errors = []

def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

def check_json_duplicates():
    with open(JSON_PATH) as f:
        data = json.load(f)

    ids = {}
    names = {}
    files = {}

    for uc in data["use_cases"]:
        # ID duplicates
        if uc["id"] in ids:
            errors.append(f"Duplicate ID '{uc['id']}': {ids[uc['id']]} and {uc['name']}")
        ids[uc["id"]] = uc["name"]

        # Name duplicates (case-insensitive)
        name_lower = uc["name"].lower()
        if name_lower in names:
            errors.append(f"Duplicate name '{uc['name']}': IDs {names[name_lower]} and {uc['id']}")
        names[name_lower] = uc["id"]

        # File path duplicates
        if uc.get("file") in files:
            errors.append(f"Duplicate file path '{uc['file']}': {files[uc['file']]} and {uc['name']}")
        files[uc["file"]] = uc["name"]

    print(f"Checked {len(data['use_cases'])} use cases")
    print(f"  Unique IDs: {len(ids)}")
    print(f"  Unique names: {len(names)}")
    print(f"  Unique files: {len(files)}")

def check_files_exist():
    """Check that all referenced use case card files exist."""
    with open(JSON_PATH) as f:
        data = json.load(f)

    missing = []
    for uc in data["use_cases"]:
        if uc.get("file"):
            path = REPO_ROOT / uc["file"]
            if not path.exists():
                missing.append(f"[{uc['id']}] Missing file: {uc['file']}")

    if missing:
        errors.extend(missing)

def main():
    print("=" * 60)
    print("Duplicate Check — OpenClaw Use Case Atlas")
    print("=" * 60)

    check_json_duplicates()
    check_files_exist()

    if errors:
        print(f"\n❌ Found {len(errors)} issue(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    else:
        print("\n✅ No duplicates found!")
        return 0

if __name__ == "__main__":
    exit(main())
