import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month

# Create own date
the_day = dt.datetime(year=2001, month=6, day=14, hour=16)
print(the_day)
