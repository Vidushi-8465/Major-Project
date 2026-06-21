# RAG-Based Legacy Code Understanding and Documentation Assistant

## Final Year Major Project

### Team Size
4 Members

### Domain
Artificial Intelligence + Retrieval Augmented Generation (RAG) + Software Engineering + NLP + Knowledge Graphs

---

# 1. Project Overview

Software developers often work on code written by other developers.

When documentation is missing or outdated, understanding a codebase becomes difficult and time-consuming.

Developers typically spend hours:

- Reading source files
- Understanding project architecture
- Tracing function calls
- Understanding module dependencies
- Finding the impact of code changes

Traditional code search tools can locate files and keywords but cannot explain:

- How a feature is implemented
- Which files participate in a workflow
- Dependencies between modules
- Impact of modifying a component

This project solves that problem by building an AI-powered assistant that understands source code repositories and answers developer questions using Retrieval-Augmented Generation (RAG).

---

# 2. Problem Statement

Suppose a new developer joins a company and receives a legacy Python project containing:

```text
100 Files
15,000+ Lines of Code
Little or No Documentation
```

The developer asks:

```text
How does login work?
```

Instead of manually reading many files, the system automatically:

1. Parses the repository
2. Retrieves relevant code sections
3. Identifies dependencies
4. Generates an explanation using an LLM

Example Output:

```text
Login Flow:

LoginController
    ↓
AuthService
    ↓
UserRepository
    ↓
Database

Files involved:
- login_controller.py
- auth_service.py
- user_repository.py
```

---

# 3. Project Objectives

## Primary Objectives

- Parse Python repositories
- Extract classes and functions
- Generate embeddings
- Store code knowledge in a vector database
- Retrieve relevant code chunks
- Generate developer-friendly explanations

## Secondary Objectives

- Dependency analysis
- Function call tracing
- Auto documentation generation
- Repository summarization
- Impact analysis

---

# 4. Scope

# 5. Included 
Evaluation repositories:

1. Django Oscar
   - Enterprise e-commerce system

2. Hospitality Management System
   - Domain workflow system

3. Student Management System
   - Small-scale baseline system

Repository Size:

```text
50–100 Files
5000–20000 LOC
```

## Not Included

- Multi-language repositories
- Automatic bug fixing
- Code generation
- IDE plugins
- Enterprise-scale systems

---

# 5. System Architecture

```text
Repository Upload
        │
        ▼
Repository Scanner
        │
        ▼
AST Parser
        │
        ▼
Chunking Engine
        │
        ▼
Embedding Model
        │
        ▼
Vector Database
        │
        ▼
Retriever
        │
        ▼
Large Language Model
        │
        ▼
Developer Explanation
```

---

# 6. Technology Stack

## Programming Language

- Python

## RAG Framework

- LangChain

OR

- LlamaIndex

## Embedding Models

### Model A

BAAI/bge-small-en-v1.5

### Model B

all-MiniLM-L6-v2

## Vector Databases

### Option A

FAISS

### Option B

ChromaDB

## LLM

### Option A

Llama 3 8B

### Option B

Mistral 7B

Running Through:

- Ollama

## Frontend

- Streamlit

## Dependency Visualization

- NetworkX
- Graphviz

---

# 7. Project Folder Structure

```text
rag-legacy-code-assistant/

├── README.md
├── requirements.txt
├── .env
├── .gitignore

├── data/
├── backend/
├── frontend/
├── experiments/
├── reports/
├── docs/
└── tests/
```

---

# 8. Folder Explanations

---

# data/

Contains all generated project data.

```text
data/

├── repositories/
├── parsed_chunks/
├── embeddings/
├── vectordb/
├── dependency_graphs/
├── generated_docs/
└── evaluation/
```

---

## repositories/

Stores downloaded GitHub repositories.

Example:

```text
repositories/

├── student_management/
├── ecommerce/
└── hospital_management/
```

Purpose:

- DOE-1 Repository Selection
- Repository Testing

---

## parsed_chunks/

Stores parsed code chunks.

```text
parsed_chunks/

├── file_chunks.json
├── class_chunks.json
├── function_chunks.json
└── metadata.json
```

Purpose:

- DOE-2 Chunking Experiment
- Retrieval Dataset

---

### file_chunks.json

Stores entire files as chunks.

Example:

```json
{
  "file":"auth.py",
  "content":"Entire file"
}
```

---

### class_chunks.json

Stores classes as chunks.

Example:

```json
{
  "class":"AuthService"
}
```

---

### function_chunks.json

Stores functions as chunks.

Example:

```json
{
  "function":"login"
}
```

---

### metadata.json

Stores metadata.

Example:

```json
{
  "file":"auth.py",
  "class":"AuthService",
  "function":"login"
}
```

---

## embeddings/

Stores vector embeddings.

```text
embeddings/

├── minilm_embeddings.pkl
└── bge_embeddings.pkl
```

Purpose:

- DOE-3 Embedding Comparison

---

## vectordb/

Stores vector databases.

```text
vectordb/

├── chromadb/
└── faiss/
```

Purpose:

- DOE-4 Database Comparison

---

## dependency_graphs/

Stores generated dependency diagrams.

```text
dependency_graphs/

├── login_graph.png
├── payment_graph.png
└── full_repository_graph.png
```

Purpose:

- Dependency Analysis
- Call Flow Visualization

---

## generated_docs/

Stores auto-generated documentation.

```text
generated_docs/

├── README_GENERATED.md
├── auth_module.md
└── full_project_docs.md
```

Purpose:

- Auto Documentation Feature

---

## evaluation/

Stores experiment results.

```text
evaluation/

├── doe1_results.csv
├── doe2_results.csv
├── doe3_results.csv
├── doe4_results.csv
├── doe5_results.csv
├── doe6_results.csv
└── final_metrics.csv
```

Purpose:

- Report Writing
- Viva Demonstration

---

# backend/

Contains the complete project logic.

```text
backend/

├── parser/
├── chunking/
├── embeddings/
├── vectordb/
├── retrieval/
├── llm/
├── dependency_graph/
├── rag/
├── evaluation/
├── api/
└── utils/
```

---

# parser/

Responsible for code analysis.

```text
parser/

├── repository_scanner.py
├── ast_parser.py
├── metadata_extractor.py
└── import_extractor.py
```

---

### repository_scanner.py

Purpose:

- Scan repository
- Count files
- Generate project structure

---

### ast_parser.py

Purpose:

- Parse Python code using AST
- Extract classes
- Extract functions

---

### metadata_extractor.py

Purpose:

- Extract metadata

Example:

```json
{
  "file":"auth.py",
  "class":"AuthService"
}
```

---

### import_extractor.py

Purpose:

- Extract imports
- Build dependency relationships

---

# chunking/

Responsible for DOE-2.

```text
chunking/

├── file_chunker.py
├── class_chunker.py
├── function_chunker.py
└── chunk_manager.py
```

---

### file_chunker.py

Chunking Method A

Entire File = One Chunk

---

### class_chunker.py

Chunking Method B

One Class = One Chunk

---

### function_chunker.py

Chunking Method C

One Function = One Chunk

---

### chunk_manager.py

Controls all chunking methods.

---

# embeddings/

Responsible for DOE-3.

```text
embeddings/

├── embedding_generator.py
├── minilm_embedder.py
└── bge_embedder.py
```

---

### embedding_generator.py

Main embedding service.

---

### minilm_embedder.py

MiniLM implementation.

---

### bge_embedder.py

BGE implementation.

---

# vectordb/

Responsible for DOE-4.

```text
vectordb/

├── chromadb_manager.py
├── faiss_manager.py
└── vector_store_factory.py
```

---

### chromadb_manager.py

Handles ChromaDB operations.

---

### faiss_manager.py

Handles FAISS operations.

---

### vector_store_factory.py

Selects active database.

---

# retrieval/

Responsible for DOE-5.

```text
retrieval/

├── retriever.py
├── reranker.py
└── search_service.py
```

---

### retriever.py

Top-K retrieval.

---

### reranker.py

Improves retrieval quality.

---

### search_service.py

Unified search interface.

---

# llm/

Responsible for DOE-6.

```text
llm/

├── ollama_client.py
├── prompt_templates.py
├── explanation_generator.py
└── documentation_generator.py
```

---

### ollama_client.py

Communicates with Ollama.

---

### prompt_templates.py

Stores prompt templates.

---

### explanation_generator.py

Generates developer explanations.

---

### documentation_generator.py

Generates documentation.

---

# dependency_graph/

Responsible for dependency visualization.

```text
dependency_graph/

├── dependency_builder.py
├── graph_generator.py
├── graph_visualizer.py
└── call_trace_builder.py
```

---

### dependency_builder.py

Builds dependency graph.

---

### graph_generator.py

Creates graph structure.

---

### graph_visualizer.py

Generates PNG diagrams.

---

### call_trace_builder.py

Tracks function call chains.

---

# rag/

Contains RAG pipeline.

```text
rag/

├── rag_pipeline.py
├── context_builder.py
└── query_processor.py
```

---

### rag_pipeline.py

Complete RAG workflow.

---

### context_builder.py

Builds LLM context.

---

### query_processor.py

Processes user queries.

---

# evaluation/

Measures project performance.

```text
evaluation/

├── retrieval_metrics.py
├── response_metrics.py
├── hallucination_metrics.py
└── experiment_runner.py
```

---

# api/

Backend API layer.

```text
api/

├── app.py
├── routes.py
└── schemas.py
```

---

### app.py

FastAPI entry point.

---

### routes.py

API endpoints.

---

### schemas.py

Request and response models.

---

# frontend/

User Interface.

```text
frontend/

├── Home.py

├── pages/
│   ├── Upload_Repository.py
│   ├── Ask_Questions.py
│   ├── Retrieved_Code.py
│   ├── Dependency_Graph.py
│   ├── Auto_Documentation.py
│   └── Experiments.py

├── components/
└── assets/
```

---

# Frontend Pages

---

## Upload Repository

Upload GitHub repository.

---

## Ask Questions

Developer chat interface.

Example:

```text
How does login work?
```

---

## Retrieved Code

Displays retrieved chunks.

---

## Dependency Graph

Displays module relationships.

---

## Auto Documentation

Displays generated documentation.

---

## Experiments

Displays DOE results.

---

# experiments/

Contains all DOE implementations.

```text
experiments/

├── DOE1/
├── DOE2/
├── DOE3/
├── DOE4/
├── DOE5/
└── DOE6/
```

---

# DOE1

Repository Selection

---

# DOE2

Chunking Comparison

---

# DOE3

Embedding Comparison

---

# DOE4

FAISS vs ChromaDB

---

# DOE5

Top-K Retrieval Comparison

---

# DOE6

Llama3 vs Mistral Comparison

---

# reports/

Stores final reports.

```text
reports/

├── DOE1_Report.pdf
├── DOE2_Report.pdf
├── DOE3_Report.pdf
├── DOE4_Report.pdf
├── DOE5_Report.pdf
├── DOE6_Report.pdf
└── Final_Report.pdf
```

---

# docs/

Contains project documentation.

```text
docs/

├── architecture.md
├── system_design.md
├── api_documentation.md
└── user_manual.md
```

---

# tests/

Contains unit tests.

```text
tests/

├── test_parser.py
├── test_chunking.py
├── test_embeddings.py
├── test_retrieval.py
└── test_rag_pipeline.py
```

---

# 9. Expected Features

✓ Repository Upload

✓ Code Parsing

✓ AST Analysis

✓ Semantic Search

✓ RAG Pipeline

✓ Dependency Visualization

✓ Function Call Tracing

✓ Auto Documentation

✓ Repository Summarization

✓ Impact Analysis

✓ DOE Evaluation Dashboard

---

# 10. Expected Outcome

The system should be able to:

- Understand legacy Python repositories
- Explain project architecture
- Trace feature implementation
- Generate documentation
- Visualize dependencies
- Help developers understand unfamiliar codebases faster

The final product acts as an AI-powered software architect and code understanding assistant for legacy Python projects.