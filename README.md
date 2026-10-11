<div align="center">

# 🔬 Shod — AI Research Agent

### Research smarter. Discover papers. Build answers from evidence.

An AI research assistant that combines academic paper discovery, hybrid retrieval, evidence analysis and verification into one agentic workflow.

![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![OpenSearch](https://img.shields.io/badge/OpenSearch-005EB8?style=for-the-badge&logo=opensearch&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</div>

---

<div align="center">
  <img src="docs/images/shod-ui.png" alt="Shod research workspace" width="900" />
  <br>
  <sub>The Shod research workspace: ask a question, explore papers, get evidence-backed answers.</sub>
</div>

## 📖 Overview

Research often means jumping between academic search engines, papers, notes and scattered sources. Shod simplifies this by combining paper discovery with retrieval-augmented generation and evidence-aware agent orchestration.

Built with **LangGraph, LangChain, OpenSearch, FastAPI and React**, Shod plans the research, retrieves relevant evidence, analyzes findings, verifies support and then generates a grounded answer.

> 📱 A Telegram-based interface is part of the upcoming Shod experience, bringing research assistance closer to where users communicate.

## ✨ Key Capabilities

| | Capability | Description |
|---|---|---|
| 🧠 | **Agentic research workflow** | Orchestrates planning, research, analysis, verification and answer generation using LangGraph |
| 📚 | **Academic paper discovery** | Searches arXiv for relevant research papers |
| 🔎 | **Hybrid retrieval** | Combines BM25 keyword search and semantic retrieval |
| 🧮 | **Reciprocal Rank Fusion** | Merges lexical and semantic rankings into one result set |
| 🧾 | **Evidence-aware analysis** | Synthesizes retrieved passages into research findings |
| ✅ | **Evidence verification** | Checks whether findings are supported and can trigger additional research |
| 🔗 | **Structured source tracking** | Maintains paper metadata, source URLs and retrieved evidence |
| 💾 | **Persistent graph state** | PostgreSQL-backed LangGraph checkpointing for conversation and workflow state |
| 🖥️ | **Web interface** | React research workspace backed by a FastAPI application |
| 🏠 | **Local model support** | Runs on Ollama locally, with Gemini and Groq as additional providers |
| 🔭 | **Observability** | LangSmith integration for inspecting and debugging agent runs |

## 🏗️ Architecture

### System overview

<div align="center">
  <img src="docs/images/system-overview.svg" alt="Shod system overview" width="900" />
</div>

### Agent workflow

```mermaid
flowchart TD
    U[Research Question] --> API[FastAPI]
    API --> P[Planner]
    P --> R[Researcher]

    R --> T{Research Tools}
    T --> A[arXiv Search]
    T --> O[OpenSearch Hybrid Retrieval]
    T --> G[Paper Retrieval]

    A --> R
    O --> R
    G --> R

    R --> S[Capture Sources]
    S --> N[Analyzer]
    N --> V[Verifier]

    V -->|Additional evidence needed| R
    V -->|Continue| AG[Answer Agent]

    AG --> OUT[Answer and Sources]
    OUT --> API
    API --> UI[React Interface]

    DB[(PostgreSQL Checkpointer)] -.-> API
    LS[LangSmith Observability] -.-> P
```

## ⚙️ How It Works

### 1. Research planning
The planner interprets the research question and creates a plan to guide evidence collection.

### 2. Research and retrieval
The researcher uses available tools to discover academic papers and retrieve relevant passages from the indexed research corpus.

### 3. Hybrid search
Shod combines two complementary retrieval approaches:

- **BM25:** finds relevant documents through lexical matching.
- **Semantic search:** retrieves conceptually related passages using vector embeddings.

Reciprocal Rank Fusion combines the rankings from both methods into a unified result set.

<div align="center">
  <img src="docs/images/hybrid-retrieval.svg" alt="Hybrid retrieval pipeline" width="900" />
</div>

### 4. Source capture
Retrieved evidence is collected into structured source records containing paper titles, arXiv identifiers, URLs and evidence passages.

### 5. Analysis and verification
The analyzer synthesizes the retrieved evidence. The verifier checks whether the findings are supported, identifies limitations and assesses whether further research is needed.

The graph can route back to the researcher when additional evidence is required, subject to a bounded iteration limit.

### 6. Answer generation
The answer agent uses the research findings, source evidence and verification feedback to produce a response.

## 🧰 Technology Stack

| Component | Technology |
|---|---|
| Frontend | React, JavaScript, Vite |
| UI and styling | Tailwind CSS v4, shadcn/ui, Base UI, Lucide |
| API | FastAPI, Pydantic |
| Agent orchestration | LangGraph, LangChain |
| Paper discovery | arXiv API |
| Search engine | OpenSearch |
| Retrieval methods | BM25, semantic search, Reciprocal Rank Fusion |
| Embeddings | Hugging Face Sentence Transformers |
| Persistence | PostgreSQL, LangGraph checkpointing |
| Local inference | Ollama |
| Additional LLM providers | Gemini, Groq |
| Observability | LangSmith |
| Service management | Docker Compose |

## 📁 Project Structure

```
Shod/
├── src/
│   └── researchagent/
│       ├── graph/          # Agent workflow and state
│       ├── tools/          # Research tools
│       ├── ingestion/      # Paper discovery and ingestion
│       ├── retrieval/      # Hybrid search and OpenSearch
│       ├── rag/            # LLM and RAG components
│       └── database/       # Database integrations
├── FastApi/
│   ├── main.py             # HTTP endpoints
│   ├── service.py          # Research graph integration
│   └── schemas.py          # API schemas
├── frontend/
│   └── src/                # React application
├── docs/
│   └── images/             # README images
├── test/                   # Tests and development scripts
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- [uv](https://docs.astral.sh/uv/)
- Node.js and npm
- Docker and Docker Compose
- [Ollama](https://ollama.com/)

### 1. Clone the repository

```bash
git clone https://github.com/Pranav-MRK/ShodAi.git
cd ShodAi
```

### 2. Install backend dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a local `.env` file using `.env.example` as a reference. Configure the variables required by your selected LLM provider, OpenSearch, PostgreSQL, and LangSmith if tracing is enabled.

> 🔒 Keep API keys and other secrets out of Git.

### 4. Start supporting services

```bash
docker compose up -d
```

Check the Compose configuration for the services and ports used by your local setup.

### 5. Start the local model

For the default Ollama configuration:

```bash
ollama pull llama3.2:3b
ollama list
```

Ensure the Ollama service is running before starting research requests.

### 6. Run the backend

From the repository root:

```bash
uv run uvicorn FastApi.main:app --reload
```

API documentation: <http://localhost:8000/docs>

### 7. Run the frontend

In a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite, typically <http://localhost:5173>. Make sure the API CORS configuration allows your frontend origin.

## 🔌 API Usage

### Research endpoint

`POST /research`

Example request:

```json
{
  "question": "How can retrieval-augmented generation reduce hallucinations in large language models?",
  "thread_id": null
}
```

The response includes the thread identifier, question, generated answer, retrieved sources and verification output. Refer to `/docs` for the active request and response schemas.

## 🧭 Design Decisions

<details>
<summary><b>Why LangGraph?</b></summary>

Research is a multi-step process involving tool execution, conditional routing, state management and bounded retries. LangGraph makes these transitions explicit and allows the workflow to be inspected and extended.
</details>

<details>
<summary><b>Why hybrid retrieval?</b></summary>

Keyword search and semantic search solve complementary problems. BM25 is useful for exact terminology, while semantic retrieval helps identify passages with related meaning. RRF combines their rankings.
</details>

<details>
<summary><b>Why a separate verifier?</b></summary>

Generating a plausible answer is not the same as verifying its supporting evidence. A separate verification stage makes evidence sufficiency and additional research explicit parts of the workflow.
</details>

<details>
<summary><b>Why PostgreSQL and OpenSearch?</b></summary>

PostgreSQL supports durable workflow state and checkpointing, while OpenSearch supports indexing and retrieval over the research corpus. Each service has a distinct responsibility.
</details>

<details>
<summary><b>Why support local inference?</b></summary>

Ollama allows development and experimentation with local models, reducing dependence on paid inference APIs for supported workflows.
</details>

## 🗺️ Roadmap

- [x] Agentic research workflow with planning, verification and answer generation
- [x] Hybrid retrieval with BM25, semantic search and RRF
- [x] React research workspace backed by FastAPI
- [x] Persistent main research threads and paper-specific conversations
- [x] Progressive answer streaming and research-status updates
- [x] Research evaluation and answer-quality measurement
- [x] Guardrails, reliability improvements and deployment automation
- [x] Telegram-based research assistant
- [x] Productivity integrations for research documents, spreadsheets and email

## 🔐 Security

- Store API keys and credentials in environment variables or a secret manager.
- Keep `.env`, local model files and private research data out of version control.
- Validate incoming API requests and handle dependency failures.
- Review access controls before exposing the API publicly.



<div align="center">

**Shod — turning research questions into evidence-backed exploration.**

Built by [Pranav](https://github.com/Pranav-MRK) · ⭐ Star the repo if you find it useful!

</div>