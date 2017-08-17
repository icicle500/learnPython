class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal,Runnable,CarnivorousMixIn):
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 几种功能
class RunnableMixIn(object):
    pass

class FlyableMixIn(object):
    pass

class CarnivorousMixIn(object):
    pass

class HerbivoreMixIn(object):
    pass