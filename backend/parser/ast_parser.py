import ast
from pathlib import Path


class ASTParser:

    def parse_file(self, file_path):

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                source = f.read()

            tree = ast.parse(source)

            classes = []
            functions = []
            imports = []

            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):
                    classes.append(node.name)

                elif isinstance(node, ast.FunctionDef):
                    functions.append(node.name)

                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)

                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)

            return {
                "file_path": str(file_path),
                "classes": classes,
                "functions": functions,
                "imports": imports,
                "line_count": len(source.splitlines()),
                "docstring": ast.get_docstring(tree)
            }

        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None

    def parse_repository(self, repo_path):

        results = []

        for file in Path(repo_path).rglob("*.py"):

            metadata = self.parse_file(file)

            if metadata:
                results.append(metadata)

        return results