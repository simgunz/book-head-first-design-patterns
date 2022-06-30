class Pizza:
    def __init__(self, name):
        self.name = name

    def prepare(self):
        print(f"Preparing {self.name}:")

    def bake(self):
        print(f"Baking {self.name}:")


class NYCheesePizza(Pizza):
    def __init__(self):
        super().__init__("Cheese Pizza")

    def prepare(self):
        super().prepare()
        print("Adding ceddar")

    def bake(self):
        super().bake()
        print("Baking for 1 minutes")


class NYVeggiePizza(Pizza):
    def __init__(self):
        super().__init__("Veggie Pizza")

    def prepare(self):
        super().prepare()
        print("Adding carrots")

    def bake(self):
        super().bake()
        print("Baking for 4 minutes")


class ChicagoCheesePizza(Pizza):
    def __init__(self):
        super().__init__("Cheese Pizza")

    def prepare(self):
        super().prepare()
        print("Adding cheese")

    def bake(self):
        super().bake()
        print("Baking for 2 minutes")


class ChicagoVeggiePizza(Pizza):
    def __init__(self):
        super().__init__("Veggie Pizza")

    def prepare(self):
        super().prepare()
        print("Adding zucchini")

    def bake(self):
        super().bake()
        print("Baking for 3 minutes")
