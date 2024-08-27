import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Email configuration
EMAIL_ADDRESS = 'vrobert997@yahoo.com'
EMAIL_PASSWORD = 'jenanqebkhkwpqit'  # Generated password key in yahoo account settings
SMTP_SERVER = 'smtp.mail.yahoo.com'  # Yahoo SMTP server
SMTP_PORT = 587  # SMTP port for Yahoo

def create_email(subject, body, from_address, to_address, bcc_addresses):
    # Create a multipart message
  
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = '#HealthyLiveStyle@itPAT.co.za' #to_address
    msg['Subject'] = subject

    # Set Bcc recipients
    if bcc_addresses:
        msg['Bcc'] = ', '.join(bcc_addresses)

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    return msg

def send_email(from_address, to_address, bcc_addresses, subject, body):
    msg = create_email(subject, body, from_address, to_address, bcc_addresses)
    
    try:
        # Connect to the server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        
        # Login to the email account
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Send the email
        server.send_message(msg)
        
        #print(f"Email sent to {to_address}")
        print(f'Email Chunk of {chunk_size} sent.')
        
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")
        
    finally:
        server.quit()

def send_emails_to_list(file_path):
    try:
        with open(file_path, 'r') as file:
            email_addresses = [email.strip() for email in file.readlines() if email.strip()]
        
        subject = "IT PAT Healthy Living Test"
        file_path = 'K:\Graad 11\PAT2024_VanDerSpoelRobert\IT11_PAT2024_Fase2_SurnameName\Email\email_test.txt'
        
        with open(file_path, 'r') as file:
            body = file.read()
        global chunk_size
        chunk_size = 50
        for i in range(0, len(email_addresses), chunk_size):
            chunk = email_addresses[i:i + chunk_size]
            
            if chunk:
                to_address = chunk[0]  # First recipient in the chunk goes in the To field
                bcc_addresses = chunk[1:]  # Remaining recipients go in the Bcc field
                
                send_email(EMAIL_ADDRESS, to_address, bcc_addresses, subject, body)
               # From = 'Healthy Living News'  # Replace this with the name of the Company/app + newsletter
              #  send_email(From, to_address, bcc_addresses, subject, body)
                time.sleep(2)  # Delay to avoid rate limiting between chunks
            
    except Exception as e:
        print(f"Failed to read email list file or send emails: {e}")

if __name__ == "__main__":
    email_list_path = r"K:\Graad 11\PAT2024_VanDerSpoelRobert\IT11_PAT2024_Fase2_SurnameName\Email\email_addresslist_test.txt"  # Update this path to your email list file
    send_emails_to_list(email_list_path)
