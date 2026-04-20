# Islamic History Chatbot

A retrieval‑augmented chatbot that answers questions about Islamic history using Wikipedia long‑form historical articles as its knowledge base.

This project downloads major Islamic history pages, stores them locally, and uses them as context for answering user questions.

---

## Reproducing the Project

The repository includes `pyproject.toml` and `uv.lock` so the environment can be reproduced exactly.

### 1. Clone repository

```bash
git clone https://github.com/yourusername/islamic-history-chatbot.git

```

### 2. Install uv

```bash
pip install uv
```

or

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

### 3. Install dependencies (from lockfile)

```bash
uv sync
```

This installs the exact versions defined in `pyproject.toml` and `uv.lock`.

### 4. Add environment variables

Create a `.env` file in the project root:

```bash
touch .env

echo "OPENAI_API_KEY=your_api_key_here" > .env
```

Add any additional variables required by the chatbot.

### 5. Download Islamic history dataset

```bash
uv run python history_downloader.py
```

This will download Wikipedia pages into:

```
history_pages/
```

### 6. Run the chatbot

```bash
uv run python chat_with_wiki.py
```

The chatbot will now answer questions using the downloaded Islamic history dataset.

---

## Overview

The chatbot is designed to answer factual questions about:

* Early Islamic history
* Major caliphates
* Islamic empires
* Political transitions
* Historical regions
* Islamic Golden Age

The knowledge base is built by downloading full Wikipedia articles and using them for retrieval‑based question answering.

---

## Knowledge Sources

The chatbot currently uses the following core history articles:

* History of Islam
* Rashidun Caliphate
* Umayyad Caliphate
* Abbasid Caliphate
* Islamic Golden Age
* Ottoman Empire
* Mamluk Sultanate (Cairo)
* Al-Andalus
* Fatimid Caliphate
* Ayyubid dynasty

These are downloaded locally and used as the dataset.

---

## Data Collection Script

The dataset is generated using `wikipediaapi`.

The script downloads long‑form history pages and saves them as text files.

```python
import wikipediaapi
import os

history_topics = [
    "History of Islam",
    "Rashidun Caliphate",
    "Umayyad Caliphate",
    "Abbasid Caliphate",
    "Islamic Golden Age",
    "Ottoman Empire",
    "Mamluk Sultanate (Cairo)",
    "Al-Andalus",
    "Fatimid Caliphate",
    "Ayyubid dynasty"
]

def download_history():
    wiki = wikipediaapi.Wikipedia(
        user_agent="IslamicHistoryBot/1.0 (contact@example.com)",
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    folder = "./history_pages"
    os.makedirs(folder, exist_ok=True)
    
    for topic in history_topics:
        page = wiki.page(topic)
        
        if page.exists():
            filename = topic.replace(" ", "_") + ".txt"
            path = os.path.join(folder, filename)
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(page.text)

if __name__ == "__main__":
    download_history()
```

---

## Output Structure

After running the script:

```
history_pages/
 ├── History_of_Islam.txt
 ├── Rashidun_Caliphate.txt
 ├── Umayyad_Caliphate.txt
 ├── Abbasid_Caliphate.txt
 ├── Islamic_Golden_Age.txt
 ├── Ottoman_Empire.txt
 ├── Mamluk_Sultanate_(Cairo).txt
 ├── Al-Andalus.txt
 ├── Fatimid_Caliphate.txt
 └── Ayyubid_dynasty.txt
```

These files are used as the chatbot knowledge base.

---

## How It Works

1. Wikipedia pages downloaded
2. Text files stored locally
3. Files loaded into retriever
4. Relevant chunks selected
5. LLM generates grounded answer

Pipeline:

```
User Question
     ↓
Retriever (history_pages)
     ↓
Relevant Context
     ↓
LLM
     ↓
Answer
```

---

## Installation (uv)

This project uses uv for reproducible environments.

Initialize project:

```bash
uv init
```

Create virtual environment:

```bash
uv venv
```

Activate:

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:


---

## Reproducibility

To ensure reproducible builds:

1. Commit `pyproject.toml`
2. Commit `uv.lock`
3. Pin dependency versions
4. Use uv for all installs

Install exact locked dependencies:

```bash
uv sync
```

This guarantees:

* Same dependency versions
* Same dataset behavior
* Same parsing results
* Same chatbot outputs (given same model)

---

## Running Dataset Download

```bash
uv run python history_downloader.py
```

---

## Example Questions

* Who were the Rashidun caliphs?
* What caused the Abbasid revolution?
* What was Al-Andalus?
* When did the Ottoman Empire start?
* What was the Islamic Golden Age?
* Who ruled after the Umayyads?
* What was the Fatimid Caliphate?

---

## Design Goals

* Grounded historical answers
* Minimal hallucination
* Simple dataset
* Offline knowledge base
* Expandable topic list

---

## Expanding the Dataset

Add more topics to `history_topics`:

```python
history_topics = [
    "Seljuk Empire",
    "Delhi Sultanate",
    "Mughal Empire",
    "Timurid Empire"
]
```

Then rerun the script.

---

## Limitations

* Based only on selected Wikipedia pages
* No citations yet
* English only
* No scholar biographies
* No hadith/fiqh history yet

---

## Future Improvements

* Add more empires
* Add scholar biographies
* Add timeline indexing
* Add citations
* Add Arabic sources
* Add embeddings + vector search
* Add mobile app UI

---

## License

MIT

---

## Disclaimer

This chatbot provides historical summaries based on Wikipedia content. Historical interpretations may vary. Always verify critical information with primary sources.
