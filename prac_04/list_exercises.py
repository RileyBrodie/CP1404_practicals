numbers = []
for i in range(1, 6):
    number = int(input("Number: "))
    numbers.append(number)
print(numbers)
print("The {} number is {}".format("first", numbers[0]),
      "\nThe {} number is {}".format("last", numbers[-1]),
      "\nThe {} number is {}".format("smallest", min(numbers)),
      "\nThe {} number is {}".format("largest", max(numbers)),
      "\nThe average of the numbers is {}".format(sum(numbers) / len(numbers)))

"""Security Checker"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
