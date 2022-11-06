from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime('%H:%M:%S --- %Y/%m/%d'))
print(datetime(year=1996, month=10, day=17, hour=22))

yesterday = now - timedelta(days=1)
print(yesterday)
