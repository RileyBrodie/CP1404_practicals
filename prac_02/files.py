name = str(input("Please enter your name: "))
name_file = open("name.txt", "w")
print(name, file=name_file)
name_file.close()

name_file = open("name.txt", "r")
name = str(name_file.readline())
print("Your name is {}".format(name))
name_file.close()

numbers_file = open("numbers.txt", "r")
num1 = int(numbers_file.readline())
num2 = int(numbers_file.readline())
print(num1 + num2)
numbers_file.close()

total = 0
multiple_numbers_file = open("multiple_numbers.txt", "r")
nums = (multiple_numbers_file.readlines())
for number in nums:
    total = total + int(number)
print(total)
multiple_numbers_file.close()
