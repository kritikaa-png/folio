import requests
import json

USERNAME = "kritikaa-png"

url = f"https://api.github.com/users/{USERNAME}/repos"

repos = requests.get(url).json()

projects = []

for repo in repos:
    projects.append({
        "name": repo["name"],
        "description": repo["description"],
        "url": repo["html_url"],
        "stars": repo["stargazers_count"]
    })

with open("projects.json", "w") as f:
    json.dump(projects, f, indent=4)

print("projects.json updated")