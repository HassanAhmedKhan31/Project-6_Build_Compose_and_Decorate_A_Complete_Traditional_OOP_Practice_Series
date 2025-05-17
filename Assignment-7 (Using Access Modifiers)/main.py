class Employee:
    def __init__(self):
        self.name = "Ali"              # Public
        self._salary = 50000           # Protected
        self.__ssn = "123-45-6789"     # Private

# Example
emp = Employee()
print(emp.name)         # Public
print(emp._salary)      # Protected (discouraged but accessible)
# print(emp.__ssn)      # Private - Error
print(emp._Employee__ssn)  # Access using name mangling
