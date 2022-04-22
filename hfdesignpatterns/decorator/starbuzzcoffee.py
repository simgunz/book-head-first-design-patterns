from bevarages import DarkRoast, Espresso, HouseBlend
from condiments import Mocha, Soy, Whip


def main():
    beverage = Espresso()
    print(f"{beverage.get_description()} ${beverage.cost()}")

    beverage_2 = DarkRoast()
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Whip(beverage_2)
    print(f"{beverage_2.get_description()} ${beverage_2.cost()}")

    beverage_3 = HouseBlend()
    beverage_3 = Soy(beverage_3)
    beverage_3 = Mocha(beverage_3)
    beverage_3 = Whip(beverage_3)
    print(f"{beverage_3.get_description()} ${beverage_3.cost()}")


if __name__ == "__main__":
    main()
