s = input("Enter a string: ")                 # user input

rev = ""
for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome string")
else:
    print("Not a palindrome")
