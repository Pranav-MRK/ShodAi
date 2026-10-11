from typing import Annotated
from typing_extensions import TypedDict

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


class ResearchState(TypedDict):
    question: str
    plan: str
    messages: Annotated[list[AnyMessage], add_messages]
    sources: list[dict]
    findings: str
    verification: str
    verification_decision: str
    research_iterations: int