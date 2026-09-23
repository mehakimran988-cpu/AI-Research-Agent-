```python
import os

from crewai import Agent, Crew, LLM, Process, Task

from src.tools import web_search


MODEL_NAME = "gemini/gemini-3.5-flash"


def create_research_crew() -> Crew:
    """
    Create the single-agent research crew.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY was not found."
        )

    # Create Gemini LLM
    gemini_llm = LLM(
        model=MODEL_NAME,
        api_key=api_key,
    )

    # Create the single research agent
    researcher = Agent(
        role="Senior Research Analyst",

        goal=(
            "Research the given topic using reliable web sources "
            "and produce a factual, balanced, well-structured "
            "research report."
        ),

        backstory=(
            "You are an experienced research analyst. "
            "You investigate topics carefully, compare information "
            "from multiple sources, identify important facts, "
            "avoid unsupported claims, and write clear reports."
        ),

        tools=[web_search],

        llm=gemini_llm,

        verbose=True,

        allow_delegation=False,
    )

    # Create the research task
    research_task = Task(
        description="""
        Research the following topic:

        {topic}

        Search the web and create a high-quality research report.

        Requirements:

        1. Search the web multiple times.
        2. Use multiple sources.
        3. Prefer reliable sources.
        4. Do not invent facts or sources.
        5. Distinguish facts from opinions and predictions.
        6. If sources disagree, explain the disagreement.
        7. Include source URLs.

        Use this report structure:

        # Research Report: [Topic]

        ## Executive Summary

        Summarize the most important findings.

        ## Introduction

        Explain the topic and why it matters.

        ## Key Findings

        Present the major findings.

        ## Detailed Analysis

        Explain the findings in detail.

        ## Important Perspectives

        Discuss relevant perspectives,
        disagreements, limitations, and uncertainties.

        ## Conclusion

        Summarize the main findings.

        ## Sources

        Provide a numbered list of important sources
        with their URLs.

        Return only the final research report.
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

    # Create the crew
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        process=Process.sequential,
        verbose=True,
    )

    return crew
```
