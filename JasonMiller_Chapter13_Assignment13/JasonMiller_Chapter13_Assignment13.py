# This program creates and displays data of
# an SQL table that stores a cities name, year, and population of that year,
# as well as a graph.

import sqlite3

# Connects to the population_JM database
conn = sqlite3.connect('population_JM')

# Creates a cursor object
cursor = conn.cursor()

def main():

    # Drops the population_JM table if it exits
    cursor.execute("""DROP TABLE IF EXISTS population""")

    # Creates a table for a city, year, and population
    cursor.execute("""CREATE TABLE population(
    city TEXT,
    year INT,
    population INT)""")

    # Defines a dictionary of cities and their respective populations
    cities = {"Orlando": 320_742, "St. Petersburg": 263_553, "Bradenton": 57_076,
              "Parrish": 38_944, "Ocala": 68_426, "Cape Coral": 224_455,
              "Brandon": 116_365, "Fort Myers": 97_372, "North Port": 88_934,
              "Daytona Beach": 82_485}

    while True:
        # calls the displays_options function
        display_options()

        # Lets a user choose which option they please
        option = input()

        # First option: shows the current population
        if option == '1':
            current_pop(cities)

        # Second option: shows the population 20 years from the current
        elif option == '2':
            pop_growth(cities)

        # Third option: shows a graph of the population increasing over the years.
        elif option == '3':
            print("Enter one of the following cities\n"
                  "Orlando, St. Petersburg, Bradenton, Parrish, Ocala\nCape Coral,"
                  " Brandon, Fort Myers, North Port, or Daytona Beach")

            # Receives which city the user wishes to view
            city = input()

            # Attempts to call the show_pop_growth function
            try:
                show_pop_growth(city, cities[city])

            # Catches a KeyError if an invalid option is inputted
            except KeyError:
                print("Invalid Option")
                print()

        # Breaks the loop if a valid option is not chosen
        else:
            print("Quitting...")
            break

    # Closes the database
    conn.close()

def display_options():

    # Displays the options the user can choose from
    print("{:>40}".format("Here are your options"))
    print("--" * 30)

    print("Enter 1: Display Current Population\nEnter 2: Display Population Growth\n"
          "Enter 3: Show city options to see population growth graph.\n"
          "Enter 0: Quit")

def current_pop(cities):

    # Loops through the cities dictionary
    for city, pop in cities.items():
        # Inserts the city name, current year, and the respective cities
        # population into the population table
        cursor.execute("""INSERT INTO population VALUES(?, 2023 , ?)""",
                       (city, pop))

    # Selects all columns in the population table
    cursor.execute("""SELECT * from population""")

    # Assigns all columns to the "info" variable
    info = cursor.fetchall()

    # Displays and formats the title of the function
    print("{:>25}".format("Current Population"))

    # Displays and formats the column names of the function
    print("{:<15} {:<9} {:<9}".format("City",
                                     "Year",
                                     "Population"))
    print("--" * 20)

    # Loops through each row of the table
    for row in info:

        # Displays and formats each row of the table
        print("{:<15} {:<9} {:<9}".format(row[0],
                                          row[1],
                                          row[2]))

    print()

    # Resets the table
    cursor.execute("DELETE FROM population")

def pop_growth(cities):
    import numpy as np

    # Loops through the cities dictionary
    for city, pop in cities.items():

        # Creates an array with 20 elements
        # This is used as the 20 years
        years = np.linspace(0, 20, 20)

        # Gets the amount of people increased in a city
        # for each of the 20 years
        population = years * (pop * .02)

        # Adds the increased population each year to the total population
        population += pop

        # Inserts the city, the future year, and increased population into the
        # population table
        cursor.execute("""INSERT INTO population VALUES(?, 2043 ,?)""",
                       (city, population[-1]))

    # Selects all columns in the population table
    cursor.execute("""SELECT * from population""")

    # Assigns all columns to the "info" variable
    info = cursor.fetchall()

    # Displays and formats the title of the function
    print("{:>25}".format("Growing Population"))

    # Displays and formats the column names of the function
    print("{:<15} {:<9} {:<9}".format("City",
                                     "Year",
                                     "Population"))
    print("--" * 20)

    # Loops through each row of the table
    for row in info:

        # Displays and formats each row of the table
        print("{:<15} {:<9} {:<9}".format(row[0],
                                         row[1],
                                         row[2]))

    print()

    # Resets the table
    cursor.execute("DELETE FROM population")

def show_pop_growth(city, pop):
    import numpy as np
    import matplotlib.pyplot as plt

    # Creates an array with 20 elements
    # This is used as the 20 years
    years = np.linspace(0, 20, 20)

    # Gets the amount of people increased in a city
    # for each of the 20 years
    population = years * (pop * .02)

    # Plots the increasing population onto a graph
    plt.plot(years, population)

    # Formats the graph
    plt.xticks(np.arange(0, 21, 5),
               ("2023", "2028", "2033", "2038", "2043", ))
    plt.title(f"{city}'s Population")
    plt.xlabel("Years")
    plt.ylabel("Population")

    # Shows the graph
    plt.show()

if __name__ == '__main__':
    main()