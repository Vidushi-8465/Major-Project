# tests/test_metadata_stats.py

import json

with open(
    "data/parsed_chunks/metadata.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

total_files = len(data)

total_classes = sum(
    len(item["classes"])
    for item in data
)

total_functions = sum(
    len(item["functions"])
    for item in data
)

total_imports = sum(
    len(item["imports"])
    for item in data
)

print(f"Files: {total_files}")
print(f"Classes: {total_classes}")
print(f"Functions: {total_functions}")
print(f"Imports: {total_imports}")