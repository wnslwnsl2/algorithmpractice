
"""
decorator pattern

urls
- https://refactoring.guru/design-patterns/decorator/python/example

definition
- Decorator is a structural pattern that allows adding new behaviors to objects
dynamically by placing them inside special wrappper objects.

-------------------------------------
decorator is a component
decorator has a component
"""

class Beverage:
    def desc(self)->str:
        return "Beverage"
    def cost(self)->int:
        return 0

class Coffee(Beverage):
    def desc(self)->str:
        return "coffee"
    def cost(self)->int:
        return 4000

class BeverageDecorator(Beverage):
    def __init__(self,beverage):
        self.beverage = beverage

    def desc(self)->str:
        return self.beverage.desc()

    def cost(self)->int:
        return self.beverage.cost()

class MilkDecorator(BeverageDecorator):
    def desc(self)->str:
        return '{} + Milk'.format(self.beverage.desc())
    def cost(self) ->int:
        return self.beverage.cost()+500

caffelatte = MilkDecorator(Coffee())
print(caffelatte.desc())
print(caffelatte.cost())