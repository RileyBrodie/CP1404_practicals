number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items.")
    number_of_items = int(input("Number of items: "))

total = 0
for i in range(number_of_items):
    price = float(input("Price of item: $"))
    total = total + price

if total >= 100:
    total = total - (total * 0.1)

print("total price for {1} items is ${0:.2f}".format(total, number_of_items))
