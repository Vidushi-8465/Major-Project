import json
from pathlib import Path

from backend.chunking.file_chunker import FileChunker
from backend.chunking.class_chunker import ClassChunker
from backend.chunking.function_chunker import FunctionChunker


REPO_PATH = (
    "data/repositories/"
    "Repo_1/django-oscar"
)

OUTPUT_DIR = Path(
    "data/parsed_chunks"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def save_json(
    data,
    filename
):

    with open(
        OUTPUT_DIR / filename,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


if __name__ == "__main__":

    print(
        "\nGenerating File Chunks..."
    )

    file_chunks = (
        FileChunker()
        .chunk_repository(
            REPO_PATH
        )
    )

    save_json(
        file_chunks,
        "file_chunks.json"
    )

    print(
        f"File Chunks: "
        f"{len(file_chunks)}"
    )

    print(
        "\nGenerating Class Chunks..."
    )

    class_chunks = (
        ClassChunker()
        .chunk_repository(
            REPO_PATH
        )
    )

    save_json(
        class_chunks,
        "class_chunks.json"
    )

    print(
        f"Class Chunks: "
        f"{len(class_chunks)}"
    )

    print(
        "\nGenerating Function Chunks..."
    )

    function_chunks = (
        FunctionChunker()
        .chunk_repository(
            REPO_PATH
        )
    )

    save_json(
        function_chunks,
        "function_chunks.json"
    )

    print(
        f"Function Chunks: "
        f"{len(function_chunks)}"
    )

    print(
        "\nChunking Completed."
    )