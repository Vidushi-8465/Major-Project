import ast
from pathlib import Path


class ASTParser:

    def parse_file(self, file_path):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

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
                imports.extend(
                    alias.name
                    for alias in node.names
                )

        return {
            "file": str(file_path),
            "classes": classes,
            "functions": functions,
            "imports": imports
        }

    def parse_repository(self, repo_path):

        repo_path = Path(repo_path)

        results = []

        for py_file in repo_path.rglob("*.py"):

            try:
                results.append(
                    self.parse_file(py_file)
                )

            except Exception as e:
                print(e)

        return results