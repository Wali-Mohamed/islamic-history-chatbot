Athar Project: Local RAG Setup Summary
1. Environment Setup
• Python (uv): Manages libraries in `.venv`.

  • `llama-index-core` (Orchestrator)

  • `llama-index-embeddings-huggingface` (Local search/embeddings)

  • `llama-index-llms-ollama` (Local brain connector)

• System (WSL):

  • `zstd`: Required for extraction.

  • `Ollama`: The background engine (installed via `curl -fsSL https://ollama.com/install.sh | sh`).

2. Core Components
• Embeddings: `BAAI/bge-small-en-v1.5` (Runs locally via HuggingFace).

• LLM: `llama3` (Runs locally via Ollama).

• Data: Wikipedia `.md` files in `./wiki_pages`.

3. Execution Workflow
1. Start Engine: Open a terminal and run `ollama serve`.

2. Download Model: `ollama pull llama3`.

3. Run App: `uv run python chat_with_wiki.py`.

4. Cleanup/Uninstallation
• Project/Libs: `rm -rf ~/athar-project`

• AI Models (Space): `rm -rf ~/.ollama`

• Ollama App: `sudo rm $(which ollama)`

• System Tools: `sudo apt remove zstd`