from twilio.rest import Client

account_sid = "AC9269aa85146bc986a89c2db53a3d8dc7"
auth_token = "1d4216607be123be4fbccf2f7762fe9b"

client = Client(account_sid, auth_token)

client.messages.create(
    to="+16145636712",
    from_="+18336590732",
    body="first text message!"
)
