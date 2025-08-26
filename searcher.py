import os
import requests


def search_serpapi(query):
    api_key = os.getenv("SERPAPI_KEY")
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key
    }
    res = requests.get("https://serpapi.com/search", params=params).json()
    results = res.get("organic_results", [])
    return "\n\n".join([f"🔗 {r['title']}\n{r['link']}" for r in results[:5]]) or "❌ No results."
