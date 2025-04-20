'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import schedule
#import time

# Email configuration
EMAIL_ADDRESS = ''
EMAIL_PASSWORD = ''     # Generated password key in yahoo account settings.
TO_ADDRESS = ['']           
 # Perhaps loop thru a txt file to with email addresses to send emails to a broad range of people. For the newsletter for example  
 # Only a single address if you want to verify a person or something
SMTP_SERVER = 'smtp.mail.yahoo.com'  # Yahoo SMTP server
SMTP_PORT = 587  # SMTP port for Yahoo

def create_email():
    # Create the email content
    subject = "Daily Report Test"
    #file = open('email_test.txt', 'r') 
    file = open('email_test.txt', 'r') 
    
    body = file.read()  # Can also use a string here
    file.close()

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] =  TO_ADDRESS
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    return msg

def send_email():
    msg = create_email()
    
    try:
        # Connect to the server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        
        # Login to the email account
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Send the email
        server.send_message(msg)
        
        print(f"Email sent to {TO_ADDRESS}")
        
    except Exception as e:
        print(f"Failed to send email: {e}")
        
    finally:
        server.quit()

'''
def schedule_daily_email():
    # Schedule the email to be sent daily at a specific time
    schedule.every().day.at("12:05").do(send_email)

    while True:
        schedule.run_pending()
        time.sleep(1)
''' 
if __name__ == "__main__":
   # schedule_daily_email()
   send_email()
   
   
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
EMAIL_ADDRESS = 'vrobert997@yahoo.com'
EMAIL_PASSWORD = 'ttnukqndcirmvwyn'  # Use a more secure method to store this
TO_ADDRESS = ['robertvdspoel2007@gmail.com', '10867@hsrandburg.co.za']  # List of recipients
SMTP_SERVER = 'smtp.mail.yahoo.com'
SMTP_PORT = 587

def create_email(recipient):
    # Create the email content from a file
    subject = "Daily Report Test"
    with open('email_test.txt', 'r') as file:
        body = file.read()

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    return msg

def send_email():
    for recipient in TO_ADDRESS:
        msg = create_email(recipient)
        
        try:
            # Connect to the server
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            
            # Login to the email account
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            
            # Send the email
            server.send_message(msg)
            
            print(f"Email sent to {recipient}")
            
        except Exception as e:
            print(f"Failed to send email to {recipient}: {e}")
            
        finally:
            server.quit()

if __name__ == "__main__":
    send_email()
