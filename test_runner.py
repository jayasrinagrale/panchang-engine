from engine.panchang_service import get_panchang

result = get_panchang(
    date_str="2025-01-01",
    lat=17.385,
    lng=78.486,
    tz_str="Asia/Kolkata"
)

print(result)
