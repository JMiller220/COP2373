# This program attempts to sell 20 cinema tickets,
# allows users to pre-order up to four tickets, and
# displays the total number of buyers.


def per_customer(purchase):
    # Loops if user attempts to purchase more than 4 tickets
    while purchase > 4:

        print()
        print('Limit of 4 per customer')

        # Re-asks the user to input a valid number of tickets.
        # Assigns this back into the variable "purchase"
        purchase = int(input('Enter valid number of tickets: '))

    # Returns a valid number of tickets
    return purchase

def get_tickets():

    # Amount of tickets to sell
    tickets = 20

    # Sets up an accumulator
    buyers = 0

    # Loops if there is still tickets left.
    while tickets:

        # Prompts and assigns the amount of tickets a customer would like
        buy = int(input('How many tickets would you like: '))

        # Prevents a customer from purchasing zero tickets.
        while buy == 0:

            print()
            print('Cannot be 0')
            print()

            buy = int(input('How many tickets would you like: '))

        # Prevents a customer from buying more than 4 tickets
        if buy > 4:

            # Assigns "limit" to the valid amount from the
            # "per_customer" function
            limit = per_customer(buy)

            # Sells a valid amount of tickets
            tickets -= limit

            # Cancels the purchase if users buy non-existing tickets.
            if tickets < 0:
                # returns any existing and non-existing tickets
                tickets += limit

                # Removes a customer from the total customers
                buyers -= 1

                print()
                print(f'Unfortunately, there is only {tickets} left')

            # Counts the amount of valid customers
            buyers += 1

            print()
            # Display the amount of tickets left
            print(f'Tickets: {tickets}')

        # Used if nothing goes wrong during the original
        # purchase
        else:

            # Sells a valid amount of tickets
            tickets -= buy

            # Counts the amount of valid customers
            buyers += 1

            if tickets < 0:

                # returns any existing and non-existing tickets
                tickets += buy

                # Removes a customer from the total customers
                buyers -= 1

                print()
                print(f'Unfortunately, there is only {tickets} left')

            else:

                print()
                # Display the amount of tickets left
                print(f'Tickets: {tickets}')

    # Displays the amount of valid customers
    print(f'Customers: {buyers}')


# Calls the get_ticket function
get_tickets()
