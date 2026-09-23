import os

import streamlit as st
from dotenv import load_dotenv

from src.agent import create_research_crew


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

load_dotenv()


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

    Works locally with .env and on Streamlit Cloud
    with Streamlit secrets.
    """

    try:
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

    return os.getenv("GEMINI_API_KEY", "")


def run_research(topic: str) -> str:
    """
    Run the CrewAI research crew.
    """

    crew = create_research_crew()

    result = crew.kickoff(
        inputs={
            "topic": topic
        }
    )

    return result.raw


# ---------------------------------------------------------
# UI
# ---------------------------------------------------------

st.title("🔎 AI Research Agent")

st.markdown(
    """
    Enter a research topic and the AI Research Agent will search
    the web and generate a structured research report.
    """
)


topic = st.text_input(
    "Research topic",
    placeholder="Example: Impact of artificial intelligence on education",
)


research_button = st.button(
    "🚀 Start Research",
    type="primary",
)


if research_button:

    if not topic.strip():
        st.warning("Please enter a research topic.")

        st.stop()

    api_key = get_api_key()

    if not api_key:
        st.error(
            "Gemini API key not found. "
            "Add GEMINI_API_KEY to your .env file locally "
            "or Streamlit Cloud Secrets."
        )

        st.stop()

    # Make the key available to CrewAI.
    os.environ["GEMINI_API_KEY"] = api_key

    with st.spinner(
        "Researching the topic. This may take a little while..."
    ):

        try:

            report = run_research(topic)

            st.success("Research completed!")

            st.markdown("---")

            st.markdown(report)

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
