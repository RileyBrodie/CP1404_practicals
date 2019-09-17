numbers = [3, 1, 4, 1, 5, 9, 2]

"""
- Selects first list item (3)
- Selects end list item (2)
- Selects the 4th list item (1)
- Select list from start to end
- Select list from the 4th to 5th item
- Checks for the value "5" in the list
- Checks for the value "7" in the list
- Checks for a string "3" in the list
- Adds the values "6", "5", and "3" to the end of the list
"""

print(numbers[0], "\n",
      numbers[-1], "\n",
      numbers[3], "\n",
      numbers[:-1], "\n",
      numbers[3:4], "\n",
      5 in numbers, "\n",
      7 in numbers, "\n",
      "3" in numbers, "\n",
      numbers + [6, 5, 3])

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:-1], "\n",
      9 in numbers)
print(numbers)
