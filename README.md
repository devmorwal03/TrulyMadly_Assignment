# AI Operations Assistant

An AI-powered Operations Assistant built using a **multi-agent architecture** that converts natural language queries into structured plans, executes real APIs, and verifies results.

## Architecture
The system follows a **Planner → Executor → Verifier** flow:

1. **Planner Agent**  
   Uses an LLM to convert user input into a structured JSON plan and select tools.

2. **Executor Agent**  
   Executes the plan by calling real third-party APIs.

3. **Verifier Agent**  
   Validates the output, handles missing data, and formats the final response.

## Integrated APIs
- **GitHub API** – Search repositories and fetch stars & descriptions  
- **OpenWeather API** – Get current weather by city  
- **News API** – Fetch latest news by topic  

## Tech Stack
- Python  
- Streamlit (UI)  
- Groq LLM  
- REST APIs  

## Setup Instructions
```bash
pip install -r requirements.txt
cp .env.example .env
# Add API keys
streamlit run app.py