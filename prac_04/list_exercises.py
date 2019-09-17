numbers = []
for i in range(1, 6):
    number = int(input("Number: "))
    numbers.append(number)
print(numbers)
print("The {} number is {}".format("first", numbers[0]), "\n"
      "The {} number is {}".format("last", numbers[-1]), "\n"
      "The {} number is {}".format("smallest", min(numbers)), "\n"
      "The {} number is {}".format("largest", max(numbers)), "\n"
      "The average of the numbers is {}".format(sum(numbers)/len(numbers)))
