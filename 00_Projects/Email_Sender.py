import pandas as pd
import smtplib
import os
from email.message import EmailMessage

# Excel File Read Karein
df = pd.read_excel('E:/3_Python/100_DaysPython/0Emial/Excel.xlsx', engine="openpyxl")

# SMTP Server Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "muhammadkhuzaimasiddiqui@gmail.com"  # Apna email dalain
SENDER_PASSWORD = "mwjyvwddmxofhzdu_gmail"  # Gmail ka app password


# Email Setup
for index, row in df.iterrows():
    receiver_email = row["Email"]
    invoice_path = row["Invoice"]

    # Check karein ke invoice file mojood hai ya nahi
    if not os.path.exists(invoice_path):
        print(f"Error: File {invoice_path} not found. Skipping email to {receiver_email}")
        continue  # Agle student par move karein

    # Email Message Create Karein
    msg = EmailMessage()
    msg["Subject"] = "Your Invoice"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg.set_content(f"Dear {row['Name']},\n\nAttached is your invoice.\n\nBest regards,\nYour Company")

    # Invoice Attach Karein
    with open(invoice_path, "rb") as file:
        file_data = file.read()
        file_name = os.path.basename(invoice_path)  # File ka sirf naam extract karein
        msg.add_attachment(file_data, maintype="image", subtype="png", filename=file_name)

    # SMTP Server Ke Zariye Email Send Karein
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {receiver_email} with invoice {file_name}")
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")
