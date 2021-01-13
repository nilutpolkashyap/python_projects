from twilio.rest import Client 
  

account_sid = 'account_sid_from_twilio_dashboard'
auth_token = 'auth_token_from_twilio_dashboard'
  
client = Client(account_sid, auth_token) 
  
message = client.messages.create( 
                              from_='my_phone_number', 
                              body ='Hello this Nilutpol. I am using the Twilio API in Python to send an SMS. I am 
                              participating in the MLH local hack day build challenges. Happy Hacking......', 
                              to ='receiver_phone_number'
                          ) 
  
print(message.sid) 
