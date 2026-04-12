from datetime import datetime, timedelta

def today():
    return datetime.today().date()

def parse(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()