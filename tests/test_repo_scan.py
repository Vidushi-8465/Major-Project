from pathlib import Path

from backend.parser.repository_scanner import RepositoryScanner


def test_repository_scanner_stats():
    repo_path = Path("data/repositories/Repo_1/django-oscar")
    scanner = RepositoryScanner(str(repo_path))

    stats = scanner.get_repository_stats()

    assert stats["repository"] == "django-oscar"
    assert stats["python_files"] > 0
    assert stats["lines_of_code"] > 0