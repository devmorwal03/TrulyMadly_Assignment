import json
from llm.llm_client import call_llm

def create_plan(user_query):

    prompt = f"""
You are a planning agent.

Convert the user request into STRICT JSON.
Do NOT write anything except JSON.
Do NOT explain.

Available tools:
1. github → needs: query
2. weather → needs: city
2. news -> needs: topic

Rules:
- If user asks weather → use weather tool
- If user asks github/repos/code → use github tool
- If user aks news → get news by topic (needs "topic")
- Always produce valid JSON
- Never return empty steps

JSON format:
{{
  "steps":[
    {{"tool":"weather","city":"city_name"}}
  ]
}}

User request: {user_query}
"""

    response = call_llm(prompt)
    # Try parsing LLM JSON
    try:
        plan = json.loads(response)
        if plan.get("steps"):
            return plan
    except:
        pass

    # Fallback rule-based (guaranteed execution)
    return {"steps": []}