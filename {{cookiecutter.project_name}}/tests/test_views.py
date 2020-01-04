import httpx
import pytest


@pytest.mark.asyncio
async def test_home_route(client: httpx.Client):
    response = await client.get("/deomo")
    assert response.status_code == 200
    assert response.json() == {"status": True, "data": {"hello": "world"}}
