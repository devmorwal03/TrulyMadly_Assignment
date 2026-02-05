from tools.github_tool import search_github
from tools.weather_tool import get_weather
from tools.news_tool import get_news

def execute_plan(plan):
    results = {}

    for step in plan.get("steps", []):
        tool = step.get("tool")

        if tool == "github":
            results["github"] = search_github(step.get("query"))

        elif tool == "weather":
            results["weather"] = get_weather(step.get("city"))

        elif tool == "news":
            results["news"] = get_news(step.get("topic", "technology"))

    return results