# This program calculates and displays the statistics
# of a number of students exams

def main():
    import csv
    import numpy as np
    # Opens and reads the "grades.csv" file
    with open("grades.csv", "r", newline='') as file:
        # Creates a reader instance
        reader = csv.reader(file)

        # Skips the header
        next(reader)

        # Creates empty lists for a student's info and scores
        students_info = []
        scores = []

        # Iterates through each row in the "grades.csv" file
        for row in reader:
            # Appends everything in a row to the students_info list
            students_info.append(np.array(row))

            # Appends only exam scores to the scores list
            scores.append(np.array(row[:][2:], dtype=float))

    print("\n\tStudent Info")
    # Displays the first 4 rows of the "grades.csv" file (skipping the header)
    for i in range(4):
        print(" ".join(students_info[i]))

    # Assigns a dictionary of exam stats
    stats = get_stats_per_exam(scores)

    print("--" * 30, "\n\tStats Per Exam")
    # Displays the statistics for each exam
    for name, values in stats.items():
        formatted = " ".join(f"{v:.2f}" for v in values)
        print(f"{name}: {formatted}")

    print("--" * 30, "\n\tOverall Stats")

    # Assigns a dictionary of the overall exam stats
    overall = get_overall_stats(scores)

    # Displays the overall statistics of the exams
    for name, values in overall.items():
        print(f"{name}: {values:.2f}")


    print("--" * 30, "\n\tPassing and Failing")

    # Assigns a list of how many students passed each exam
    passed = get_pass_fail(scores)[0]

    # Assigns a list of how many students failed each exam
    failed = get_pass_fail(scores)[1]

    # Displays how many students passed and failed each exam
    for i, (p, f) in enumerate(zip(passed, failed), start=1):
        print(f"{p} student(s) passed exam{i}, {f} student(s) failed exam{i}")

    print("--" * 30, "\n\tPassing Percentage")

    # Assigns the overall passing percentage across all exams
    percent = get_percent(scores)

    # Displays the overall passing percentage
    print(f"{percent:.2f}")


def get_stats_per_exam(scores):
    import numpy as np
    # Creates a dictionary of each exam's stats
    stats = {
    "Mean" : np.mean(scores, axis=0),
    "Median" : np.median(scores, axis=0),
    "Standard Deviation" : np.std(scores, axis=0),
    "Minimum" : np.min(scores, axis=0),
    "Maximum" : np.max(scores, axis=0)
    }

    # Returns the dictionary
    return stats

def get_overall_stats(scores):
    import numpy as np

    # Creates a dictionary of the overall of the exam's stats
    overall = {
    "Mean": np.mean(scores),
    "Median": np.median(scores),
    "Standard Deviation": np.std(scores),
    "Minimum": np.min(scores),
    "Maximum": np.max(scores)
    }
    # Returns the dictionary
    return overall

def get_pass_fail(scores):
    import numpy as np
    # Creates empty list for who passed and who failed an exam
    pass_failed = []

    # Determines if a student passed (true) and if a student
    # fails (false) each exam
    # Assigns this to the pass_failed list
    for i in range(len(scores)):

        # 60 is the passing grade
        pass_failed.append(scores[i] >= 60)

    # A list of the number of students who passed each exam
    passed = np.sum(pass_failed, axis=0)
    # A list of the number of students who failed each exam
    failed = np.size(pass_failed, axis=0) - passed

    # returns both passed and failed lists
    return passed, failed

def get_percent(scores):
    import numpy as np

    # Creates an empty list for the number of exams each student passes
    passing = []

    # Determines how many exams each student passes
    for i in range(len(scores)):

        # 60 is the passing grade
        passing.append(np.sum(scores[i] >= 60))

    # Gets the total number of exams
    total = np.size(scores)

    # Sums all passing exams
    # Gets the percent of the number of passing exams
    percent = (sum(passing) / total) * 100

    # Returns the percent
    return percent

if __name__ == "__main__":
    main()