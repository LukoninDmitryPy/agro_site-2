import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


APIKEY = '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'


message = Mail(
    from_email='muxa2k11@gmail.com',
    to_emails='mikushnerev@stud.etu.ru',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(APIKEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
