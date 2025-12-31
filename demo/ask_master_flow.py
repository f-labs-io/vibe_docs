"""
Demo: ask_master flow
Shows how Research Manager can ask user for clarification
"""

import asyncio

async def main():
    print("=" * 50)
    print("Ask Master Flow Demo")
    print("=" * 50)

    print("""
This demo shows the ask_master flow:

1. User submits ambiguous query: "Tell me about vibe coding"
2. Research Manager calls ask_master to clarify
3. Execution PAUSES - waiting for user input
4. User responds with clarification
5. Research Manager continues with clarified scope
6. Research Agent performs targeted search
7. Final results returned

The ask_master tool enables human-in-the-loop workflows
where the agent can request clarification or approval
before proceeding.
    """)

if __name__ == "__main__":
    asyncio.run(main())
