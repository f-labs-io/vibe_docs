"""
Demo: Simple research query
Shows basic flow: user -> research_manager -> research_agent -> result
"""

import asyncio
from pathlib import Path

async def main():
    # Note: In real usage, ai-orchestration would be installed
    # For demo purposes, we show the intended usage pattern

    print("=" * 50)
    print("Simple Research Demo")
    print("=" * 50)

    print("""
This demo shows the basic flow:
1. User submits query to Research Manager
2. Research Manager delegates to Research Agent
3. Research Agent searches the web
4. Results flow back to user

Example usage (when ai-orchestration is installed):

    from ai_orchestration import Orchestrator
    from vibe_docs.agents import build_research_manager_config, build_research_agent_config
    from vibe_docs.tools import search_web

    orch = Orchestrator(logs_dir="./logs")
    orch.agent.create(**build_research_manager_config())
    orch.agent.create(**build_research_agent_config())
    orch.register_tool(name="search_web", ...)

    result = await orch.run("research_manager", "What is vibe coding?")
    """)

if __name__ == "__main__":
    asyncio.run(main())
