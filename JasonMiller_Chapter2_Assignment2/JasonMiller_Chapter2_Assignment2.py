# This program checks emails received from users and indicates
# how likely it is to be a scam and what caused the email to be considered spam.
def main():

    # List of spam phrases
    spam_phrases = ["Best price", "100% free", "Cash bonus", "Join Millions", "No fees",
                    "Earn money", "% Off", "Fast cash", "Free gift", "Free access",
                    "Free trial", "Giveaway", "Guaranteed", "Incredible deal", "Lowest price",
                    "Money back", "Prize", "Save up to", "Special promotion", "Click here",
                    "Call now", "Click below", "Get started now", "Weight loss", "Limited time",
                    "Sign up free", "Urgent", "You have been selected", "Congratulations", "Passwords",]

    # Receives email from user.
    get_email = str(input("Input a email: "))

    # Splits the email into individual words.
    email_word_count = get_email.split()

    # Sends the email and spam phrase list to get_spam_score function
    # Assigns results to "spam_score" variable
    spam_score = get_spam_score(get_email, spam_phrases)

    # assigns the spam score to "user_spam_score" variable
    user_spam_score = (spam_score[0])

    # Assigns the flagged spam phrases to "caused_phrases" variable
    caused_phrases = (", ".join(spam_score[1][0:]))

    # Sends over the individual words of the email and spam score
    # to "get_likelihood variable"
    # Assigns the result to "percent" variable
    percent = get_likelihood(email_word_count, spam_score[0])

    # Displays the spam score, spam likelihood, and flagged phrases.
    print(f'Your spam score: {user_spam_score}')
    print(f'Spam likelihood: {percent:.1f}%')
    print(f'Flagged words/phrases: {caused_phrases}')

def get_spam_score(email, phrases):
    # Sets an accumulator
    spam_score = 0

    # Sets an empty list for flagged phrases
    words_found = []

    # Loops into the spam phrases list
    for phrase in phrases:
        # If it detects a spam phrase in the email, spam_score gets a point
        # and the flagged phrase appends into the empty list
        if phrase.lower() in email.lower():
            spam_score += 1
            words_found.append(phrase)

    # Returns the spam score and words found
    return spam_score, words_found

def get_likelihood(email, spam_count):

    # Proceeds if there is at least 1 word in the email.
    if len(email) > 0:

        # Gets the percentage of spam words in the email
        likelihood = (spam_count / len(email)) * 100

        # Returns this percentage
        return likelihood

    # Exits the code if there are 0 words
    else:
        print('Cannot have 0 words')
        exit()
if __name__ == "__main__":
    main()