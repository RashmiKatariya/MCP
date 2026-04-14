# 🚀 AI Agent MCP-style Server

A lightweight implementation of a Model Context Protocol (MCP)-style server using FastAPI.  
This project enables AI agents to perform real-world actions via structured tool APIs.

---

## 🧠 What is this?

Traditional AI models can only respond with text.  
This project extends AI capabilities by allowing it to:

- Call tools
- Perform actions
- Interact with real-world systems

---

## 🔧 Features

- ➕ Math Tools  
  - Add numbers  
  - Multiply values  

- 📂 File Operations  
  - Read files  
  - Write files  

- 🌐 External API Integration  
  - Fetch real-time weather data  

---

## 🏗️ Architecture
User → AI Agent → MCP-style Server → Tools → Actions → Response


This mimics how modern AI agents (like ChatGPT plugins, LangChain agents) interact with external systems.

---

## ⚙️ Tech Stack

- Python
- FastAPI
- Uvicorn
- Requests

---

## ▶️ How to Run

### 1. Clone Repository

git clone https://github.com/your-username/mcp-ai-agent.git
cd mcp-ai-agent

### 2. Create Virtual Environment
 
python -m venv venv
venv\Scripts\activate   # Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Start Server
uvicorn server:app --reload

### 5. Open API Docs
http://127.0.0.1:8000/docs

Interactive UI to test all tools 🚀

### 6.Test Client
python client/test_client.py

🔍 Example API Calls
Add Numbers
POST /tools/add
{
  "a": 5,
  "b": 10
}

Get Weather
POST /tools/get_weather
{
  "city": "Bangalore"
}


📌 Use Cases
  AI Agents performing real-world actions
  Workflow automation
  Tool-based LLM systems
  Backend for autonomous agents

🚀 Future Improvements
  🤖 OpenAI / LLM integration
  🔐 Authentication & security
  ☁️ Cloud deployment (AWS / Render)
  📊 Logging & monitoring
  
💡 Key Concept

This project demonstrates how:

AI → chooses tool → calls API → executes action → returns result

👨‍💻 Author

Built as part of an AI systems project to explore tool-augmented intelligence and MCP architecture.
