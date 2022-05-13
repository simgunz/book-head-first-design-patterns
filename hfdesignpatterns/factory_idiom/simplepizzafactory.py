from pizzas import CheesePizza, VeggiePizza


class SimplePizzaFactory:
    def createPizza(self, type):
        if type == "cheese":
            return CheesePizza()
        elif type == "veggie":
            return VeggiePizza()
        else:
            return None
