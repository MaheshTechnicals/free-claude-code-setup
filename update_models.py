#!/usr/bin/env python3
"""
update_models.py
Fetches free models from OpenCode API and updates the cheat sheet markdown file.
"""

import urllib.request
import json
import re
from datetime import datetime, timezone, timedelta

API_URL = "https://opencode.ai/zen/v1/models"
README_PATH = "cheat-sheet-free-claude-code.md"

def fetch_free_models():
    """Fetch model list from OpenCode API and return only free ones."""
    req = urllib.request.Request(
        API_URL,
        headers={"User-Agent": "Mozilla/5.0 (GitHub-Actions)"}
    )
    with urllib.request.urlopen(req, timeout=15) as response:
        data = json.loads(response.read().decode())

    models = data.get("data", [])
    free_models = [m for m in models if "free" in m.get("id", "").lower()]
    return free_models

def build_table(models):
    """Build a markdown table string from the model list."""
    lines = []
    lines.append("| Model ID | Status |")
    lines.append("|----------|--------|")
    for model in models:
        model_id = model.get("id", "unknown")
        lines.append(f"| `{model_id}` | FREE |")
    return "\n".join(lines)

def update_readme(table_content, timestamp):
    """Replace the placeholder section in the markdown file with fresh table."""
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace models table between markers
    new_section = f"<!-- FREE_MODELS_START -->\n{table_content}\n<!-- FREE_MODELS_END -->"
    content = re.sub(
        r"<!-- FREE_MODELS_START -->.*?<!-- FREE_MODELS_END -->",
        new_section,
        content,
        flags=re.DOTALL
    )

    # Replace last updated timestamp
    content = re.sub(
        r"<!-- LAST_UPDATED -->.*",
        f"<!-- LAST_UPDATED --> `{timestamp} IST`",
        content
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    print("Fetching free models from OpenCode API...")
    try:
        models = fetch_free_models()
    except Exception as e:
        print(f"ERROR: Failed to fetch models: {e}")
        raise SystemExit(1)

    if not models:
        print("WARNING: No free models found. File will not be updated.")
        raise SystemExit(1)

    print(f"Found {len(models)} free model(s):")
    for m in models:
        print(f"  - {m.get('id')}")

    table = build_table(models)
    ist = timezone(timedelta(hours=5, minutes=30))
    timestamp = datetime.now(ist).strftime("%Y-%m-%d %H:%M")

    print("\nUpdating cheat-sheet-free-claude-code.md...")
    update_readme(table, timestamp)
    print("Done! File updated successfully.")

if __name__ == "__main__":
    main()
