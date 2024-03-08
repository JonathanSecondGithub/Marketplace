import africastalking

# TODO: Initialize Africa's Talking
username = 'sandbox'
api_key = 'bbf7fd98429d1ae96fd33237fd57fb5a4b3b9a6fd6d1f360f2f651d9247c8fef'
africastalking.initialize(username, api_key)

sms = africastalking.SMS

class send_sms(): 
    #TODO: Send message
    def sending(self):
        # Set the numbers in international format
        recipients = ["+254790313572"]
        # Set your message
        message = "Hey AT Ninja!";
        # Set your shortCode or senderId
        sender = "29874"
        try:
            response = self.sms.send(message, recipients, sender)
            print (response)
        except Exception as e:
            print (f'Houston, we have a problem: {e}')