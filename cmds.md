# Commands Reference - Legacy Code RAG Assistant

This document contains all commands required to run the project from setup to DOE-2.

---

# 1. Clone Project

```bash
git clone <your-github-repository>
cd "Major Proj"
```

---

# 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

Expected:

```bash
(venv) C:\Vidushi\Major Proj>
```

---

# 3. Install Requirements

```bash
pip install -r requirements.txt
```

Verify:

```bash
pip list
```

---

# 4. Clone Experimental Repositories

Navigate to:

```bash
cd data\repositories
```

Clone repositories:

```bash
git clone https://github.com/django-oscar/django-oscar.git Repo_1
```

```bash
git clone https://github.com/Kamva-Ntlanga/hospitality-management-system.git Repo_2
```

```bash
git clone https://github.com/jobic10/student-management-using-django.git Repo_3
```

Return to project root:

```bash
cd ..\..
```

---

# 5. Verify Repository Structure

```bash
dir data\repositories
```

Expected:

```text
Repo_1
Repo_2
Repo_3
```

---

# DOE-1 : Repository Analysis

---

# 6. Run Repository Comparison

```bash
py experiments\DOE1\repository_comparision.py
```

Expected Output:

```text
Scanning Repo_1...
Scanning Repo_2...
Scanning Repo_3...

Results saved successfully.
```

Generated:

```text
data/evaluation/doe1_results.csv
```

---

# 7. Open DOE-1 Results

```bash
notepad data\evaluation\doe1_results.csv
```

---

# AST Parsing & Metadata Extraction

---

# 8. Run Metadata Extraction

```bash
py tests\test_metadata_extraction.py
```

Expected:

```text
Files Parsed: 823
```

Generated:

```text
data/parsed_chunks/metadata.json
```

---

# 9. Run Metadata Statistics

```bash
py tests\test_metadata_stats.py
```

Expected:

```text
Files: 823
Classes: 1662
Functions: 4181
Imports: 2926
```

---

# DOE-2 : Chunking Strategy Comparison

---

# 10. Generate File / Class / Function Chunks

```bash
py backend\chunking\chunk_manager.py
```

Expected:

```text
Generating File Chunks...
File Chunks: 823

Generating Class Chunks...
Class Chunks: 1662

Generating Function Chunks...
Function Chunks: 4181

Chunking Completed.
```

Generated:

```text
data/parsed_chunks/file_chunks.json
data/parsed_chunks/class_chunks.json
data/parsed_chunks/function_chunks.json
```

---

# 11. Run Chunk Statistics

```bash
py tests\test_chunk_stats.py
```

Expected:

```text
file_chunks.json
Chunks: 823

class_chunks.json
Chunks: 1662

function_chunks.json
Chunks: 4181
```

---

# Git Commands

---

# 12. Check Status

```bash
git status
```

---

# 13. Stage Changes

```bash
git add .
```

---

# 14. Commit Changes

```bash
git commit -m "DOE-2 completed"
```

---

# 15. Push Changes

```bash
git push origin main
```

---

# Generated Artifacts

After DOE-2 completes:

```text
data/

├── evaluation/
│   └── doe1_results.csv
│
└── parsed_chunks/
    ├── metadata.json
    ├── file_chunks.json
    ├── class_chunks.json
    └── function_chunks.json
```

---

# Current Project Progress

```text
✅ Repository Selection (DOE-1)

✅ AST Parsing

✅ Metadata Extraction

✅ Structural Statistics

✅ File Chunking

✅ Class Chunking

✅ Function Chunking

🔜 DOE-3: Embedding Comparison
    - MiniLM
    - BGE-Small

🔜 DOE-4: Vector Database
    - FAISS
    - ChromaDB

🔜 DOE-5: Retrieval Evaluation

🔜 DOE-6: LLM Integration

🔜 Dependency Graph Generation

🔜 Streamlit UI
```