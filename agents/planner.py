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
- If user asks news -> use news tool
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
    query_lower = user_query.lower()

    if "weather" in query_lower:
        words = user_query.split()
        city = words[-1]
        return {
            "steps": [
                {"tool": "weather", "city": city}
            ]
        }

    if "github" in query_lower or "repo" in query_lower:
        return {
            "steps": [
                {"tool": "github", "query": user_query}
            ]
        }

    if "news" in query_lower:
        return {
            "steps": [
                {"tool": "news", "topic": user_query}
            ]
        }
    
    return {"steps": []}