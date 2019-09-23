HEX_COLOURS = {"AliceBlue": "#f0f8ff", "BlueViolet": "#8a2be2", "Chocolate": "#d2691e", "DarkOrange": "#ff8c00",
               "Firebrick": "#b22222", "LawnGreen": "#7cfc00", "Moccasin": "#ffe4b5"}
# print(HEX_COLOURS)
for colour in HEX_COLOURS:
    print("{:8} is {}".format(colour, HEX_COLOURS[colour]))

colour = input("Enter colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")
