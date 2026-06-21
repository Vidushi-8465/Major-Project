from pathlib import Path

from backend.parser.ast_parser import ASTParser


def test_ast_parser_reads_repository():
    repo_path = Path("data/repositories/Repo_1/django-oscar")
    parser = ASTParser()

    data = parser.parse_repository(str(repo_path))

    assert data
    first_entry = data[0]
    assert "file" in first_entry
    assert "classes" in first_entry
    assert "functions" in first_entry
    assert "imports" in first_entry