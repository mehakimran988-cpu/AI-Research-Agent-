```python
from crewai.tools import tool
from ddgs import DDGS


@tool("web_search")
def web_search(query: str) -> str:
    """
    Search the web using DuckDuckGo.

    Args:
        query: Search query.

    Returns:
        Formatted web search results.
    """

    try:
        results = DDGS().text(
            query,
            region="us-en",
            safesearch="moderate",
            max_results=8,
        )

        if not results:
            return "No search results were found."

        formatted_results = []

        for index, result in enumerate(results, start=1):

            title = result.get(
                "title",
                "No title"
            )

            url = result.get(
                "href",
                ""
            )

            body = result.get(
                "body",
                "No description available."
            )

            formatted_results.append(
                f"""
SOURCE {index}

Title:
{title}

URL:
{url}

Summary:
{body}
"""
            )

        return "\n".join(formatted_results)

    except Exception as e:

        return f"Search failed: {str(e)}"
```
