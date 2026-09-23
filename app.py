```python
import os

import streamlit as st
from dotenv import load_dotenv

from src.agent import create_research_crew


# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------

load_dotenv()


# ---------------------------------------------------------
# Streamlit page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔎",
    layout="wide",
)


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

def get_api_key() -> str:
    """
    Get the Gemini API key.

    Locally:
        Reads GEMINI_API_KEY from .env

    Streamlit Cloud:
        Reads GEMINI_API_KEY from Streamlit Secrets
    """

    # Try Streamlit Cloud secrets first
    try:
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

    # Fall back to local .env
    return os.getenv("GEMINI_API_KEY", "")


def run_research(topic: str) -> str:
    """
    Create the CrewAI crew and run the research task.
    """

    crew = create_research_crew()

    result = crew.kickoff(
        inputs={
            "topic": topic
        }
    )

    return result.raw


# ---------------------------------------------------------
# Application UI
# ---------------------------------------------------------

st.title("🔎 AI Research Agent")

st.markdown(
    """
    ### Research any topic with AI

    Enter a topic below. The AI research agent will search the web,
    analyze the information it finds, and generate a structured
    research report.
    """
)

st.divider()


topic = st.text_input(
    "Research Topic",
    placeholder="Example: Impact of artificial intelligence on education",
)


research_button = st.button(
    "🚀 Start Research",
    type="primary",
)


# ---------------------------------------------------------
# Run research
# ---------------------------------------------------------

if research_button:

    # Check topic
    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    # Check API key
    api_key = get_api_key()

    if not api_key:
        st.error(
            "Gemini API key was not found. "
            "Please add GEMINI_API_KEY to your .env file "
            "or Streamlit Cloud Secrets."
        )
        st.stop()

    # Make the key available to CrewAI
    os.environ["GEMINI_API_KEY"] = api_key

    # Run the agent
    with st.spinner(
        "🔍 Researching your topic... "
        "This may take a little while."
    ):

        try:

            report = run_research(topic)

            st.success("✅ Research completed!")

            st.divider()

            # Display report
            st.markdown(report)

            st.divider()

            # Download report
            st.download_button(
                label="⬇️ Download Report",
                data=report,
                file_name="research_report.md",
                mime="text/markdown",
            )

        except Exception as e:

            st.error(
                "Something went wrong while generating the report."
            )

            st.exception(e)
```
