# engine/panchang_service.py

from datetime import datetime
from drikpanchang.panchanga import Panchanga
from drikpanchang.swe.swe import Swe
import pytz

from engine.muhurtas import (
    compute_rahukaal,
    compute_gulika,
    compute_yamaganda,
    compute_abhijit,
)


def fmt(dt):
    return dt.strftime("%H:%M") if dt else None


def get_panchang(date_str, lat, lng, tz_str="Asia/Kolkata"):
    """
    Returns a dict with:
    - tithi, nakshatra, yoga, karana
    - sunrise, sunset, moonrise, moonset
    - rahukaal, yama, gulika, abhijit
    """

    # Parse date
    tz = pytz.timezone(tz_str)
    date = datetime.strptime(date_str, "%Y-%m-%d")
    date = tz.localize(date)

    # Swiss Ephemeris for calculations
    swe_obj = Swe(lat=lat, lon=lng, tz=tz_str)
    panchang = Panchanga(date, swe_obj)

    # Sunrise / Sunset
    sunrise = panchang.sunrise
    sunset = panchang.sunset

    # Muhurtas
    rahu_start, rahu_end = compute_rahukaal(date, sunrise, sunset)
    gula_start, gula_end = compute_gulika(date, sunrise, sunset)
    yama_start, yama_end = compute_yamaganda(date, sunrise, sunset)
    ab_start, ab_end = compute_abhijit(sunrise, sunset)

    # Final JSON structure
    return {
        "date": date_str,
        "latitude": lat,
        "longitude": lng,

        "tithi": panchang.get_tithi()[0],
        "nakshatra": panchang.get_nakshatra()[0],
        "yoga": panchang.get_yoga()[0],
        "karana": panchang.get_karana()[0],

        "sunrise": fmt(sunrise),
        "sunset": fmt(sunset),
        "moonrise": fmt(panchang.moonrise),
        "moonset": fmt(panchang.moonset),

        "rahukaal": {
            "start": fmt(rahu_start),
            "end": fmt(rahu_end),
        },
        "gulika": {
            "start": fmt(gula_start),
            "end": fmt(gula_end),
        },
        "yamaganda": {
            "start": fmt(yama_start),
            "end": fmt(yama_end),
        },
        "abhijit": {
            "start": fmt(ab_start),
            "end": fmt(ab_end),
        }
    }
