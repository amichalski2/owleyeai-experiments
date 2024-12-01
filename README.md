![Owleye.AI Logo](/images/logo.png)

# Owleye-Experiments

This repository contains experimental code and prototypes focusing on Retrieval-Augmented Generation (RAG) and AI Agents research. Each experiment is designed to explore different aspects of these technologies and their potential applications.

## 🎯 Research Focus

### RAG Experiments
- Implementation and testing of various RAG architectures
- Document retrieval optimization
- Context relevancy improvements
- Different embedding models comparison
- Prompt engineering for RAG systems

### AI Agents
- General agent behaviors
- Multi-agent interactions
- Task planning and execution
- Tool usage and integration
- Memory and context management

## 🏗️ Repository Structure

```
owleye-experiments/
├── experiments/          # Individual experiments
│   ├── experiment_001/  # Each experiment has its own environment
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── config/
│   │   ├── data/
│   │   ├── notebooks/
│   │   └── src/
│   └── ...
├── common/              # Shared utilities
```

## 🚀 Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/username/owleye-experiments.git
cd owleye-experiments
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# or
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
# Install base dependencies
pip install -r requirements.txt

# For specific experiment
pip install -r experiments/experiment_XXX/requirements.txt
```

## 🧪 Running Experiments

Each experiment is self-contained in its directory with its own README, requirements, and documentation. To run a specific experiment:

1. Navigate to the experiment directory:
```bash
cd experiments/experiment_XXX
```

2. Read the experiment's README.md for specific setup instructions

3. Install experiment-specific dependencies:
```bash
pip install -r requirements.txt
```

4. Follow the experiment-specific run instructions in its README

## 📝 Experiment Documentation

Each experiment directory contains:
- README.md with experiment description and results
- Configuration files in `config/`
- Jupyter notebooks with analysis in `notebooks/`
- Source code in `src/`
- Data samples or data processing scripts in `data/`

## 🤝 Contributing

1. Create a new experiment directory:
```bash
mkdir experiments/experiment_XXX
```

2. Follow the coding conventions:
- Use PEP 8 style guide
- Add comprehensive docstrings
- Update experiment README with results

## 📊 Experiment Results

Results and findings from each experiment are documented in their respective README files. Key findings and comparisons across experiments are summarized in the Wiki section of this repository.

## 🔧 Utils and Common Code

The `common/` directory contains shared utilities for:
- Data processing
- Evaluation metrics
- Visualization tools
- Common interfaces

This project is licensed under the MIT License - see the LICENSE file for details.

## ✨ Acknowledgments

- List any papers, libraries, or tools that inspired your experiments
- Credit to contributors and collaborators

---

For more detailed information about specific experiments, please refer to their individual README files in the `experiments/` directory.