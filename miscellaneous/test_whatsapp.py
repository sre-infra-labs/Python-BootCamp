import os
from twilio.rest import Client

def send_test_whatsapp_message():
    # Your Account SID and Auth Token from twilio.com/console
    # Set these as environment variables for security.
    # Example: export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    # Your Twilio WhatsApp number and the recipient's number
    # Both numbers must be in the correct format with the 'whatsapp:' prefix.
    # e.g., 'whatsapp:+14155238886' for Twilio, and 'whatsapp:+15551234567' for the recipient.
    from_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")
    to_whatsapp_number = os.getenv("RECIPIENT_WHATSAPP_NUMBER")
    
    # Check if all environment variables are set
    if not all([account_sid, auth_token, from_whatsapp_number, to_whatsapp_number]):
        print("Please set your environment variables for Twilio.")
        print("Ensure TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER, and RECIPIENT_WHATSAPP_NUMBER are configured.")
        return

    try:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Hello from your Python script! This is a test message. 🎉",
            from_=from_whatsapp_number,
            to=to_whatsapp_number
        )

        print(f"Message sent successfully! SID: {message.sid}")
        print(f"Check your WhatsApp for a message from {from_whatsapp_number}.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your credentials and phone numbers.")
        print("Make sure your recipient number is enrolled in the Twilio Sandbox or approved for production.")

if __name__ == "__main__":
    send_test_whatsapp_message()