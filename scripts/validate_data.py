#!/usr/bin/env python3
"""
Validate use_cases.json and use_cases.csv for consistency and required fields.
"""

import json
import csv
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
JSON_PATH = REPO_ROOT / "data" / "use_cases.json"
CSV_PATH = REPO_ROOT / "data" / "use_cases.csv"

REQUIRED_JSON_FIELDS = ["id", "name", "category", "family", "status", "safety_level", "evidence_tier", "scores", "source_quality", "file"]
REQUIRED_SCORES = ["value", "difficulty", "risk", "evidence", "mvp_fit", "openclaw_fit", "time_to_value"]
VALID_EVIDENCE_TIERS = ["E0", "E1", "E2", "E3", "E4", "E5"]
VALID_SAFETY_LEVELS = ["L0", "L1", "L2", "L3", "L4", "L0-L1", "L0-L2", "L0-L3", "L1-L2", "L1-L3", "L2-L3"]
VALID_STATUSES = ["confirmed", "experimental", "adapted", "inferred", "ai_idea"]
VALID_SOURCE_QUALITY = ["high", "medium", "low", "medium-high", "medium-low"]

errors = []
warnings = []

def validate_json():
    if not JSON_PATH.exists():
        errors.append(f"JSON file not found: {JSON_PATH}")
        return None

    with open(JSON_PATH) as f:
        data = json.load(f)

    if "use_cases" not in data:
        errors.append("Missing 'use_cases' key in JSON")
        return None

    ids = set()
    files = set()
    for uc in data["use_cases"]:
        # Required fields
        for field in REQUIRED_JSON_FIELDS:
            if field not in uc:
                errors.append(f"[{uc.get('id', 'NO_ID')}] Missing required field: {field}")

        # Duplicate IDs
        if uc.get("id") in ids:
            errors.append(f"Duplicate ID: {uc['id']}")
        ids.add(uc.get("id"))

        # Duplicate files
        if uc.get("file") in files:
            errors.append(f"Duplicate file path: {uc['file']}")
        files.add(uc.get("file"))

        # Evidence tier
        if uc.get("evidence_tier") not in VALID_EVIDENCE_TIERS:
            warnings.append(f"[{uc.get('id', '?')}] Unusual evidence_tier: {uc.get('evidence_tier')}")

        # Safety level
        if uc.get("safety_level") not in VALID_SAFETY_LEVELS:
            warnings.append(f"[{uc.get('id', '?')}] Unusual safety_level: {uc.get('safety_level')}")

        # Status
        if uc.get("status") not in VALID_STATUSES:
            warnings.append(f"[{uc.get('id', '?')}] Unusual status: {uc.get('status')}")

        # Scores
        scores = uc.get("scores", {})
        for score_field in REQUIRED_SCORES:
            if score_field not in scores:
                errors.append(f"[{uc.get('id', '?')}] Missing score: {score_field}")
            elif not isinstance(scores[score_field], int) or not (1 <= scores[score_field] <= 5):
                if score_field != "time_to_value":
                    errors.append(f"[{uc.get('id', '?')}] Invalid score for {score_field}: {scores[score_field]}")

        # File exists
        if uc.get("file") and not (REPO_ROOT / uc["file"]).exists():
            warnings.append(f"[{uc.get('id', '?')}] Referenced file does not exist: {uc['file']}")

    return data

def validate_csv():
    if not CSV_PATH.exists():
        errors.append(f"CSV file not found: {CSV_PATH}")
        return

    with open(CSV_PATH) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    json_ids = set()
    json_data = validate_json()
    if json_data:
        json_ids = {uc["id"] for uc in json_data["use_cases"]}

    csv_ids = set()
    for row in rows:
        if row.get("id") in csv_ids:
            errors.append(f"Duplicate CSV ID: {row['id']}")
        csv_ids.add(row.get("id"))

    # Check JSON and CSV have same IDs
    missing_in_csv = json_ids - csv_ids
    missing_in_json = csv_ids - json_ids

    if missing_in_csv:
        warnings.append(f"IDs in JSON but not CSV: {missing_in_csv}")
    if missing_in_json:
        warnings.append(f"IDs in CSV but not JSON: {missing_in_json}")

def main():
    print("=" * 60)
    print("OpenClaw Use Case Atlas — Data Validation")
    print("=" * 60)

    validate_json()
    validate_csv()

    if warnings:
        print(f"\n⚠️  Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print(f"\n❌ Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        print(f"\nValidation FAILED: {len(errors)} error(s)")
        sys.exit(1)
    else:
        print("\n✅ Validation passed!")
        if warnings:
            print(f"   ({len(warnings)} warning(s) — non-blocking)")
        sys.exit(0)

if __name__ == "__main__":
    main()
