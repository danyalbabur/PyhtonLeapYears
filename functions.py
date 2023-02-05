month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    year = int(input("please write a year: " ))
    return year % 4 ==0 and (year % 100 != 0 or year % 400 == 0 )
print(is_leap(2016))

def days_in_month(year, month):
    month = int(input("write a month: "))
    if not 1 <= month <= 12: 
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
print(days_in_month(0,0))


