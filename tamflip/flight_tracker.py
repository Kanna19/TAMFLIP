import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tamflip.db import get_db

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
        tracked_flights = db.execute(
            'SELECT email, aircraft, carrier, date_and_time, prev_price '
            'FROM tracked_flights'
        ).fetchall()
        for row in tracked_flights:
            yield {'email': row[0],
                   'aircraft': row[1],
                   'carrier': row[2],
                   'date_and_time': row[3],
                   'prev_price': row[4]}

def send_alerts_to_subscribed_users(app):
    print('Started Cron job which handles sending updates to users')
    for tracked_flight_details in get_tracked_flights(app):
        # TODO: Send api requests.
        send_email(
            tracked_flight_details['email'],
            """
            Aircraft: {}
            Carrier: {}
            Date and time: {}
            Previous price: {}
            """.format(tracked_flight_details['aircraft'],
                       tracked_flight_details['carrier'],
                       tracked_flight_details['date_and_time'],
                       tracked_flight_details['prev_price'])
        )
