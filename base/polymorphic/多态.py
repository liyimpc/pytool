'''
多态：一种事务的多种形态，多态的前提是继承
'''

from base.polymorphic.cat import Cat
from base.polymorphic.mouse import Mouse
from base.polymorphic.person import Person

tom = Cat("tom")
jerry = Mouse("jerry")

# tom.eat()
# jerry.eat()

p = Person()
# p.feedCat(tom)
# p.feedMouse(jerry)
p.feedAnimal(tom)
p.feedAnimal(jerry)