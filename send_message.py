from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console

account_sid = 'ACd9635007863867a4d72b9ec6b3875931'
auth_token = '611f48880cfbf719a945dc1673f2cde1'
numbers = ["+919748978812", "+918878339946"]
whatsapp_source = "+14155238886"
sms_source = "+18123591204"
payload = 'The video(s) you have uploaded are ready to be tagged. Please go to this webapp to start tagging. https://www.google.co.in/'


def send_message():
    client = Client(account_sid, auth_token)
    for n in numbers:
        whatsapp_message = client.messages.create(
                                    body=payload,
                                    from_='whatsapp:' + whatsapp_source,
                                    to='whatsapp:' + n
                                )
        print("Success on Whatsapp : " + whatsapp_message.sid)
        sms_message = client.messages.create(
                                body=payload,
                                from_=sms_source,
                                to=n
                            )

        print("Success on SMS : " + sms_message.sid)