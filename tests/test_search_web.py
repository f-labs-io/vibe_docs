import pytest
from vibe_docs.tools.search_web import search_web


@pytest.mark.asyncio
async def test_search_web_returns_dict():
    result = await search_web("test query", mock=True)
    assert "results" in result or "answer" in result
