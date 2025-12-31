#!/usr/bin/env python3
"""
Demo: ask_master flow
Shows how Research Manager can ask user for clarification
"""

import asyncio
import sys
from pathlib import Path

# Add paths for local packages
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "ai-orchestration"))
sys.path.insert(0, str(Path(__file__).parent.parent))

from ai_orchestration import Orchestrator
from vibe_docs.agents import build_research_manager_config, build_research_agent_config


async def main():
    print("=" * 60)
    print("  Ask Master Flow Demo")
    print("  Human-in-the-loop with ask_master tool")
    print("=" * 60)
    print()

    # Create orchestrator
    logs_dir = Path("./demo_runs")
    orch = Orchestrator(logs_dir=logs_dir, default_model="claude-sonnet-4-20250514")

    # Register agents
    print("[SETUP] Registering agents...")
    manager_config = build_research_manager_config()
    agent_config = build_research_agent_config()

    orch.agent.create(
        id=manager_config["agent_id"],
        describe=manager_config["description"],
        instructions=manager_config["instructions"],
        tools=manager_config["tools"],
        model=manager_config.get("force_model"),
    )
    orch.agent.create(
        id=agent_config["agent_id"],
        describe=agent_config["description"],
        instructions=agent_config["instructions"],
        tools=agent_config["tools"],
        model=agent_config.get("force_model"),
    )
    print(f"  - research_manager")
    print(f"  - research_agent")

    # Register tools
    print("[SETUP] Registering tools...")

    orch.register_tool(
        name="search_web",
        description="Search the web for information",
        input_schema={
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"}
            },
            "required": ["query"]
        },
        handler=lambda x: {"result": f"Web search for: {x.get('query', '')}"},
    )
    # Note: route_to_research_agent is auto-registered when research_agent is created

    print("  - search_web")
    print("  - route_to_research_agent (auto-registered)")
    print()

    # Ambiguous query that should trigger ask_master
    query = "Tell me about AI"
    print(f"[START] Ambiguous query: '{query}'")
    print("        (This may trigger ask_master for clarification)")
    print("-" * 60)
    print()

    # Start research
    result = await orch.start_root_task(
        task=query,
        main_agent="research_manager",
        initiator="human",
    )

    # Check for human tasks (ask_master)
    ready_tasks = orch.graph_ops.get_ready_tasks()
    human_tasks = [
        tid for tid in ready_tasks
        if orch.graph_ops.modal.nodes[tid].agent_id == "human"
    ]

    if human_tasks:
        print()
        print("=" * 60)
        print("[ASK_MASTER] Agent requested clarification:")
        for task_id in human_tasks:
            node = orch.graph_ops.modal.nodes[task_id]
            print(f"  Question: {node.task_payload}")
        print("=" * 60)
        print()
        print("(In interactive mode, you would answer and resume)")
    else:
        print()
        print("=" * 60)
        print("[RESULT]")
        print("=" * 60)
        print(result)

    print()
    print(f"[INFO] Logs saved to: {orch._run_dir}")


if __name__ == "__main__":
    asyncio.run(main())
