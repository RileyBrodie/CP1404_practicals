COLOUR_HEXES = {"Cyan1": "#00ffff", "DarkKhaki": "#bdb76b", "DarkOliveGreen": "#556b2f", "DarkOrange": "#ff8c00",
                "DarkOrchid": "#9932cc", "LawnGreen": "#7cfc00", "LightBlue": "#add8e6"}
# print(STATE_NAMES)
for colour in COLOUR_HEXES:
    print("{:3} is {}".format(colour, COLOUR_HEXES[colour]))

colour = input("Enter colour: ")
while colour != "":
    if colour in COLOUR_HEXES:
        print(colour, "is", COLOUR_HEXES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")
