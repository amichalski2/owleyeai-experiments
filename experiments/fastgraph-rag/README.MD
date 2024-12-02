# FastGraph-RAG Example: Knowledge Graph Analysis

A simple example demonstrating how to use FastGraph-RAG for text analysis and knowledge extraction.

## 🚀 Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Usage

1. Place your text file in the data directory
2. Configure analysis parameters in `config.yaml`
3. Run the analysis:

```python
from src.graph_rag import PromptAnalyzer

analyzer = PromptAnalyzer("./config/config.yaml")

response = analyzer.analyze_techniques(
    "What are the main categories of AI agents?"
)
print(response.response)
```

## 📁 Project Structure

```
.
├── config/
│   └── config.yaml        # Analysis configuration
├── data/
│   ├── source.txt        # Source text
│   └── processed/        # FastGraph-RAG data
└── src/
    └── graph_rag.py      # Implementation
```

## ⚙️ Configuration

Edit `config.yaml` to customize the analysis:

```yaml
experiment:
  name: "fastgraph_rag_example"
  description: "Text analysis using FastGraph-RAG"

graphrag:
  domain: "Your analysis domain"
  entity_types:
    - "Type1"
    - "Type2"
  example_queries:
    - "Example query 1"
    - "Example query 2"
```

## 🛠️ Dependencies

- fast-graphrag
- jupyterlab
- nest-asyncio