import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from backend.parser.metadata_extractor import MetadataExtractor

REPO = "data/repositories/Repo_1/django-oscar"

OUTPUT = "data/parsed_chunks/metadata.json"

extractor = MetadataExtractor()

metadata = extractor.extract_repository_metadata(
    REPO,
    OUTPUT
)

print(f"Files Parsed: {len(metadata)}")

print(metadata[0])