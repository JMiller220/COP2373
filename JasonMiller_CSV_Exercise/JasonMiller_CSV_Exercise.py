import csv
def get_students():
    # Prompts for number of students
    num_students = int(input("Enter the number of students "))

    # Creates a list of headers
    # Also used to append the students' information.
    students_list = [["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]]

    # Gathers information for a received number of students
    for i in range(num_students):

        # Gets a student's first name
        first = input("Enter the students first name: ")

        # Gets a student's last name
        last = input("Enter the students last name: ")

        # Gets a student's first exam score
        exam1 = int(input(f"Enter {first} {last}'s exam 1 grade: "))

        # Gets a student's second exam score
        exam2 = int(input(f"Enter {first} {last}'s exam 2 grade: "))

        # Gets a student's third exam score
        exam3 = int(input(f"Enter {first} {last}'s exam 3 grade: "))

        # Exits if an invalid score is entered
        if exam1 > 100 or exam2 > 100 or exam3 > 100 or exam1 < 0 or exam2 < 0 or exam3 < 0:
            print("\nInvalid Exam Score Entered. File not created")
            exit()

        # Puts a student's information into a variable
        student = first, last, exam1, exam2, exam3

        # Appends a student's information to the student list.
        students_list.append(list(student))
        print()

    # Opens and writes to a csv file
    with open("grades.csv", "w", newline='') as file:

        # Creates a writer instance
        writer = csv.writer(file)

        # Writes all students' information to a csv file
        writer.writerows(students_list)


def read_students_grade():
    # Opens and reads the grades.csv file
    with open("grades.csv", "r", newline='') as file:
        # Creates a dictionary reader instance
        reader = csv.DictReader(file)

        # Formats and displays the header
        for row in reader:
            print("{:<15} {:<12} {:<9} {:<9} {:<9}".format("First Name",
                                                           "Last Name",
                                                           "Exam 1",
                                                           "Exam 2",
                                                           "Exam 3"))

            # Formats and displays all students' information
            print("{:<15} {:<12} {:<9} {:<9} {:<9}".format(row["First Name"],
                                                           row["Last Name"],
                                                           row["Exam 1"],
                                                           row["Exam 2"],
                                                           row["Exam 3"]))
            print("--" * 30)


# Call the get_students function
get_students()

# Call the read_students_grade function
read_students_grade()