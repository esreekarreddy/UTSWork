class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def default_constructor(cls):
        return cls("null", 0)

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age 
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f'{self.name} age is {self.age}'
    
class People:
    def __init__(self):
        self.first = Person.default_constructor()
        self.second = Person('Spark', 24)
    
    def show(self):
        print(self.first)
        print(self.second)
    
    def update(self, Person, name):
        Person.name = name


def main():
    people = People()
    people.show()
    people.update(people.first, 'Lily')
    people.update(people.second, 'Sparky Anderson')
    people.show()

if __name__ == "__main__":
    main()