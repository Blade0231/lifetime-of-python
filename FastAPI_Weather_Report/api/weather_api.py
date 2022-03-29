from fastapi import Depends, APIRouter
from typing import Optional

from models.location import Location
from services import open_weather_service 

router = APIRouter()

@router.get('/api/weather/{city}/')
async def weather(loc: Location = Depends(),
        units: Optional[str] = 'metric'):

    report =  await open_weather_service.async_get_report(loc.city, loc.state, loc.country, units)
    
    return report
