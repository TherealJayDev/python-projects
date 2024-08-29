import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587  # Common port for TLS
EMAIL_ADDRESS = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'
RECIPIENT_ADDRESS = 'recipient@example.com'

# Function to send email
def send_email():
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_ADDRESS
    msg['Subject'] = 'Daily Report'

    # Email body
    body = 'This is your daily report. All systems are operational.'
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()

# Schedule the email to be sent daily at a specific time
schedule.every().day.at("09:00").do(send_email)

# Keep the script running and check the schedule
while True:
    schedule.run_pending()
    time.sleep(60)
