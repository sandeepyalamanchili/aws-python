class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

class Manager(Person, Employee):
    def __init__(self, name, employee_id, department):
        Person.__init__(self, name)
        Employee.__init__(self, employee_id)
        self.department = department

    def get_info(self):
        return f"Manager {self.name}, ID: {self.employee_id}, Department: {self.department}"
