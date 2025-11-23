# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

class Prey:
    def flee(self):
        print(f"This animal is fleeing")

class Predator:
    def hunt(self):
        print(f"This animal is hunting")


# children classes
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()

fish.flee()
fish.hunt()
