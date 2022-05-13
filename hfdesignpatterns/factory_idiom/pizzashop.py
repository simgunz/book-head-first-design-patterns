class PizzaShop:
    def __init__(self, factory):
        self.factory = factory

    def orderPizza(self, pizzaType):
        pizza = self.factory.createPizza(pizzaType)
        pizza.prepare()
        return pizza
