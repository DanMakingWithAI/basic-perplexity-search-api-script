import requests

PERPLEXITY_API_KEY = "pplx-xxxyyyzzz111222333etc"

def perplexity_search(
  query: str,
  max_results: int = 5,
  max_tokens_per_page: int = None,
  country: str = None
) -> dict:
    """
    Perform a search query using the Perplexity API via HTTP POST request.

    Args:
        query (str): The search query string. Required.
        max_results (int): The number of results to return. Optional. Default is 5 if omitted.
        max_tokens_per_page (int): The number of tokens to return per search result. Optional. Default is 1024 if omitted.
        country (str): For location-specific searches, choose "GB" for close to the user, or whatever country code is applicable if explicitly directed by the user. Optional. Omit if results are not geographic location-specific.
    Returns:
        dict: A dictionary containing the search results and metadata.
    """
    url = "https://api.perplexity.ai/search"
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": query
    }
    if max_results is not None:
        payload["max_results"] = max_results
    if max_tokens_per_page is not None:
        payload["max_tokens_per_page"] = max_tokens_per_page
    if country is not None:
        payload["country"] = country

    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
