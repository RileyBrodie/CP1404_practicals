from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.name = my_car
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)

    limo = Car(100)
    limo.name = limo
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)



main()
