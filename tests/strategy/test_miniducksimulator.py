from hfdesignpatterns.strategy.behaviours.fly import FlyRockets
from hfdesignpatterns.strategy.ducks import MallardDuck, ModelDuck


def test_mallard_duck(capsys):
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    assert capsys.readouterr().out == "Quack\nI'm flying!!\n"


def test_model_duck_with_rockets(capsys):
    mallard = ModelDuck()
    mallard.perform_quack()
    mallard.perform_fly()
    mallard.fly_behaviour = FlyRockets()
    mallard.perform_fly()

    assert capsys.readouterr().out == "Quack\nI can't fly\nI'm flying with rockets\n"
