"""Riley Brodie"""
min_length = 2
max_length = 10

password = str(input("Enter a password"))
while min_length > len(password) or len(password) > max_length:
    print("please enter a password between 2 and 10 characters")
    password = str(input("Enter a password"))

print("*" * len(password))