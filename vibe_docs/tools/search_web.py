"""
Web search tool using Claude's web search capability
Adapted from data_hive research_tools.py
"""


async def search_web(
    query: str,
    summarize: bool = True,
    mock: bool = False,
    **kwargs
) -> dict:
    """
    Search the web for information.

    Args:
        query: Search query
        summarize: Whether to summarize results
        mock: Return mock data (for testing)

    Returns:
        dict with search results or summary
    """
    if mock:
        return {
            "results": [
                {"title": "Mock Result", "url": "https://example.com", "snippet": "Mock snippet"}
            ],
            "answer": f"Mock answer for: {query}"
        }

    # Import here to avoid circular dependency during testing
    from ai_orchestration import LLMClient

    client = LLMClient()

    messages = [{"role": "user", "content": query}]

    response = await client.ask(
        messages=messages,
        model="claude-sonnet-4-20250514",
        web_search_config={"max_uses": 5},
    )

    return {
        "answer": response.get("response", ""),
        "model": response.get("model", ""),
    }
