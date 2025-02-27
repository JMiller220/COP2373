# This program receives, counts, and displays each sentence of a paragraph.

import re
def main():

    # Calls and assigns the result of get_paragraph function
    paragraph = get_paragraph()

    # Calls the get_sentence function
    get_sentence(paragraph)

def get_paragraph():

    # Prompts the user to enter a paragraph
    user_p = str(input("Enter a paragraph: "))

    # Returns the paragraph
    return user_p

def get_sentence(paragraph):

    # Creates an accumulator
    s_count = 1

    # Defines a sentence pattern
    pattern = r"""[A-Z0-9"'].*?[.?!](?= [A-Z0-9"']|$| )"""

    # Finds all the sentences the paragraph that match the pattern
    sentence = re.findall(pattern, paragraph, flags=re.DOTALL|re.MULTILINE)

    # Loops through all the sentences
    for i in sentence:

        # Displays each sentence along with its sentence number
        print(f"{s_count}. {i}")

        # Adds one to the accumulator
        s_count += 1

if __name__ == "__main__":
    main()