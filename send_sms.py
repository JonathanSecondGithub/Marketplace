import africastalking

# TODO: Initialize Africa's Talking
username = ''
api_key = ''
africastalking.initialize(username, api_key)

sms = africastalking.SMS

class send_sms(): 
    #TODO: Send message
    def sending(self):
        # Set the numbers in international format
        recipients = ["+2547"]
        # Set your message
        message = "Hey AT Ninja!";
        # Set your shortCode or senderId
        sender = ""
        try:
            response = self.sms.send(message, recipients, sender)
            print (response)
        except Exception as e:
            print (f'Houston, we have a problem: {e}')
