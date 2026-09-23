```python
from crewai.tools import tool
from ddgs import DDGS


@tool("web_search")
def web_search(query: str) -> str:
    """
    Search the web using DuckDuckGo.

    Args:
        query: The search query.

    Returns:
        Formatted search results containing titles,
        URLs, and descriptions.
    """

    try:

        # -------------------------------------------------
        # Perform web search
        # -------------------------------------------------

        results = DDGS().text(
            query,
            region="us-en",
            safesearch="moderate",
            max_results=8,
        )

        # -------------------------------------------------
        # Check if results exist
        # -------------------------------------------------

        if not results:
            return "No search results were found."

        # -------------------------------------------------
        # Format results
        # -------------------------------------------------

        formatted_results = []

        for index, result in enumerate(
            results,
            start=1
        ):

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

        return (
            "The web search failed. "
            f"Error: {str(e)}"
        )
```
