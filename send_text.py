from twilio.rest import TwilioRestClient

account_sid = "ACa57d401349d04a0587cb18edd27f7231" # Your Account SID from www.twilio.com/console
auth_token  = "e51511a64946781665b940799598177b"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)
print "running!!"
message = client.messages.create(body="Hello from Python",
    to="+13056328199",    # Replace with your phone number
    from_="+17865075323") # Replace with your Twilio number

print(sms.sid)
print(message.sid)