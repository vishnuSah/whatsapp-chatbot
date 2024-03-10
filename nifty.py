import requests
from bs4 import BeautifulSoup

def get_stock_price(ticker):
    try: 
        # ticker = 'TCS'
        url = f'https://www.google.com/finance/quote/{ticker}:NSE'

        response = requests.get(url, verify=False)
        # print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        class_name = 'YMlKec fxKbKc'
        price = float(soup.find(class_=class_name).text[1:].replace(',',''))

        return price
    except Exception as e:
        return 'Please enter correct stock symbol'
