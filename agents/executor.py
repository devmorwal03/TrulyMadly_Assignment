from tools.github_tool import search_github
from tools.weather_tool import get_weather

def execute_plan(plan):
    results = {}

    for step in plan.get("steps", []):
        tool = step.get("tool")

        if tool == "github":
            results["github"] = search_github(step.get("query"))

        elif tool == "weather":
            results["weather"] = get_weather(step.get("city"))

    return results