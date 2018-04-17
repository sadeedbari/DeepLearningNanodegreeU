from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7a671e342fa28c7d09422e73b0da6ca2"
# Your Auth Token from twilio.com/console
auth_token  = "b9f090d1e60d01018976a9d41ab005a5"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16477874204", 
    from_="+16477995504",
    body="This is special agent X52495!")

print(message.sid)
