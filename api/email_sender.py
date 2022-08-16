import os
import boto3
from botocore.exceptions import ClientError

SENDER = "Web Mailer <no-reply@cowboycocktails3.com>"
RECIPIENT = os.environ["EMAIL_RECIPIENT"]
AWS_REGION = os.environ.get("AWS_REGION", "us-west-2")
SUBJECT = "Cowboy Cocktails Inquiry from {name}"
CHARSET = "UTF-8"
BODY_TEXT = """
{name} said:

{message}

This message was sent via the form at https://cowboycocktails3.com/#contact
"""
BODY_HTML = """
<html>
    <head></head>
    <body>
        <p>{name} said:</p>
        <p>{message}</p>
        <p><i>This email was sent via the form at <a href="https://cowboycocktails3.com/#contact">https://cowboycocktails3.com/#contact</a></i></p>
    </body>
</html>
"""

def send_email(name, email, message):
    client = boto3.client('ses',region_name=AWS_REGION)
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
            'CcAddresses': [
                email,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML.format(name=name, message=message),
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT.format(name=name, message=message),
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT.format(name=name),
            },
        },
        Source=SENDER,
    )
