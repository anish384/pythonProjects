# multilevel inheritance = inherit from more than one parent class
#                          C(A, B)

# 1. GRANDPARENT CLASS
# The root of the hierarchy. Everyone inherits from here eventually.
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")

# 2. PARENT CLASSES (Intermediate Level)
# These inherit from Animal, but add specific traits.
class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

# 3. CHILD CLASSES (The Specific Implementations)

# --- MULTILEVEL INHERITANCE ---
# Chain: Animal -> Prey -> Rabbit
# Rabbit gets flee() from Prey, and eat() from Animal.
class Rabbit(Prey):
    pass 

# Chain: Animal -> Predator -> Hawk
class Hawk(Predator):
    pass

# --- MULTIPLE INHERITANCE ---
# Fish inherits from TWO classes at the same time: Prey AND Predator.
# It gets flee() from Prey, hunt() from Predator, and eat() from Animal (via both).
class Fish(Prey, Predator):
    pass

# 4. TESTING
rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

# Specific behaviors
rabbit.flee()   # Defined in Prey
# rabbit.hunt() # ERROR: Rabbit is not a Predator

fish.flee()     # Defined in Prey
fish.hunt()     # Defined in Predator

# Shared behaviors (inherited all the way from Animal)
# Because Rabbit is Prey, and Prey is an Animal -> Rabbit is an Animal.
rabbit.eat() 
hawk.eat()
fish.eat()
