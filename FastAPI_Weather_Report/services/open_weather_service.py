from typing import Optional
import httpx

api_key: Optional[str] = None


async def async_get_report(
    city: str, state: Optional[str], country: str, metrics: Optional[str]
) -> dict:

    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()
    forecast = data["main"]
    return forecast
