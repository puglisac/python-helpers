"""
takes a json date-time in ISO 8601 format and returns a human-readable, formatted string

>>> get_date_time("2005-03-01 19:00:00")
'2005-03-01 07:00 PM'

"""

from datetime import datetime

def get_date_time(json_date):
    date_time = datetime.strptime(json_date, '%Y-%m-%d %H:%M:%S')
    date = datetime.date(date_time)
    time = datetime.time(date_time).strftime('%I:%M %p')
    return f"{date} {time}"

