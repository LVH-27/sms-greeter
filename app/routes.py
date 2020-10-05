from flask import request
from app import webhook_app
from twilio.twiml.messaging_response import MessagingResponse


@webhook_app.route('/receive_sms/', methods=['POST'])
def receive_sms():
    sms = request.values
    sender = sms['From']
    response = MessagingResponse()
    response.message("I received a message from {}! Hi!".format(sender))
    return str(response)
