class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Horse(Animal):
    def gallop(self):
        print("This horse is galloping")

class Dog(Animal):
    def fetch(self):
        print("The dog is fetching")

rabbit = Rabbit()
horse = Horse()
dog = Dog()

#print(rabbit.alive)
#horse.sleep()
#dog.eat()

rabbit.run()
horse.gallop()
dog.fetch()