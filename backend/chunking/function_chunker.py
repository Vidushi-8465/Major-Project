import ast
from pathlib import Path


class FunctionChunker:

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

                    source = f.read()

                tree = ast.parse(source)

                for node in ast.walk(tree):

                    if isinstance(
                        node,
                        ast.FunctionDef
                    ):

                        chunks.append(
                            {
                                "chunk_id":
                                f"function_{chunk_id}",

                                "chunk_type":
                                "function",

                                "file_path":
                                str(file),

                                "function_name":
                                node.name,

                                "start_line":
                                node.lineno,

                                "end_line":
                                getattr(
                                    node,
                                    "end_lineno",
                                    node.lineno
                                ),

                                "content":
                                ast.unparse(node)
                            }
                        )

                        chunk_id += 1

            except Exception as e:

                print(
                    f"Error processing {file}: {e}"
                )

        return chunks