"""
Demo: Multi-step research
Shows Research Manager coordinating multiple research tasks
"""

import asyncio

async def main():
    print("=" * 50)
    print("Multi-Step Research Demo")
    print("=" * 50)

    print("""
This demo shows multi-step research flow:

Query: "Research Claude Code:
        1. What is it?
        2. Main features?
        3. Compare to GitHub Copilot"

Flow:
1. Research Manager receives complex query
2. Calls ask_master to approve research plan
3. Delegates part 1 to Research Agent -> gets results
4. Delegates part 2 to Research Agent -> gets results
5. Delegates part 3 to Research Agent -> gets results
6. Synthesizes all results
7. Handoffs comprehensive answer

This shows the orchestration handling multiple
sequential research tasks with result synthesis.
    """)

if __name__ == "__main__":
    asyncio.run(main())
