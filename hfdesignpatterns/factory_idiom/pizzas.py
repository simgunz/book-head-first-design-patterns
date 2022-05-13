class Pizza:
    def __init__(self, name):
        self.name = name

    def prepare(self):
        print(f"Preparing {self.name}:")

    def bake(self):
        print(f"Baking {self.name}:")


class CheesePizza(Pizza):
    def __init__(self):
        super().__init__("Cheese Pizza")

    def prepare(self):
        super().prepare()
        print("Adding cheese")

    def bake(self):
        super().bake()
        print("Baking for 2 minutes")


class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__("Veggie Pizza")

    def prepare(self):
        super().prepare()
        print("Adding zucchini")

    def bake(self):
        super().bake()
        print("Baking for 3 minutes")
