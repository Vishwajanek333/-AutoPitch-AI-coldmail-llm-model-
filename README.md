

# AutoPitch — AI Cold Email Generator

AutoPitch AI automatically crafts personalized cold outreach emails by combining scraped job descriptions, your portfolio, and an LLM chain.

## Project summary
- Streamlit UI to enter a job URL and generate a tailored cold email.
- Uses LangChain for LLM orchestration and prompt templates.
- Portfolio data stored in a CSV and optionally a vectorstore (ChromaDB) to match skills to projects.
- Supports multiple embedding backends (ONNX, OpenAI). ONNX may require specific NumPy versions.
- 
## 🏗️ Architecture Diagram

The system architecture for **AutoPitch AI** is illustrated below:

![Architecture Diagram](C:\Users\Vishw\OneDrive\Documents\project_to_add_to_resume\cold_email generator\Architecture.png)

### 🧠 Workflow Summary
1. **Career’s Page** → Job descriptions are scraped from company sites.  
2. **LLM** → Extracts key job fields (title, skills, experience, description) into JSON format.  
3. **Vector Store** → Stores portfolio embeddings for semantic similarity search.  
4. **LLM (Matching Layer)** → Matches job requirements with relevant portfolio links.  
5. **Cold Mail Generator (LLM)** → Crafts a personalized outreach email.  

Result → A context-rich, tailored **cold email** ready to send.

## Repo structure
- app/
  - main.py — Streamlit entrypoint (UI + orchestration)
  - chain.py — LLM wrapper: extract jobs and generate email text
  - portfolio.py — load portfolio, create/query vectorstore
  - utils.py — helpers (clean_text, normalizers)
  - .env — (should be gitignored) contains API keys
- my_portfolile.csv — portfolio data (techstack, links)
- vectorstore/ — persisted chroma DB files (gitignored recommended)
- README.md — this file

## Quick start (Windows / PowerShell)
1. Open PowerShell in project root:
   ```
   cd "C:\Users\Vishw\OneDrive\Documents\project_to_add_to_resume\cold_email generator"
   ```

2. Activate virtual env (you have `.venv`):
   ```
   .\.venv\Scripts\Activate.ps1
   # If blocked:
   # Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
   # .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

   If you don't have requirements.txt:
   ```
   pip install streamlit langchain langchain-community chromadb pandas
   pip install "numpy<2" --force-reinstall
   pip install --force-reinstall onnxruntime
   ```

4. Run the app:
   ```
   streamlit run "app\main.py"
   ```
   Open http://localhost:8501

## Files to edit for API keys / config
Create `.env` (do not commit) or set environment variables:
```
OPENAI_API_KEY=sk-...
GROQ_API_KEY=...
```

## Common errors you faced and fixes

1) SyntaxError from pasted shell commands inside .py
- Symptom: SyntaxError pointing at a line like `.venv\Scripts\Activate.ps1` or `streamlit run ...`
- Cause: Terminal commands copied into Python file.
- Fix: Remove those lines from your .py files. Run them in PowerShell instead.

2) "PathNotFound" / using `cd` on Activate.ps1
- Symptom: PowerShell error when running `cd .\venv\Scripts\Activate.ps1`
- Cause: `cd` expects directories. You attempted to change directory to a file.
- Fix: Run the script instead:
  ```
  .\.venv\Scripts\Activate.ps1
  ```

3) NumPy / ONNXRuntime incompatibility
- Symptom: Tracebacks mentioning "A module that was compiled using NumPy 1.x" or "ImportError: numpy.core.multiarray failed to import" or "AttributeError: _ARRAY_API not found"
- Cause: onnxruntime (or other extension) was built against NumPy 1.x while you have NumPy 2.x installed.
- Fix:
  ```
  pip install --force-reinstall "numpy<2"
  pip install --force-reinstall onnxruntime chromadb
  ```
  OR change embedding backend to one that doesn't import onnxruntime (OpenAIEmbeddings).

4) USER_AGENT warning
- Symptom: "USER_AGENT environment variable not set"
- Fix (temp):
  ```
  $env:USER_AGENT = "cold-email-generator/1.0"
  ```
  Persist:
  ```
  setx USER_AGENT "cold-email-generator/1.0"
  ```

5) Interrupted pip install / missing packages
- Symptom: missing imports in VS Code (reportMissingImports) or runtime import errors
- Fix: Activate `.venv` in VS Code (Select interpreter) and pip install the required packages.

6) Vectorstore persisted files should be gitignored
- Remove vectorstore files from git tracking and add to .gitignore (see below).

## Recommended .gitignore
````text
// filepath: c:\Users\Vishw\OneDrive\Documents\project_to_add_to_resume\cold_email generator\.gitignore
__pycache__/
*.pyc
.venv/
venv/
.env
vectorstore/
*.sqlite3
.ipynb_checkpoints
.vscode/


// filepath: c:\Users\Vishw\OneDrive\Documents\project_to_add_to_resume\cold_email generator\requirements.txt
streamlit
langchain
langchain-community
chromadb
pandas
onnxruntime
"numpy<2"
python-dotenv
.idea/


### some problem arise how to fix it.

🛠️ Troubleshooting Summary (GitHub Copilot Notes)

Below is a summary of errors faced during development and how they were fixed.

🐍 1. SyntaxError: PowerShell/Terminal Commands in main.py

Cause:
Non-Python commands (e.g., streamlit run ..., cd ..., or .\venv\Scripts\Activate.ps1) were pasted into the .py file.

Fix:
Remove all terminal commands from main.py.
Run them separately in PowerShell or your IDE terminal instead.

📁 2. PathNotFound / ObjectNotFound While Activating Virtual Environment

Cause:
Used cd on a file path instead of running the activate script, or targeted the wrong virtual environment.

Fix:
From the project root, run:

cd "C:\Users\Vishw\OneDrive\Documents\project_to_add_to_resume\cold_email generator"
.\venv\Scripts\Activate.ps1


If blocked, enable execution policy:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force

⚙️ 3. NumPy / ONNXRuntime Incompatibility

Error: ImportError or AttributeError when importing chromadb or onnxruntime.
Cause: onnxruntime built for NumPy 1.x while NumPy 2.x is installed.

Fix (with venv active):

pip install --upgrade pip
pip install --force-reinstall "numpy<2"
pip install --force-reinstall onnxruntime chromadb


Restart Streamlit:

streamlit run "app\main.py"


Alternative:
Use an embedding backend that doesn’t rely on ONNX (e.g., OpenAIEmbeddings).

🌐 4. USER_AGENT Warning

Fix:
Temporarily set:

$env:USER_AGENT = "cold-email-generator/1.0"


Or persistently set:

setx USER_AGENT "cold-email-generator/1.0"

📦 5. Interrupted pip install / Missing Dependencies

Cause:
Installation was cancelled or dependencies not fully installed.

Fix (with venv active):

pip install -r requirements.txt


Or install minimal dependencies:

pip install streamlit langchain chromadb onnxruntime openai

⚡ 6. Minimal Commands to Run Once (PowerShell, from Project Root)
cd "C:\Users\Vishw\OneDrive\Documents\project_to_add_to_resume\cold_email generator"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app\main.py

