#!/bin/bash
set -e

pip install uv

# setup up the environment
echo "Running and Loading Environment..."
uv lock
uv sync

# Setup for all agents created for the project
echo "Loading Agents..."
uv run src/smart_agents/searcher.py
uv run src/smart_agents/search_optimiser.py
uv run src/smart_agents/emailer.py
uv run src/smart_agents/writer.py

# loading agents into a library format
echo "Loading Libraries..."
uv pip install -e .

# After loading everything, execute the async_functions file
uv run src/functions/async_functions.py

# Before Running
# chmod +x run.sh