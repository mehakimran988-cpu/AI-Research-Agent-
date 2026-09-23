# AI-Research-Agent-
# 🔎 AI Research Agent

A beginner-friendly AI research agent built with Python, CrewAI, Gemini 3.5 Flash, DuckDuckGo search, and Streamlit.

The application accepts a research topic, searches the web, analyzes the information, and generates a structured research report.

---

## 🧰 Technologies

* Python 3.12
* CrewAI
* Gemini 3.5 Flash
* DDGS / DuckDuckGo
* Streamlit
* python-dotenv

---

## 🏗️ Architecture

```text
User
 │
 ▼
Streamlit
 │
 ▼
CrewAI
 │
 ▼
Single Research Agent
 │
 ├──────────────► DDGS / DuckDuckGo
 │                       │
 │                       ▼
 │                  Search Results
 │
 ▼
Gemini 3.5 Flash
 │
 ▼
Research Report
 │
 ├── Display
 │
 └── Download
```

---

## 📁 Project Structure

```text
ai-research-agent/
│
├── .streamlit/
│   └── config.toml
│
├── src/
│   ├── __init__.py
│   ├── agent.py
│   └── tools.py
│
├── .env.example
├── .gitignore
├── README.md
├── app.py
└── requirements.txt
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-research-agent.git
```

Move into the project:

```bash
cd ai-research-agent
```

---

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install --upgrade pip
```

Then:

```bash
pip install -r requirements.txt
```

---

### 4. Create your `.env` file

Copy `.env.example` and create:

```text
.env
```

Add your Gemini API key:

```text
GEMINI_API_KEY=your_actual_api_key
```

Never commit `.env` to GitHub.

---

### 5. Start Streamlit

Run:

```bash
streamlit run app.py
```

The application should open in your browser.

Usually the local address is:

```text
http://localhost:8501
```

---

## 🔍 How the Agent Works

The user enters a research topic.

For example:

```text
Impact of artificial intelligence on education
```

Streamlit sends the topic to CrewAI.

CrewAI creates one research agent.

The agent has access to a custom tool called:

```text
web_search
```

The tool searches the web using DDGS.

The agent analyzes the search results and creates a Markdown research report using Gemini 3.5 Flash.

---

## 🤖 Agent

This project intentionally uses only one agent.

The agent acts as:

```text
Senior Research Analyst
```

Its responsibilities are:

1. Search the web.
2. Examine multiple sources.
3. Identify useful information.
4. Compare information.
5. Produce a structured report.
6. Include source URLs.

---

## 🌐 Web Search

The project uses the DDGS Python package for web search.

No separate paid search API is required for the basic implementation.

Search availability and rate limits can depend on the underlying search providers.

---

## 🔐 Environment Variables

The application requires:

```text
GEMINI_API_KEY
```

For local development, use:

```text
.env
```

For Streamlit Community Cloud, configure the key using Streamlit Secrets.

---

## ☁️ Deploy to Streamlit Community Cloud

Push the project to GitHub.

Then create a new application on Streamlit Community Cloud.

Select:

```text
Repository:
YOUR_USERNAME/ai-research-agent
```

Set the main file to:

```text
app.py
```

Use Python:

```text
3.12
```

Add the following secret:

```toml
GEMINI_API_KEY = "your_actual_api_key"
```

Then deploy the application.

---

## 🔒 Security

Never put your actual API key inside:

* `app.py`
* `agent.py`
* `tools.py`
* `README.md`
* GitHub commits

Never commit:

```text
.env
```

The `.gitignore` file already excludes `.env`.

---

## 🧪 Example Research Topics

Try topics such as:

```text
Impact of artificial intelligence on education
```

```text
Renewable energy trends
```

```text
History of the internet
```

```text
How electric vehicles work
```

```text
Benefits and challenges of remote work
```

---

## 📌 Current Limitations

This first version intentionally keeps the architecture simple.

The search tool returns search-result information rather than building a sophisticated web crawler.

Future versions could add:

* Full webpage extraction
* Better citation verification
* PDF reports
* Research history
* Academic paper search
* News search
* Source-quality checking
* Research depth controls
* Multiple agents

---

## 📚 Learning Goals

This project is designed to teach the fundamentals of an AI agent application:

```text
Python
  ↓
LLM
  ↓
CrewAI Agent
  ↓
Tools
  ↓
Web Search
  ↓
Streamlit
  ↓
GitHub
  ↓
Cloud Deployment
```

---

## 📄 License

This project is provided for educational purposes.
