import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from itsdangerous import URLSafeSerializer, BadData
from flask import url_for, render_template

from tamflip.db import get_db
from . import api_module

import jinja2

from selenium import webdriver

def take_screenshot(url, image_file):
    print("\n\n-----TOOK PICTURE----\n\n")

    url = "http://"+url

    op = webdriver.ChromeOptions()
    op.add_argument("--start-maximized")
    op.add_argument("--start-fullscreen")

    driver = webdriver.Chrome("./chromedriver", options=op)
    driver.get(url)
    driver.save_screenshot(image_file)
    driver.quit()


def send_email(receiver_email, image_file, flightstatus_url, unsub_url):
    """
    Function to send email to the given receiver email id.
    Provide sender credentials in the file credentials.txt
    """
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    with open('credentials.txt') as f:
        credentials = {k: v for k, v in map(str.split, f.readlines())}
        sender_email = credentials['EMAIL']
        app_password = credentials['APP_PASSWORD']

    # #Create email screenshot
    # take_screenshot(url=url, image_file=image_file)

    message = MIMEMultipart()
    message['Subject'] = 'Test email'
    message['From'] = sender_email
    message['To'] = receiver_email

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    message_alt = MIMEMultipart('alternative')
    message.attach(message_alt)
    message_alt.attach(MIMEText('Image showing status of your tracked flight'))

    # We reference the image in the IMG SRC attribute by the ID we give it below
    message_alt.attach(
        MIMEText(
            """
            <h2>Price updates</h2> <br>
            <img src="cid:image_updates">
            <footer>
                <a href="%s"> Manage your flights </a> <br>
                <a href="%s"> Check the current prices of your tracked flights </a>
            </footer>
            """ % (unsub_url, flightstatus_url),
            'html'
        )
    )

    with open(image_file, 'rb') as f:
        message_img = MIMEImage(f.read())

    # Define the image's ID as referenced above
    message_img.add_header('Content-ID', '<image_updates>')
    message.attach(message_img)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        print('Connection established to Gmail SMTP server')
        server.login(sender_email, app_password)
        print('Login done.')
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('Sent email to %s' % receiver_email)

def generate_user_token(email, salt):
    with open('credentials.txt') as f:
        credentials = {k: v for k, v in map(str.split, f.readlines())}
        server_secret = credentials['SERVER_SECRET']

    serializer = URLSafeSerializer(server_secret, salt=salt)
    return serializer.dumps(email)

def get_user_emails(app):
    """Returns all the user emails present in the database"""
    with app.app_context():
        db = get_db()
        cursor = db.execute(
            """
            SELECT DISTINCT email
            FROM tracked_flights
            """
        )
        return [row[0] for row in cursor.fetchall()]

def get_tracked_flights(app, email):
    """Returns all the flights tracked by given email"""
    with app.app_context():
        db = get_db()
        cursor = db.execute(
            """
            SELECT *
            FROM tracked_flights
            WHERE email = ?
            """,
            (email,)
        )
        column_names = list(map(lambda x: x[0], cursor.description))
        return [{k: v for k, v in zip(column_names, tuple(row))}
                for row in cursor.fetchall()]

def send_alerts_to_subscribed_users(app):
    print('Started Cron job which handles sending updates to users')
    for email in get_user_emails(app):
        base_url = '127.0.0.1:5000'
        image_file = 'tamflip/static/images/tempimage.png'

        take_screenshot(
            base_url + '/flightstatus/' + generate_user_token(email, 'flightstatus'),
            image_file
        )

        send_email(
            email,
            image_file=image_file,
            flightstatus_url=(
                base_url
                + '/flightstatus/'
                + generate_user_token(email, 'flightstatus')
            ),
            unsub_url=(
                base_url
                + '/unsubscribe/'
                + generate_user_token(email, 'unsubscribe')
            )
        )
