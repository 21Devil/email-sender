import re
import sys
import smtplib
from random import choice
from csv import DictReader

QUOTES_CSV_FILE = "quotes.csv"
NO_OF_ARGUMENTS = 4


def main():
    
    sender_email, app_password, receiver_email = parse_arguments()

    # Check if email is valid email or not.
    if email_check(str(sender_email)) and email_check(str(receiver_email)):
        print("The email is valid....")
    else:
        print("InputError: Enter valid email address.")
        sys.exit(1)

    sending_email(sender_email, app_password, receiver_email)


# Function to return arguments as strings if valid.
def parse_arguments():
    if len(sys.argv) != NO_OF_ARGUMENTS:
        print("Usage: python script.py sender_email app_password receiver_email")
        sys.exit(1)

    from_addr = sys.argv[1]
    password = sys.argv[2]
    to_addr = sys.argv[3]

    return from_addr, password, to_addr


# Function to check if email is valid.
def email_check(email):
    # Defining a regular expression pattern for basic email validation.
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    # Checking if email matches the pattern.
    if re.match(pattern, email):
        return True
    else:
        return False


# Function to send a random quote out of 1665 quote as an email.
def sending_email(from_addr, password, to_addr):

    # TODO: read each quote in csv file and store in array.
    quotes = []
    with open(QUOTES_CSV_FILE, 'r') as file:
        readline = DictReader(file)

        for row in readline:
            quotes.append(row["Quote"])

    # TODO: randomly pick a quote from array.
    quote = choice(quotes)

    # TODO: send the email to user with that quote as message.
    # Spend hrs figuring out that ,  creates tupule and + concatinates.
    msg = "Quote of the day!\n\n" + quote
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    print("Login Success")
    server.sendmail(from_addr, to_addr, msg)
    print("Email has been send to : ", to_addr)


if __name__ == "__main__":
    main()
