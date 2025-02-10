# This program gathers and calculates a users expenses.
# As well as, displays the highest, lowest, and the total expense.

import functools

def main():

    # Introduces the program
    print("Enter the type of expense first, afterwords enter the amounts, respectively")
    print("Combine multiple words with a hyphen")

    # Prompts user for expenses
    type_exp = str(input("Enter the type of expenses: ")).split()

    # Prompts user for amounts
    amount_exp = input("Enter the amount the expenses are, respectively: ").split()

    # Exits the program if nothing is entered for expense type or amount
    if len(type_exp) <= 0 or len(amount_exp) <= 0:
        print("Give at least one expense type and one expense amount.")
        exit()

    # Loops if the items are not the same in
    # both "type_exp" and "amount_exp" variables
    while len(type_exp) != len(amount_exp):

        # Re-prompts the program
        print('Enter "quit" to exit program')
        amount_exp = input("Enter the amount the expenses are, respectively ")
        print()

        # Always the user to quit the program.
        if amount_exp == "quit":
            exit()
        else:
            # Splits each number individually into a list
            amount_exp = amount_exp.split()

    # Gathers all expense types
    e_type = [word for word in type_exp]

    try:
        # Gathers all expense amounts
        numbers = [float(number) for number in amount_exp]

# Exits the program if a non-number item is in the "numbers" list
    except ValueError:
        print("Needs to be a valid number")
        exit()

    # Loops through the numbers list
    for num in numbers:

        # Looks if there is a negative number
        if num < 0:

            # Exits the code it there is a negative
            print("Cannot accept negative numbers")
            exit()

    print("__" * 30)
    print()


    # Creates a dictionary and makes the expense type the key and
    # the corresponding expense amount the value
    expenses_dict = {expense_t : amount for expense_t, amount in zip(e_type, numbers)}

    # Adds all numbers in the amounts list together
    total = functools.reduce(lambda x, y : x + y, numbers)

    # Loops through expense dictionary values
    for expense in expenses_dict:

        # Prints if the value is equal to the highest number in the numbers list
        if expenses_dict[expense] == max(numbers):
            print(f"Highest expense: {expense}: ${expenses_dict[expense]:,.2f}")

        # Prints if the value is equal to the lowest number in the numbers list
        if expenses_dict[expense] == min(numbers):
            print(f"Lowest expense: {expense}: ${expenses_dict[expense]:,.2f}")

    # Displays the total
    print(f"Total monthly expense: ${total:,.2f}")


if __name__ == "__main__":
    main()