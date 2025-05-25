from datetime import datetime, timezone

def get_now() -> datetime:
    return datetime.now(tz=timezone.utc)

def get_now_utc() -> datetime:
    return datetime.now(tz=timezone.utc)