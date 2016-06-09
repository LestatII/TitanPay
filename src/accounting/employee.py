# Creation of the Employee class to store and manipulate general employee data.
class Employee:

    # Initialization of the Employee class and its attributes.
    def __init__(self, employee_id, first_name, last_name, weekly_dues):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__weekly_dues = weekly_dues

        # The following methods are mutators for the class's data attributes.
        def get_employee_id =

        def set_first_name(self, first_name):
            self.__first_name = first_name

        def set_last_name(self, last_name):
            self.__last_name = last_name

        # The get_full_name function will get first and last name and order them as last_name, first_name.
        def get_full_name(last_name, first_name):
            return __full_name = ()

    def get_employee_id(self):
        return self.__employee_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    # The get_full_name function will get first and last name and order them as last_name, first_name.
    def get_full_name(last_name, first_name):
        return __full_name = ()

# The Hourly class holds data for an hourly employee.
class Hourly(Employee):
    # The __init__ method accepts arguments for the hourly employee's employee ID, first and last name, \
    # weekly dues and hourly rate.
    def __init__(self, employee_id, first_name, last_name, weekly_dues, hourly_rate):
        # Call the superclass's __init__ method and pass the required arguments.
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)

        # Initialize the hourly_rate attribute.
        self.__hourly_rate = hourly_rate

# The Salary class holds data for an salaried employee.
class Salary(Employee):
    # The __init__ method accepts arguments for the salaried employee's employee ID, first and last name, \
    # weekly dues and salary.
    def __init__(self, employee_id, first_name, last_name, weekly_dues, salary):
        # Call the superclass's __init__ method and pass the required arguments.
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)

        # Initialize the salary attribute.
        self.__salary = salary