from fast_graphrag import GraphRAG
from pathlib import Path
from typing import Dict
import yaml
import asyncio
import nest_asyncio
from IPython import get_ipython

nest_asyncio.apply()

class PromptAnalyzer:
    def __init__(self, config_path: str):
        """Initialize analyzer with config file."""
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
            
        self.grag = GraphRAG(
            working_dir=self.config['data']['processed_dir'],
            domain=self.config['graphrag']['domain'],
            example_queries="\n".join(self.config['graphrag']['example_queries']),
            entity_types=self.config['graphrag']['entity_types']
        )

    async def insert_document(self, text: str):
        """Insert a document asynchronously."""
        return await self.grag.async_insert(text)

    async def retrieve(self, query: str):
        """Retrieve information based on query asynchronously."""
        return await self.grag.async_query(query)

def jupyter_async(coroutine):
    """Execute async code in Jupyter notebooks."""
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coroutine)