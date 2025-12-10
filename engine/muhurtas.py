# engine/muhurtas.py

from datetime import datetime, timedelta

def compute_rahukaal(date, sunrise, sunset):
    """
    Rahukaal calculation based on weekday.
    Returns tuple: (start_time, end_time)
    """

    # Rahukaal segments are 1/8th of daytime
    day_duration = (sunset - sunrise).total_seconds() / 8
    weekday = date.weekday()  # Monday=0 ... Sunday=6

    # Segment index depending on weekday
    rahukaal_segment = {
        0: 1,  # Monday
        1: 6,  # Tuesday
        2: 4,  # Wednesday
        3: 5,  # Thursday
        4: 3,  # Friday
        5: 2,  # Saturday
        6: 7   # Sunday
    }[weekday]

    start = sunrise + timedelta(seconds=day_duration * rahukaal_segment)
    end = start + timedelta(seconds=day_duration)

    return start, end


def compute_yamaganda(date, sunrise, sunset):
    yamaganda_segment = {
        0: 5,
        1: 2,
        2: 3,
        3: 1,
        4: 0,
        5: 6,
        6: 4
    }[date.weekday()]

    day_duration = (sunset - sunrise).total_seconds() / 8
    start = sunrise + timedelta(seconds=day_duration * yamaganda_segment)
    end = start + timedelta(seconds=day_duration)

    return start, end


def compute_gulika(date, sunrise, sunset):
    gulika_segment = {
        0: 4,
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 6,
        6: 5
    }[date.weekday()]

    day_duration = (sunset - sunrise).total_seconds() / 8
    start = sunrise + timedelta(seconds=day_duration * gulika_segment)
    end = start + timedelta(seconds=day_duration)

    return start, end


def compute_abhijit(sunrise, sunset):
    """
    Abhijit Muhurta is the middle of the day ± approx 24 mins
    """
    mid_day = sunrise + (sunset - sunrise) / 2
    start = mid_day - timedelta(minutes=24)
    end = mid_day + timedelta(minutes=24)

    return start, end
