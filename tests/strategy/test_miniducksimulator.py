from hfdesignpatterns.strategy.ducks import MallardDuck


def test_mallard_duck(capsys):
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    assert capsys.readouterr().out == "Quack\nI'm flying!!\n"
