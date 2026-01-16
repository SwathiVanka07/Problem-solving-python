year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):                  # if the entered year is divisible by 400 → Leap year
    print("Leap year")
else:
    print("Not a leap year")
