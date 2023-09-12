# 1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.

"""
year % 40 &
year % 100 !=0 /
year% 400 == 0

"""
def isLeapYear(year):
  if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    return True
  else:
    return False

year = int(input("Enter a year :"))

if isLeapYear(year):
  print('() is a Leap Year.'.format(year))
else:
  print('() is not a Leap Year.'.format(year))