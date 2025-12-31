# Vibe Docs

Research agents for web research, powered by ai-orchestration.

## Installation

```bash
pip install git+https://github.com/f-labs-io/vibe_docs.git
```

## Quick Start

```python
import asyncio
from ai_orchestration import Orchestrator
from vibe_docs.agents import build_research_manager_config, build_research_agent_config
from vibe_docs.tools import search_web

async def main():
    orch = Orchestrator(logs_dir="./logs")

    # Register agents
    orch.agent.create(**build_research_manager_config())
    orch.agent.create(**build_research_agent_config())

    # Register search tool
    orch.register_tool(
        name="search_web",
        description="Search the web",
        input_schema={"type": "object", "properties": {"query": {"type": "string"}}},
        handler=search_web
    )

    # Research!
    result = await orch.run("research_manager", "What is vibe coding?")
    print(result)

asyncio.run(main())
```

## Agents

- **Research Manager**: Root agent that coordinates research, can ask user for clarification
- **Research Agent**: Web search specialist

## Demo Scripts

```bash
# Simple query
python demo/simple_research.py

# ask_master flow (user interaction)
python demo/ask_master_flow.py

# Multi-step research
python demo/multi_step_research.py
```

## License

MIT
