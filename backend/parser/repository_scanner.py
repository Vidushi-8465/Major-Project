from pathlib import Path
from collections import defaultdict


class RepositoryScanner:
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)

    def get_python_files(self):
        return list(self.repo_path.rglob("*.py"))

    def count_python_files(self):
        return len(self.get_python_files())

    def count_lines_of_code(self):
        total = 0

        for file in self.get_python_files():
            try:
                with open(file, "r", encoding="utf-8") as f:
                    total += len(f.readlines())
            except Exception:
                pass

        return total

    def generate_tree(self):
        tree = defaultdict(list)

        for path in self.repo_path.rglob("*"):
            if path.is_file():
                tree[str(path.parent)].append(path.name)

        return dict(tree)

    def get_repository_stats(self):
        return {
            "repository": self.repo_path.name,
            "python_files": self.count_python_files(),
            "lines_of_code": self.count_lines_of_code(),
        }