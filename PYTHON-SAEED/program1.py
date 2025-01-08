# year = int(input("enter the year"))
# if (year % 4 == 0 and year % 100!=0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")



#another way to find leap years to between certain period

import datetime
current_year = datetime.date.today().year
starting_period = int(input("enter the starting year rou want:"))
final_year = int(input("Enter the final year: "))
if final_year < current_year:
    print("Final year must be greater than or equal to the current year")
else:
    print (f"Leap years from {starting_period} to {final_year} are:-")
for year in range(starting_period, final_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)
