## Dates ##

from datetime import datetime

now = datetime.now()



timestamp = now.timestamp()
print(timestamp)



def print_date(date):
    print(date.day)
    print(date.hour)
    print(date.min)
    print(date.second)
    print(date.year)
    print(date.month)
    print(date.timestamp())

print_date(now)

year_2023= datetime(2023, 1, 1, 3)
print_date(year_2023)

from datetime import time

current_time = time(21, 6, 0 )
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)


current_date = date(2022, 10, 6)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day )
print(current_date.month)

diff = year_2023 - now
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks= 10)
end_timedelta = timedelta(200, 100, 100, weeks= 10)
print(end_timedelta + start_timedelta)
print(end_timedelta - start_timedelta)
print(end_timedelta / start_timedelta)