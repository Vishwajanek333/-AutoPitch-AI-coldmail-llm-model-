# -AutoPitch-AI-coldmail-llm-model-
AutoPitch AI  Automatically crafts personalized pitches for cold outreach.

# AutoPitch — AI Cold Email Generator

AutoPitch AI automatically crafts personalized cold outreach emails by combining scraped job descriptions, your portfolio, and an LLM chain.

## Project summary
- Streamlit UI to enter a job URL and generate a tailored cold email.
- Uses LangChain for LLM orchestration and prompt templates.
- Portfolio data stored in a CSV and optionally a vectorstore (ChromaDB) to match skills to projects.
- Supports multiple embedding backends (ONNX, OpenAI). ONNX may require specific NumPy versions.

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


GitHub Copilot

Summary of errors you faced and how to fix them (concise)

SyntaxError: you had PowerShell/terminal commands inside main.py
Cause: lines like streamlit run ..., cd ..., or .\venv\Scripts\Activate.ps1 were pasted into the .py file.
Fix: remove any non‑Python lines from main.py. Run those commands in PowerShell/terminal instead.
PathNotFound / ObjectNotFound when using cd on Activate.ps1
Cause: you used cd on a file path instead of running the activate script, or targeted the wrong venv folder.
Fix: from project root run:
cd "C:\Users\Vishw\OneDrive\Documents\project_to_add_to_resume\cold_email generator"
Activate.ps1
If blocked: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
NumPy / onnxruntime incompatibility (ImportError / AttributeError) when chromadb imports ONNX embedding
Cause: onnxruntime or other native wheels were built for NumPy 1.x; you have NumPy 2.x.
Fix (with venv active):
pip install --upgrade pip
pip install --force-reinstall "numpy<2"
pip install --force-reinstall onnxruntime chromadb
Then restart Streamlit: streamlit run "app\main.py"
Alternative: change portfolio to use an embedding backend that does not import onnxruntime (e.g., OpenAIEmbeddings).
USER_AGENT warning
Fix: set env var temporarily in PowerShell:
$env:USER_AGENT = "cold-email-generator/1.0"
or persistently: setx USER_AGENT "cold-email-generator/1.0"
Interrupted pip install / missing deps
Cause: you cancelled pip install; some packages are missing.
Fix: with venv active run: pip install -r requirements.txt (or install the minimal list shown below).
Minimal commands to run once (PowerShell, from project root)
