import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Name validation
while True:
    pattern = re.compile(r'^[A-Za-z ]+$')
    name = input("Enter Name: ")
    if pattern.fullmatch(name):
        break
    else:
        print("Enter Name in correct format (only letters and spaces).")

# Date of birth validation
while True:
    pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
    dob = input("Enter Date of Birth (DD-MM-YYYY): ")
    if pattern.fullmatch(dob):
        break
    else:
        print("Enter DOB in correct format (DD-MM-YYYY).")

# Mobile number validation
while True:
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    phone = input("Enter Mobile Number (XXX-XXX-XXXX): ")
    if pattern.fullmatch(phone):
        break
    else:
        print("Enter Mobile Number in correct format (XXX-XXX-XXXX).")

# Email validation
while True:
    pattern = re.compile(r'^[a-zA-Z0-9]+@gmail\.com$')
    email = input("Enter Email: ")
    if pattern.fullmatch(email):
        break
    else:
        print("Enter Email in correct format (example@gmail.com).")

# Instagram ID (no validation needed)
insta = input("Enter Insta ID: ")

print("\nAll details verified successfully!\n")

# Sending email
sender_email = "chandrikachavva5@gmail.com" 
sender_password = "jdlg nmbg kbwp vrak"  

subject = "Registration Successful"
body = f"""
Hello {name},

Thank You for Registering with us!

Here are your details:
- Name: {name}
- Date of Birth: {dob}
- Mobile: {phone}
- Instagram ID: {insta}
- Email: {email}

If this wasn't you, please ignore this email.
"""

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, email, msg.as_string())
    server.quit()
    print("Email sent successfully to", email)
except Exception as e:
    print("Error sending email:", e)
