# sms-greeter
Example Flask app serving as a Twilio webhook

The app contains just a single POST endpoint:
* `/receive_sms`

Upon receiving an SMS message via Twilio, it will return a simple TwiML greeting.
