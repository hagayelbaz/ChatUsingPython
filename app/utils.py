def format_date(date):
    if date is None:
        return '-/-'
    day = date.day
    month = date.month
    return f"{day}.{month}"