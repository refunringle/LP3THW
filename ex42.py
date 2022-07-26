class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        print(name)

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        print(name)

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None
        print(name)


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary
        print(salary)

class Fish(object):
    pass

class Salmon(Fish):
    def __init__(self,name):
        super(Salmon,self).__init__(name)
        self.name=name
        print(name)

class Halibut(Fish):
    pass

if __name__ == "__main__":
    rover = Dog("Rover")
if __name__ == "__main__":
    satan = Cat("Satan")
if __name__ == "__main__":
    mary = Person("Mary")
    mary.pet = satan
if __name__ == "__main__":
    frank = Employee("Frank", 120000)
if __name__ == "__main__":
    frank.pet = rover
if __name__ == "__main__":
    flipper = Salmon('cat_fish')
