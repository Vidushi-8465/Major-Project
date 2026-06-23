from pathlib import Path


class FileChunker:

    def chunk_repository(self, repo_path):

        chunks = []
        chunk_id = 1

        for file in Path(repo_path).rglob("*.py"):

            try:

                with open(
                    file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                chunks.append(
                    {
                        "chunk_id": f"file_{chunk_id}",
                        "chunk_type": "file",
                        "file_path": str(file),
                        "content": content,
                        "size": len(content)
                    }
                )

                chunk_id += 1

            except Exception as e:

                print(
                    f"Error reading {file}: {e}"
                )

        return chunks