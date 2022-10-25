from chalice import Chalice
import requests, json
 
app = Chalice(app_name='tradingview-alerts')
API_KEY = 'PKJOLHODIUJ43UR1RUSN'
SECRET_KEY = 'tg1kV4ibU4r53XE1323axHwVVFiUfpd2LnTh1gxD'
BASE_URL = 'https://paper-api.alpaca.markets'
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
@app.route('/')
def index():
    return{'hello':'world'}
@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    request = app.current_request
    webhook_message = request.json_body
 
    data = {
        'symbol':webhook_message['ticker'],
        'qty':10,
        'side':'buy',
        'type':'limit',
        'limit_price':webhook_message['close'],
        'time_in_force':'gtc',
        'order_class':'bracket',
        'take_profit':{
            "limit_price":webhook_message['close'] * 1.05
        },
        "stop_loss": {
            "stop_price":webhook_message['close'] * 0.98,
        }
    }
 
    r = requests.post(ORDERS_URL, json = data, headers=HEADERS)
    response = json.loads(r.content)
  
    return {
        'message':"I bought the stock!!",
        'webhook_message':webhook_message
        'id':response['id']
        'client_order_id':response['client_order_id']
    }
