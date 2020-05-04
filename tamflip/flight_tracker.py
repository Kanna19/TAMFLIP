import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email, details=None):
    """
    Function to send email to the given receiver email id.
    Provide sender credentials in the file credentials.txt
    """
    # TODO: Email structure.
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    with open('credentials.txt') as f:
        sender_email, app_password = f.readline().split()

    message = MIMEMultipart()
    message['Subject'] = 'Test email'
    message['From'] = sender_email
    message['To'] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Email from python script boi.
    This is the text part.
    """
    html = """\
    <html>
      <body>
        <p>Hoi,<br>
           This is the html part.<br>
           <a href="https://www.youtube.com/watch?v=RcMQuy1ObeY"> Check this out!! </a>
        </p>
        <h1> boi </h1>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        print('Connection established to Gmail SMTP server')
        server.login(sender_email, app_password)
        print('Login done.')
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('Sent email to %s' % receiver_email)

def send_alerts_to_subscribed_users():
    # TODO:
    # 1. Read user subsricption database
    # 2. Send api requests.
    # 3. send email updates.
    pass
