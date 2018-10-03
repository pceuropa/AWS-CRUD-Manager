from datetime import datetime, timedelta, timezone


def difference(date: datetime):
    """return days difference
    :arg1: TODO
    :returns: TODO
    """
    now = datetime.now(timezone.utc)
    d = now - date
    return d.days

def format(date: datetime):
    """return days difference
    :arg1: TODO
    :returns: TODO
    """
    return date.strftime("%Y-%m-%d")
