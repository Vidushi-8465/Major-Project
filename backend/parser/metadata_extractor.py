import json
from pathlib import Path

from backend.parser.ast_parser import ASTParser


class MetadataExtractor:

    def __init__(self):
        self.parser = ASTParser()

    def extract_repository_metadata(
        self,
        repo_path,
        output_file
    ):

        metadata = self.parser.parse_repository(repo_path)

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                metadata,
                f,
                indent=4
            )

        return metadata