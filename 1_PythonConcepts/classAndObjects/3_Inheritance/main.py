# 1. THE PARENT CLASS (Base Class)
# This class contains the logic shared by all animals.
class Animal:
    def __init__(self, name):
        self.name = name        # Attribute shared by all animals
        self.is_alive = True    # Attribute shared by all animals

    def eat(self):
        # A method that every child class will inherit automatically
        print(f"{self.name} is eating")

    def sleep(self):
        # Another shared method
        print(f"{self.name} is sleeping")

# 2. THE CHILD CLASSES (Derived Classes)
# We put 'Animal' in parentheses to tell Python: 
# "This class has everything an Animal has, plus more."

class Dog(Animal):
    def speak(self):
        # This method is unique to Dog
        print("wof!")

class Cat(Animal):
    def speak(self):
        # This method is unique to Cat
        print("meow!")

class Mouse(Animal):
    def speak(self):
        # This method is unique to Mouse
        print("chew!")

# 3. CREATING OBJECTS (Instantiation)
# Notice we pass the 'name' because the Child classes inherited the __init__ from Animal
dog = Dog("Scooby")
cat = Cat("spsp")
mouse = Mouse("Mickey")

# 4. USING METHODS
dog.speak()  # Defined in Dog class -> Output: wof!
cat.speak()  # Defined in Cat class -> Output: meow!

# We can also call methods from the Parent class, even though 
# we didn't write them inside Dog or Cat!
dog.eat()    # Inherited from Animal -> Output: Scooby is eating
