import json
import os
import requests

def search_api(query: str, search_depth: str = 'basic', include_domains: list[str] = None, max_results: int = 5) -> str:
    """
    Performs a high-precision, parameter-controlled web search using the Tavily API.
    
    Args:
        query (str): The search query.
        search_depth (str): The depth of the search ('basic' or 'advanced').
        include_domains (list[str], optional): A list of specific domains to restrict search to (e.g. ['reddit.com', 'github.com']).
        max_results (int): The maximum number of results to return.
        
    Returns:
        str: A JSON-formatted string containing the search results or an error message.
    """
    api_key = os.getenv("TAVILY_API_KEY")
    
    if not api_key:
        return json.dumps({
            "error": "Missing TAVILY_API_KEY. Please add it to your .env file and run /reset."
        })

    url = "https://api.tavily.com/search"
    
    # Prepare the payload
    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": search_depth,
        "max_results": max_results,
    }
    
    if include_domains:
        payload["include_domains"] = include_domains

    try:
        response = requests.post(url, json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        # Format the results for the LLM to digest efficiently
        formatted_results = []
        for result in data.get("results", []):
            formatted_results.append({
                "title": result.get("title"),
                "url": result.get("url"),
                "content": result.get("content")
            })
            
        return json.dumps({
            "status": "success",
            "query": query,
            "results": formatted_results
        }, indent=2)

    except requests.exceptions.RequestException as e:
        return json.dumps({
            "error": f"API request failed: {str(e)}"
        })
    except Exception as e:
        return json.dumps({
            "error": f"An unexpected error occurred: {str(e)}"
        })

# Test block (optional)
if __name__ == "__main__":
    # This allows you to test the script manually from the terminal
    print("Running local test...")
    print(search_api("test query", max_results=1))
