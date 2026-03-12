# FiSage

FiSage is a Financial Knowledge Graph platform. It serves as an information hub aggregating data from multiple companies, financial transactions, market information, and public records to build a structured, queryable knowledge graph.

## Architecture

```text
              +-------------------+
   CSV/API/DB |   Loaders         |
  --------->  +-------------------+
              | Transformers      |
              +-------------------+
              | Connectors        |
              +-------------------+
                      |
                      v
                 +--------+
                 | Neo4j  |
                 +--------+
```

## Project Structure

```text
fisage/
├── ingestion/             # Loaders, transformers, connectors
│   ├── base/
│   ├── loaders/
│   ├── transformers/
│   ├── connectors/
│   ├── config/           # source configs (YAML/JSON)
│   └── pipeline.py
├── graph/                 # Neo4j integration code
├── data/                  # Raw & processed data storage
├── scripts/               # Utility scripts
├── api/                   # Optional FastAPI or REST API
├── docker-compose.yml
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Neo4j (Dockerized or local installation)

### Setup

1. **Clone the repository**

```bash
git clone https://github.com/lorenzhoerb/fisage.git
cd fisage
```

2. **Start Neo4j via Docker**

```bash
docker-compose up -d
```

3. **Install Python dependencies**

```bash
uv install
uv run pip install -r requirements.txt
```

4. **Run the ingestion pipeline**

```bash
uv run python -m ingestion.pipeline
```
