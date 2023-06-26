# Write a script to extract email addresses from a given text file.
import re

match = r"[\w]+[\d]*\@[\w]+[\d]*\.\bcom\b$"
email = str(input("Enter an email: ")).strip()
with open("email.txt", "w") as file:
    file.write(email)

with open("email.txt", "r") as file:
    lines = file.read()
    if re.search(match, email) and email in lines:
        print(str(lines))
    else:
        print("No lines detected")
