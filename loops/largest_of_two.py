a = int(input("Enter first number: "))          # user input of 1st num
b = int(input("Enter second number: "))         # user input of 2nd num

if a > b:                                        
    print("Largest number is:", a)
elif b > a:
    print("Largest number is:", b)
else:
    print("Both numbers are equal")
