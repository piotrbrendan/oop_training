import pandas as pd
import numpy as np
from operator import itemgetter, attrgetter


class Pizza(object):
    '''Base pizza object - implements get_description and get_cost methods'''


    def get_description(self):
        return self.DESCRIPTION

    def get_cost(self):
        return self.COST



class Margherita(Pizza):
    '''Concrete pizza from basic menu'''

    DESCRIPTION = 'Margherita'
    COST = 15


class Pepperoni(Pizza):
    '''Concrete pizza from basic menu'''

    DESCRIPTION = 'Pepperoni'
    COST = 20


class ToppingDecorator(Pizza):
    '''Base topping decorator class - adding components to basic menu pizzas'''

    def __init__(self,pizza):
        self.pizza = pizza

    def get_description(self):
        return ' '.join([self.pizza.get_description(), Pizza.get_description(self)])

    def get_cost(self):
        return self.pizza.get_cost() + Pizza.get_cost(self)


class TomatoTopping(ToppingDecorator):
    '''Concrete topping with description and its cost'''
    DESCRIPTION = 'Tomato topping'
    COST = 3

class BaconTopping(ToppingDecorator):
    '''Concrete topping with description and its cost'''
    DESCRIPTION = 'Bacon topping'
    COST = 6


if __name__ == '__main__':
    p1 = Margherita()
    p1 = TomatoTopping(p1)
    p1 = BaconTopping(p1)

    p2 = TomatoTopping(Pepperoni())


    print(p1.get_cost())
    print(p1.get_description())
    print(p2.get_cost())