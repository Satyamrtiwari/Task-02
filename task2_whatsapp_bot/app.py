from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from scraper import get_latest_news

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    """Respond to incoming WhatsApp messages."""
    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg == "hello":
        msg.body("Hi there! 👋 Send 'news' to get the latest headlines.")
    elif incoming_msg == "news":
        headlines = get_latest_news()
        if headlines:
            msg.body("\n".join(headlines))
        else:
            msg.body("Sorry, I couldn't fetch news right now.")
    else:
        msg.body("I didn't understand that. Try 'hello' or 'news'.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
