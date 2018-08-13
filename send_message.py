from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console

account_sid = '*PUT TWILIO ACCOUND SID*'
auth_token = '*PUT TWILIO AUTH TOKEN*'
numbers = ["*PUT VERIFIED PHONE NUMBERS AS RECIPIENTS*"]
whatsapp_source = "*WHATSAPP SOURCE NUMBER*"
sms_source = "*SMS SOURCE NUMBER*"
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
