# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Derived class from Person
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")


# Multiple inheritance (Person + Employee)
class Manager(Employee, Person):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_manager(self):
        print(f"Department: {self.department}")

    def full_details(self):
        print("\n--- Manager Details ---")
        self.display_person()
        self.display_employee()
        self.display_manager()


# Creating object
m1 = Manager("Tejas", 21, "E101", 50000, "IT")

# Calling method
m1.full_details()