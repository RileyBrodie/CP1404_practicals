from prac_06.guitar import Guitar


def main():
    g1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    g2 = Guitar("Another Guitar", 2012, 7499)

    print(g1)
    print(g2)

    print(g1.get_age())
    print(g2.get_age())

    print(g1.is_vintage())
    print(g2.is_vintage())


main()
