import calendar  
year = int(input("Enter the year (e.g., 2025): "))
month = int(input("Enter the month number (1-12): "))

print()
print(calendar.month(year, month))
"""
output
Enter the year (e.g., 2025): 2025
Enter the month number (1-12): 6

     June 2025
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30
"""