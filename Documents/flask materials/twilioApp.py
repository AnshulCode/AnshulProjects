from twilio.rest import Client

def sendSMS(messageTS):
    account_sid = "AC1766b2e8c2be0cde6644e69ce3c686b9"
    auth_token = "2e734614fc62eeb5d7f38b3e56ff34e5"

    client = Client(account_sid,auth_token)

    message = client.messages.create(
    to = "+17323106609",
    from_= "+17323654661", 
    body = messageTS
    )
    sendSMS()