class Person:
    '''This class represents a person object'''

    def __init__(self, first_name, surname, tel):
        self.first_name = first_name
        self.surname = surname
        self.tel = tel

    def full_name(self):
        return self.first_name + " " + self.surname


class Employee(Person):

    def __init__(self, first_name, surname, tel, salary):
        super().__init__(first_name, surname, tel)
        self.salary = salary

    def give_raise(self, amount):
        self.salary = self.salary + amount


print(Person.__doc__)

p = Person("Simon", "Anderson", "123-456")

e = Employee("Sergey", "Tyulenev", "79-46-14", 3000)

print(p.full_name())
print(e.full_name())
e.give_raise(100)