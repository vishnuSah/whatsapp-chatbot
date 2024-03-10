from flask import Flask, request
from twilio.rest import Client
from nifty import get_stock_price
from configuration import cfg 
import pdb
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

apiconfig = cfg.get_keys()
ACCOUNT_ID = apiconfig['API_KEYS']['ACCOUNT_ID']
AUTH_TOKEN = apiconfig['API_KEYS']['AUTH_TOKEN']
# print(ACCOUNT_ID)
# print(AUTH_TOKEN)

TWILIO_NUMBER = 'whatsapp:+14155238886'

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

def process_msg(msg):
    response = ''
    if msg == 'hi' or msg == 'Hi':
        response = 'Hi welcome to stock market bot! \nPlease type sym:<stock symbol> for stock price'
    elif 'sym' in msg:
        ticker = msg.split(':')[1]
        stock_price = get_stock_price(ticker)
        response = stock_price
    else:
        response = 'Please type hi to start conversation...'

    return response


@app.route('/webhook', methods=['POST'])
def twilioApp():
    try:
        f = request.form
        msg = f['Body']
        sender = f['From']
        response = process_msg(msg)
        send_msg(response,sender)
        
        return 'OK', 200
    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    app.run(debug=True)

