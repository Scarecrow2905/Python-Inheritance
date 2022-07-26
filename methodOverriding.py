class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    # Here is the method overridden
    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()