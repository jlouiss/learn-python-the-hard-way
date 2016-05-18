# Animal is-a object
class Animal(object):
    def __init__(self):
        self.isAlive = true


# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name


# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name


# Person is-a object
class Person(object):

    def __init(self, name):
        # Person has-a name
        self.name = name
        # Person has-a pet of some kind
        self.pet = None


# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # Employee has-a name
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary


# Fish is-a object
class Fish(object):
    def __init__(self):
        self.fins = 2


# Salmon is-a Fish
class Salmon(Fish):
    def __init__(self):
        self.scientificName = 'Salmo Salar'


# Halibut is-a Fish
class Halibut(Fish):
    def __init__(self):
        self.scientificName = 'Hippoglossus Hippoglossus'


# rover is-a Dog
rover = Dog('Rover')

# satan is-a Cat
satan = Cat('Satan')

# mary is-a person
mary = Person('Mary')

# mary has-a pet named satan
mary.pet = satan

# frank is-a Employee named Frank with a salary of 120000
frank = Employee('Frank', 120000)

# frank has-a pet named rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
