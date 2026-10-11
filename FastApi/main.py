from fastapi import FastAPI
from FastApi.schema import Research_response,ResearchRequest
from FastApi.service import run_researchagent
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from FastApi.streaming import stream_research

app = FastAPI(
    title="Shod Ai",
    description="AI Research Agent API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/research/stream")
def research_stream(request: ResearchRequest):

    return StreamingResponse(
        stream_research(
            question=request.question,
            thread_id=request.thread_id,
        ),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )

@app.get("/")
def root():
    return{
        "Shod running....."
    }

@app.get("/health")
def health():
    return {
        "status":"health"
    }


@app.post("/research", response_model=Research_response)
def research(request: ResearchRequest):

    print("\n" + "=" * 60)
    print("FASTAPI /research")
    print("QUESTION:", request.question)
    print("THREAD:", request.thread_id)

    result = run_researchagent(
        question=request.question,
        thread_id=request.thread_id,
    )

    print("GRAPH RESULT:")
    print(result)
    print("=" * 60)

    return result