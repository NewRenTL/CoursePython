##import datetime

from datetime import datetime

def print_date(date):
    print(f'Year: {date.year} Month: {date.month} Day: {date.day} Hour: {date.hour} Minutes: {date.minute} Seconds: {date.second} timestamp:{date.timestamp()}')

now = datetime.now()
print_date(now)


print()
year_2023 = datetime(2024,1,1)
print_date(year_2023)

from datetime import time

current_time = time(21,6,20)
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

def print_date_1(curr_date:date):
    print(f'{curr_date.year} | {curr_date.month} | {curr_date.day}')
current_date = date.today()
print()
print_date_1(current_date)

current_date = date(2022,10,6)
print()
print_date_1(current_date)
current_date = date(current_date.year,current_date.month+2,current_date.day)
print()
print_date_1(current_date)
#You can't place +1 when the month is 12

from datetime import timedelta

print(year_2023- now)

#Timedelta supports substract,add,plus,minus,divided by x operations
time_delta1 = timedelta(200,100,100,weeks=10) # 200 days + 100 seconds + 100 ms + 10 weeks (10*7)
time_delta2 = timedelta(300,100,100,weeks=13) # 300 days + 100 seconds + 100 ms + 10 weeks (10*7
print(time_delta2 - time_delta1)



