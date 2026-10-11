MAX_RESEARCH_ITERATIONS = 3


def verification_router(state):
    decision = state.get("verification_decision", "")
    iterations = state.get("research_iterations", 0)

    print("\n🔀 VERIFICATION ROUTER")
    print(f"Decision: {decision}")
    print(f"Research iterations: {iterations}")

    if decision == "NEEDS_MORE_RESEARCH":

        if iterations >= MAX_RESEARCH_ITERATIONS:
            print("🛑 Maximum research iterations reached")
            print("➡️ Proceeding to agent")
            return "pass"

        print("🔁 Verifier requested more research")
        return "needs_more_research"

    print("✅ Verification passed")
    return "pass"