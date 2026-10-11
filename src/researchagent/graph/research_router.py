MAX_RESEARCH_ITERATIONS = 3


def research_router(state):

    last_message = state["messages"][-1]

    iterations = state.get("research_iterations", 0)

    # ------------------------------------------------
    # Safety limit
    # ------------------------------------------------

    if iterations >= MAX_RESEARCH_ITERATIONS:
        print("🛑 Maximum research iterations reached")
        return "research_done"

    # ------------------------------------------------
    # Did researcher request a tool?
    # ------------------------------------------------

    tool_calls = getattr(last_message, "tool_calls", None)

    if not tool_calls:
        print("✅ Researcher has enough evidence")
        return "research_done"

    # ------------------------------------------------
    # Collect previous research_search queries
    # ------------------------------------------------

    previous_queries = set()

    for message in state["messages"][:-1]:

        previous_tool_calls = getattr(
            message,
            "tool_calls",
            None
        )

        if not previous_tool_calls:
            continue

        for tool_call in previous_tool_calls:

            if tool_call.get("name") != "research_search":
                continue

            args = tool_call.get("args", {})

            query = args.get("query")

            if query:
                previous_queries.add(query)

    # ------------------------------------------------
    # Check current tool calls
    # ------------------------------------------------

    for tool_call in tool_calls:

        tool_name = tool_call.get("name")

        if tool_name != "research_search":
            continue

        args = tool_call.get("args", {})

        query = args.get("query")

        print(f"🔎 Requested research query: {query}")

        if query in previous_queries:

            print("⚠️ DUPLICATE RESEARCH QUERY")
            print(f"   Query: {query}")
            print("🛑 Blocking duplicate tool call")

            return "research_done"

    print("🛠️ Researcher requested a new tool")

    return "research_tools"