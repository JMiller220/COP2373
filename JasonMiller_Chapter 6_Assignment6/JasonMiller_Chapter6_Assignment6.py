# This program validates or invalidates a given
# phone number, SSN, and zip code to their respective formats.

import re

def main ():

    # Create an initializer
    re_enter = 'y'

    # Loops if re_enter is equal to y
    while re_enter.lower() == 'y':

        # Prompt user to enter a phone number, ssn, and zip code, respectively.
        user_pn = input("Enter Phone Number: ")
        user_ssn = input("Enter Social Security Number: ")
        user_zip = input("Enter last five digits of your Zip Code: ")

        # Assigns the "check_phone_num", "check_ssn", and "check_zip" to variables, respectively
        phone = check_phone_num(user_pn)
        ssn = check_ssn(user_ssn)
        zip_code = check_zip(user_zip)

        # Displays the results of each function
        print()
        print(f"{phone}\n{ssn}\n{zip_code}")
        print()

        # Prompt the user if they would want to re-run this program
        re_enter = input("Want to re-enter? (y/n): ")
        print()
def check_phone_num(p_number):

    # Defines a pattern for a phone number
    pattern = r"\d{3}[ -]\d{3}[ -]\d{4}$"

    # Compare the phone number to the pattern
    if re.match(pattern, p_number):

        # Assign a valid statement to result if the phone number has a valid format
        result = "Phone number accepted!\n"

    else:

        # Assign an invalid statement to result if the phone number has an incorrect format
        result = "Phone number invalid. \nUse ###-###-#### or ### ### ####\n"

    # Return the result.
    return result

def check_ssn(ssn):

    # Defines a pattern for a social security number
    pattern = r"\d{3}[ -]\d{2}[ -]\d{3}$"

    # Compare the social security number to the pattern
    if re.match(pattern, ssn):

        # Assign a valid statement to result if the social security number has a valid format
        result = "SSN accepted!\n"

    else:

        # Assign an invalid statement to result if the social security number has an incorrect format
        result = "SSN invalid. \nUse ###-##-### or ### ## ###\n"

    # Return the result.
    return result

def check_zip(zip_code):

    # Defines a pattern for a zip code
    pattern = r"\d{5}$"

    # Compare the zip code to the pattern
    if re.match(pattern, zip_code):

        # Assign a valid statement to result if the zip code has a valid format
        result = "Zip Code accepted!"

    else:

        # Assign an invalid statement to result if the zip code has an incorrect format
        result = "Zip code invalid. \nUse #####"

    # Return the result.
    return result

if __name__ == "__main__":
    main()