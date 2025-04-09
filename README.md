
# Caching Service (Python)

## Description
A simple in-memory caching service with LRU eviction policy. Evicted items are stored in a simulated database (in-memory dictionary).

## Features
- Configurable maximum cache size
- LRU-based eviction
- APIs: add, remove, get, removeAll, clear
- Logging and exception handling
- Unit tested with 'unittest'

## Setup
```bash
git clone <your_repo_url>
cd caching_service
pip install -r requirements.txt
```

## Running Tests
'''bash
pytest
'''

## Folder Structure
- 'cache/': Core implementation
- 'tests/': Unit tests
- 'logs/': Log output
