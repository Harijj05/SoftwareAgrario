"""Date utilities - Date handling functions."""

from datetime import datetime, timedelta


def parse_date(date_string, format="%Y-%m-%d"):
    """Parse date string to datetime object."""
    try:
        return datetime.strptime(date_string, format)
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}. Expected format: {format}")


def format_date(date_obj, format="%Y-%m-%d"):
    """Format datetime object to string."""
    if isinstance(date_obj, str):
        return date_obj
    return date_obj.strftime(format)


def add_days(date_obj, days):
    """Add days to a date."""
    if isinstance(date_obj, str):
        date_obj = parse_date(date_obj)
    return date_obj + timedelta(days=days)


def get_date_difference(date1, date2):
    """Get difference between two dates in days."""
    if isinstance(date1, str):
        date1 = parse_date(date1)
    if isinstance(date2, str):
        date2 = parse_date(date2)
    return abs((date1 - date2).days)
