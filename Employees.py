# This program accepts an employees name, number, shift, and hourly
# pay, then displays all the information.
# Jason Miller. Assignment 1.

class Employee:

    # Initializes the attributes with the employee's
    # name and number.
    def __init__(self, name, number):
        self.__name = name

        self.__number = number

    # Accepts an argument for the employee's name.
    def set_name(self, name):
        self.__name = name

    # Accepts an argument for the employee's number.
    def set_number(self, number):
        self.__number = number

    # Returns the employee's name.
    def get_name(self):
        return self.__name

    # Returns the employee's number.
    def get_number(self):
        return self.__number


# Creates a subclass of the Employee class
class ProductionWorker(Employee):

    # Initializes the attributes with the employee's
    # name, number, shift and hourly pay rate.
    def __init__(self, name, number, shift, pay):
        # Calls the '__init__' function from the
        # Employee class

        # This allows the 'Production_Worker' subclass to
        # access the Employee class objects.
        Employee.__init__(self, name, number)

        self.__shift = shift

        self.__pay = pay

    # Accepts an argument for the employee's shift.
    def set_shift(self, shift):
        self.__shift = shift

    # Accepts an argument for the employee's hourly rate.
    def set_pay(self, pay):
        self.__pay = pay

    # Returns the employee's shift.
    def get_shift(self):
        return self.__shift

    # Returns the employee's hourly rate.
    def get_pay(self):
        return self.__pay


def main():
    intro()
    enter()

    # Prompts user for the employee's name.
    name = input("Enter the employee's name: ")

    # Prompts user for the employee's number.
    number = input("Enter the employee's number: ")

    # Creates an instance for the Employee class.
    Employee(name, number)

    # Prompts user for the employee's shift number.
    shift = int(input("Enter the employee's shift number\n"
                      "(1 = Day, 2 = Night): "))

    # Re-prompts user for the employee's number if
    # an invalid number is inputted.
    while shift != 1 and shift != 2:
        shift = int(input('Enter a valid shift number: '))

    # Prompts user for the employee's hourly pay.
    pay = float(input("Enter the employee's hourly pay: "))

    # Creates an instance for the Production_Worker class.
    shift_info = ProductionWorker(name, number, shift, pay)

    # Displays all information received.
    print()
    print('Review the info you entered')
    print('---------------------------')

    print(f'Employee Name: {shift_info.get_name()}')
    print()
    print(f'Employee Number: {shift_info.get_number()}')
    print()

    # Displays 1 of 2 prompts depending on shift time.
    if shift == 1:

        print(f'Employee Shift: {shift_info.get_shift()} (Day shift)')

    else:
        print(f'Employee Shift: {shift_info.get_shift()} (Night shift)')
    print()
    print(f'Employee hourly pay: ${shift_info.get_pay():,.1f}')


def intro():
    # Briefly describes the program.
    print("Input an employee's credentials and review\n"
          'them at the end (press enter when ready).')


def enter():
    input()


if __name__ == '__main__':
    main()
