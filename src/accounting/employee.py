# Creation of the Employee class to store and manipulate Employee related data.
class Employee:

    # Initilization of the Employee class and its attributes.
    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues):
        self.__employee_id = get_employee_id()  # Get employee ID.
        self.__first_name = get_first_name()    # Get first name.
        self.__last_name = get_last_name()    # Get last name.
        self.__hourly_rate = get_hourly_rate()    # Get hourly rate.
        self.__weekly_dues = get_weekly_dues()    # Get weekly dues.

    # get_employee_id will gather employee ID from user input.
    def get_employee_id = input('Please input employee ID: ')

    # get_first_name will gather employee first name from user input.
    def get_first_name = input('Please enter employee first name: ')

    def get_last_name = input('Please enter employee last name: ')

    # The get_full_name function will get first and last name and order them as last_name, first_name.

    def get_full_name(last_name, first_name):
        return __full_name = ()