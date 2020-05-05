import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tamflip.db import get_db
from . import api_module

def send_email(receiver_email, details=''):
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
    text = details
    html = """\
    <html>
      <body>
        <p>Hoi,<br>
           This is the html part.<br>
           <a href="https://www.youtube.com/watch?v=RcMQuy1ObeY"> Check this out!! </a>
        </p>
        <h3> Sent from apscheduler triggered cron job. Jai kc </h3>
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

def get_tracked_flights(app):
    """Generator function to get the tracked flight details"""
    with app.app_context():
        db = get_db()
        cursor = db.execute('SELECT * FROM tracked_flights')
        column_names = list(map(lambda x: x[0], cursor.description))
        for row in cursor.fetchall():
            yield {
                k: v
                for k, v in zip(column_names, tuple(row))
            }

def send_alerts_to_subscribed_users(app):
    print('Started Cron job which handles sending updates to users')
    for tracked_flight_details in get_tracked_flights(app):
        flight_details, price_details = api_module.query_tracked_flight(
            tracked_flight_details
        )
        # Flight not found.
        # TODO: Handle this case properly
        if flight_details is None:
            continue

        print('Flight details retrieved.')

        # Dummy email body
        email_body = (
            tracked_flight_details['from_location']
            + ' to '
            + tracked_flight_details['to_location'] + '\n'
            + '\n'.join([(k + ': ' + v) for k, v in flight_details[0].items()])
        )

        if len(flight_details) == 2:
            email_body += (
                '\n' + tracked_flight_details['to_location']
                + ' to '
                + tracked_flight_details['from_location'] + '\n'
                + '\n'.join([(k + ': ' + v) for k, v in flight_details[1].items()])
            )

        email_body += '\nCost: ' + price_details
        send_email(tracked_flight_details['email'], email_body)
