import abc

from pizzas import ChicagoCheesePizza, ChicagoVeggiePizza, NYCheesePizza, NYVeggiePizza


class PizzaStore(abc.ABC):
    def orderPizza(self, pizzaType):
        pizza = self.createPizza(pizzaType)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abc.abstractmethod
    def createPizza(self):
        raise NotImplementedError()


class NYStylePizzaStore(PizzaStore):
    def createPizza(self, type):
        if type == "cheese":
            return NYCheesePizza()
        elif type == "veggie":
            return NYVeggiePizza()


class ChigagoStylePizzaStore(PizzaStore):
    def createPizza(self, type):
        if type == "cheese":
            return ChicagoCheesePizza()
        elif type == "veggie":
            return ChicagoVeggiePizza()


if __name__ == "__main__":
    pizza_store = NYStylePizzaStore()
    pizza_store.orderPizza("cheese")
    pizza_store.orderPizza("veggie")
