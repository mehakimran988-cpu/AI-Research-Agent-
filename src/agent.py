```python
import os

from crewai import Agent, Crew, LLM, Process, Task

from src.tools import web_search


# ---------------------------------------------------------
# Gemini configuration
# ---------------------------------------------------------

MODEL_NAME = "gemini/gemini-3.5-flash"


# ---------------------------------------------------------
# Create CrewAI research crew
# ---------------------------------------------------------

def create_research_crew() -> Crew:
    """
    Create the single-agent research crew.
    """

    # Get Gemini API key
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY environment variable was not found."
        )

    # -----------------------------------------------------
    # Create Gemini LLM
    # -----------------------------------------------------

    gemini_llm = LLM(
        model=MODEL_NAME,
        api_key=api_key,
        temperature=0.2,
    )

    # -----------------------------------------------------
    # Create research agent
    # -----------------------------------------------------

    researcher = Agent(
        role="Senior Research Analyst",

        goal=(
            "Research the given topic using reliable web sources "
            "and produce a factual, balanced, well-structured "
            "research report."
        ),

        backstory=(
            "You are an experienced research analyst who specializes "
            "in investigating topics using information from the web. "
            "You carefully compare information from multiple sources, "
            "identify important facts, avoid unsupported claims, "
            "and write clear and useful research reports."
        ),

        tools=[
            web_search
        ],

        llm=gemini_llm,

        verbose=True,

        allow_delegation=False,
    )

    # -----------------------------------------------------
    # Create research task
    # -----------------------------------------------------

    research_task = Task(

        description="""
        Conduct thorough research on the following topic:

        {topic}

        Your job is to create a high-quality research report
        based on information discovered through web searches.

        Follow these requirements:

        1. Search the web multiple times.

        2. Use different search queries when appropriate.

        3. Use multiple sources instead of relying on a single source.

        4. Prefer reliable sources such as:
           - Government websites
           - Universities
           - Research institutions
           - Official organizations
           - Peer-reviewed research
           - Established news organizations
           - Reputable industry organizations

        5. Do not invent statistics, studies, quotations,
           facts, or sources.

        6. Clearly distinguish factual information from opinions,
           predictions, or interpretations.

        7. If reliable sources disagree, explain the disagreement.

        8. Include URLs for the important sources used.

        9. Focus on information that is relevant to the research topic.

        10. Write the final report using Markdown.

        Use this structure:

        # Research Report: [Topic]

        ## Executive Summary

        Provide a concise summary of the most important findings.

        ## Introduction

        Explain the topic and why it is important.

        ## Key Findings

        Present the major findings discovered during the research.

        ## Detailed Analysis

        Explain the important findings in greater detail.

        ## Important Perspectives

        Discuss relevant perspectives, disagreements,
        limitations, or uncertainties.

        ## Conclusion

        Summarize the main findings without introducing
        unsupported new information.

        ## Sources

        Provide a numbered list of important sources.
        Include the source title and URL.

        The final response must be a polished research report.

        Do not describe your internal reasoning or research process.
        """,

        expected_output="""
        A polished Markdown research report containing:

        - Executive Summary
        - Introduction
        - Key Findings
        - Detailed Analysis
        - Important Perspectives
        - Conclusion
        - Sources with URLs
        """,

        agent=researcher,
    )

    # -----------------------------------------------------
    # Create Crew
    # -----------------------------------------------------

    crew = Crew(
        agents=[
            researcher
        ],

        tasks=[
            research_task
        ],

        process=Process.sequential,

        verbose=True,
    )

    return crew
```
