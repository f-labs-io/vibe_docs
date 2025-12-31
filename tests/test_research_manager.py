import pytest
from vibe_docs.agents.research_manager import build_research_manager_config


def test_research_manager_has_delegation():
    config = build_research_manager_config()
    assert "route_to_research_agent" in config["tools"]


def test_research_manager_has_ask_master():
    config = build_research_manager_config()
    assert "ask_master" in config["tools"]


def test_research_manager_has_handoff():
    config = build_research_manager_config()
    assert "handoff" in config["tools"]
