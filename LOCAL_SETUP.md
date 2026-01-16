# 💻 Local Development Setup Guide

This guide details exactly how to set up and run the Web-Chat Agent locally on your machine.

## 📋 Prerequisites
- **Python 3.10 or higher** installed.
- **Git** installed.
- An IDE like **VS Code**.

## 🚀 Step-by-Step Execution

### 1. Clone the Repository
Open your terminal (Command Prompt or PowerShell on Windows) and run:
```bash
git clone https://github.com/Mrigank23012023/Web-Chat.git
cd Web-Chat
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies locally.
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
Install all required libraries from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```
*Note: If you are on Windows, you might see a warning about `pysqlite3-binary`. You can safely ignore this as it is only required for Linux/Cloud/Docker environments.*

### 4. Configure API Keys
Create a file named `.env` in the root directory (same folder as `app.py`).
Add your keys inside it:

```ini
# Required for the LLM
GROQ_API_KEY=gsk_your_groq_api_key_here

# Required if using Pinecone (Hybrid/Cloud mode)
PINECONE_API_KEY=pc_your_pinecone_api_key_here

# Optional: Set provider explicitly (defaults to 'chroma' if not set)
# VECTOR_STORE_PROVIDER=pinecone
```
* **Groq API Key**: Get it from [Groq Console](https://console.groq.com/keys)
* **Pinecone API Key**: Get it from [Pinecone Dashboard](https://app.pinecone.io/)

### 5. Run the Application
Start the Streamlit server:
```bash
streamlit run app.py
```

The app should automatically open in your browser at `http://localhost:8501`.

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure you activated the virtual environment (`.venv`) before running `streamlit`. |
| `Connection Refused` on start | Ensure no other app is running on port 8501. Try `streamlit run app.py --server.port 8502`. |
| `sqlite3` error | This app patches sqlite3 automatically. If issues persist, ensure you are not using `pysqlite3` imports manually on Windows. |

## 🧪 Testing
To run the app in "headless" mode (without opening a browser) for testing:
```bash
streamlit run app.py --server.headless true
```
