import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd
from backend.parser.repository_scanner import RepositoryScanner

repos = [
    "data/repositories/Repo_1",
    "data/repositories/Repo_2",
    "data/repositories/Repo_3"
]

results = []

for repo in repos:
    scanner = RepositoryScanner(repo)

    stats = scanner.get_repository_stats()

    results.append(stats)

df = pd.DataFrame(results)

print(df)

df.to_csv(
    "data/evaluation/doe1_results.csv",
    index=False
)