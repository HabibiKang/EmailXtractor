import re

# Define a generic email pattern
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Read email addresses from the text file
with open("email.txt", "r") as file:
    lines = file.read()

    # Extract and print valid email addresses
    found_emails = re.findall(email_pattern, lines)

    if found_emails:
        print("Emails found in the file:")
        for email in found_emails:
            print(email)
    else:
        print("No valid email addresses found in the file.")
