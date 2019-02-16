from datetime import datetime


def validate_time(time, fmt="%H:%M:%S"):
    try:
        return str(datetime.strptime(time, fmt))
    except Exception as exc:
        raise ValueError("invalid format")
