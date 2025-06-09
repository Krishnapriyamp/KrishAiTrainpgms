import datetime
year = int(input("Enter the year (e.g., 2025): "))
month = int(input("Enter the month number (1-12): "))
month_list=["JAN","FEB","MAR","APRIL","MAY","JUNE","JULY","AUG","SEP","OCT","NOV","DEC"]
print()
print("\t"+month_list[month-1]+"  "+str(year)+"\t")
print("\nMo Tu We Th Fr Sa Su")

first_day = datetime.date(year, month, 1)

start_day = first_day.weekday()

days_in_week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

if month == 12:
    next_month = datetime.date(year + 1, 1, 1)
else:
    next_month = datetime.date(year, month + 1, 1)

total_days = (next_month - first_day).days

print("   " * start_day, end="")

for day in range(1, total_days + 1):
    print(f"{day:2}", end=" ")
    if (start_day + day) % 7 == 0:
        print()  
"""
output
Enter the year (e.g., 2025): 2025
Enter the month number (1-12): 6

        JUNE  2025

Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30
"""