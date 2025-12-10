# engine/panchang_service.py

from datetime import datetime
from drikpanchang.panchanga import Panchanga
from drikpanchang.swe.swe import Swe
import pytz

def get_panchang(date_str, lat, lng, tz_str="Asia/Kolkata"):
    """
    Returns a dict with:
    - tithi
    - nakshatra
    - yoga
    - karana
    - sunrise, sunset
    - moonrise, moonset
    """

    # Parse date
    tz = pytz.timezone(tz_str)
    date = datetime.strptime(date_str, "%Y-%m-%d")
    date = tz.localize(date)

    # Create Swiss Ephemeris object
    swe_obj = Swe(lat=lat, lon=lng, tz=tz_str)

    # Create Panchanga calculation instance
    panchang = Panchanga(date, swe_obj)

    # Format results
    result = {
        "date": date_str,
        "latitude": lat,
        "longitude": lng,
        "tithi": panchang.get_tithi()[0],
        "nakshatra": panchang.get_nakshatra()[0],
        "yoga": panchang.get_yoga()[0],
        "karana": panchang.get_karana()[0],
        "sunrise": panchang.sunrise.strftime("%H:%M") if panchang.sunrise else None,
        "sunset": panchang.sunset.strftime("%H:%M") if panchang.sunset else None,
        "moonrise": panchang.moonrise.strftime("%H:%M") if panchang.moonrise else None,
        "moonset": panchang.moonset.strftime("%H:%M") if panchang.moonset else None,
    }

    return result
