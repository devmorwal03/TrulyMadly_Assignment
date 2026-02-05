import requests

def search_github(query):
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page=3"
    res = requests.get(url).json()

    results = []
    for repo in res.get("items", []):
        results.append({
            "name": repo["name"],
            "url": repo["html_url"],
            "stars": repo["stargazers_count"],
            "description": repo["description"]
        })

    return results