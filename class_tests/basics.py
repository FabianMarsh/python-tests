class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Number of Employess:", Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name, "Salary:", self.salary)


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
print("Employee.__name__", Employee.__name__)
print("Employee.__module__", Employee.__module__)
print("Employee.__bases__", Employee.__bases__)
print("Employee.__dict__", Employee.__dict__)
