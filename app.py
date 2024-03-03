from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

TWILIO_NUMBER = 'whatsapp:+14155238886'
ACCOUNT_ID = 'AC24bfce27f12fbb677e5a586795262849'
AUTH_TOKEN = 'b892316cee0e3611ec2c91f4c41fb343'

client = Client(ACCOUNT_ID, AUTH_TOKEN)

@app.route('/')
def hello():
    
    response ={
        'Bolo':"Jai Shree Ram"
    }
    return response

def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )

    # response = {
    #     'from': TWILIO_NUMBER,
    #     'message':msg,
    #     'To':recipient
    # }
    # return response

def process_msg(msg):
    response = ''
    if msg == 'hi':
        response = 'Hi welcome to stock market bot!'
    else:
        response = 'Please type hi to start conversation...'

    return response


@app.route('/webhook', methods=['POST'])
def twilioApp():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response,sender)
    
    return 'OK', 200
    


if __name__ == '__main__':
    app.run(debug=True)

