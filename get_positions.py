# Ryuryu's Bybit Positions Saver
###################################
# Ryan Hayabusa 2017-2022 
# GitGub: https://github.com/ryu878
# Web: https://aadresearch.xyz
# Discord: ryuryu#4087
###################################

import time
import sqlite3
from inspect import currentframe
from pybit import usdt_perpetual
from datetime import datetime



title = 'Ryuryu\'s Bybit Positions Saver'
ver = '1.0'


assets = ['BTCUSDT','ETHUSDT','XRPUSDT'] 
endpoint = 'https://api.bybit.com'
api_key = 'YOUR_API_KEY_HERE'
api_secret = 'AND_SECRET_HERE'


terminal_title = title+ver
print(f'\33]0;{terminal_title}\a', end='', flush=True)

client = usdt_perpetual.HTTP(endpoint=endpoint, api_key=api_key, api_secret=api_secret)


def get_linenumber():
    cf = currentframe()
    global line_number
    line_number = cf.f_back.f_lineno


while True:

    for symbol in assets:

        def get_position():
            # https://bybit-exchange.github.io/docs/futuresV2/linear/#t-myposition
            positions = client.my_position(symbol=symbol)
            
            for position in positions['result']:

                if position['side'] == 'Sell':

                    global sell_position_size
                    global sell_position_prce
                    global sell_position_liq_price
                    global sell_position_leverage
                    global sell_position_realised_pnl
                    global sell_position_unrealised_pnl
                    global sell_position_position_margin
                    global sell_position_occ_closing_fee
                    global sell_position_risk_id
                    global sell_position_stop_loss
                    global sell_position_take_profit

                    sell_position_size = position['size']
                    sell_position_prce = position['entry_price']
                    sell_position_liq_price = position['liq_price']
                    sell_position_leverage = position['leverage']
                    sell_position_realised_pnl = position['realised_pnl']
                    sell_position_unrealised_pnl = position['unrealised_pnl']
                    sell_position_position_margin = position['position_margin']
                    sell_position_occ_closing_fee = position['occ_closing_fee']
                    sell_position_risk_id = position['risk_id']
                    sell_position_stop_loss = position['stop_loss']
                    sell_position_take_profit = position['take_profit']


                if position['side'] == 'Buy':

                    global buy_position_size
                    global buy_position_prce
                    global buy_position_liq_price
                    global buy_position_leverage
                    global buy_position_realised_pnl
                    global buy_position_unrealised_pnl
                    global buy_position_position_margin
                    global buy_position_occ_closing_fee
                    global buy_position_risk_id
                    global buy_position_stop_loss
                    global buy_position_take_profit

                    buy_position_size = position['size']
                    buy_position_prce = position['entry_price']
                    buy_position_liq_price = position['liq_price']
                    buy_position_leverage =position['leverage']
                    buy_position_realised_pnl = position['realised_pnl']
                    buy_position_unrealised_pnl = position['unrealised_pnl']
                    buy_position_position_margin = position['position_margin']
                    buy_position_occ_closing_fee = position['occ_closing_fee']
                    buy_position_risk_id = position['risk_id']
                    buy_position_stop_loss = position['stop_loss']
                    buy_position_take_profit = position['take_profit']

        
        try:
            get_position()
        except Exception as e:
            get_linenumber()
            print(line_number, 'exeception: {}'.format(e))
            pass


        # print(symbol)
        # print('Sell position:',sell_position_size,sell_position_prce)
        # print(' Buy position:',buy_position_size,buy_position_prce)

        try:               

            conn = sqlite3.connect('positions.db')
            cursor = conn.cursor()
            conn.execute("""
                    CREATE TABLE IF NOT EXISTS positions (
                    symbol text UNIQUE PRIMARY KEY NOT NULL,
                    sell_position_size real,
                    sell_position_prce real,
                    sell_position_liq_price real,
                    sell_position_leverage real,
                    sell_position_realised_pnl real,
                    sell_position_unrealised_pnl real,
                    sell_position_position_margin real,
                    sell_position_occ_closing_fee real,
                    sell_position_risk_id real,
                    sell_position_stop_loss real,
                    sell_position_take_profit real,     
                    buy_position_size real,
                    buy_position_prce real,
                    buy_position_liq_price real,
                    buy_position_leverage real,
                    buy_position_realised_pnl real,
                    buy_position_unrealised_pnl real,
                    buy_position_position_margin real,
                    buy_position_occ_closing_fee real,
                    buy_position_risk_id real,
                    buy_position_stop_loss real,
                    buy_position_take_profit real
                    )""")

            sqlite_update = """
                    INSERT OR REPLACE INTO positions (
                    symbol, 
                    sell_position_size,
                    sell_position_prce,
                    sell_position_liq_price,
                    sell_position_leverage,
                    sell_position_realised_pnl,
                    sell_position_unrealised_pnl,
                    sell_position_position_margin,
                    sell_position_occ_closing_fee,
                    sell_position_risk_id,
                    sell_position_stop_loss,
                    sell_position_take_profit,
                    buy_position_size,
                    buy_position_prce,
                    buy_position_liq_price,
                    buy_position_leverage,
                    buy_position_realised_pnl,
                    buy_position_unrealised_pnl,
                    buy_position_position_margin,
                    buy_position_occ_closing_fee,
                    buy_position_risk_id,
                    buy_position_stop_loss,
                    buy_position_take_profit
                    ) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """
            
            data_tuple = (symbol,\
                sell_position_size,\
                sell_position_prce,\
                sell_position_liq_price,\
                sell_position_leverage,\
                sell_position_realised_pnl,\
                sell_position_unrealised_pnl,\
                sell_position_position_margin,\
                sell_position_occ_closing_fee,\
                sell_position_risk_id,\
                sell_position_stop_loss,\
                sell_position_take_profit,\
                buy_position_size,\
                buy_position_prce,\
                buy_position_liq_price,\
                buy_position_leverage,\
                buy_position_realised_pnl,\
                buy_position_unrealised_pnl,\
                buy_position_position_margin,\
                buy_position_occ_closing_fee,\
                buy_position_risk_id,\
                buy_position_stop_loss,\
                buy_position_take_profit)

            cursor.execute(sqlite_update, data_tuple)
            time.sleep(0.1)
            
        except Exception as e:
            print('exeception: {}'.format(e))
            pass
                
        conn.commit()
        conn.close()


    print(' Positions saved to DB')
    print(datetime.now().strftime("  %H:%M:%S")) 

    time.sleep(33)
