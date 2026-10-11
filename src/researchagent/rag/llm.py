import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

load_dotenv()


def get_llm(provider: str | None = None):

    provider = provider or os.getenv("SHOD_LLM_PROVIDER", "ollama")

    # ---------------- Ollama ----------------
    if provider == "ollama":
        return ChatOllama(
            model="llama3.2:3b",
            temperature=0,
        )

    # ---------------- Groq ----------------
    if provider == "groq":
        return ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY"),  # type: ignore
        )

    # ---------------- Gemini ----------------
    if provider == "gemini":
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
        )

    raise ValueError(f"Unsupported LLM provider: {provider}")