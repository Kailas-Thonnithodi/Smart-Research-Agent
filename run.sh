#!/bin/bash
set -e

# setup up the environment
echo "Running and Loading Environment..."
uv lock
uv sync

echo "Loading Agents..."
uv run src/smart_agents/agent_properties.py
uv run src/smart_agents/searcher.py
uv run src/smart_agents/search_optimiser.py
uv run src/smart_agents/emailer.py
uv run src/smart_agents/writer.py

echo "Loading Libraries..."
uv pip install -e .

# Before Running
# chmod +x run.sh