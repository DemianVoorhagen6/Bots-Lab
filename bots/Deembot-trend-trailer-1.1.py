# Imports of external modules come here
import talib

# Imports of internal modules comes here
# When you want to change the buy_signal_settings from within the get_buy_or_sell_signal function import config_test or config_live
# See https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules

# Global variables come here.
# Global variables can be used to store values for later use.
# See https://www.w3schools.com/python/gloss_python_global_variables.asp

def get_buy_or_sell_signal(data):

    # skip when the number of rows (candles) is too short
    if len(data) < 2:
        return None

    # get the last and second to last row
    current_candle = data.iloc[-1]
    previous_candle = data.iloc[-2]

    macd, macdsignal, macdhist = talib.MACD(data['close'].values, fastperiod=12, slowperiod=26, signalperiod=9)
    minus_di = talib.MINUS_DI(data['high'].values, data['low'].values, data['close'].values, timeperiod=14)
    plus_di = talib.PLUS_DI(data['high'].values, data['low'].values, data['close'].values, timeperiod=14)
    sar = talib.SAR(data['high'].values, data['low'].values, acceleration=0.001, maximum=0.2)

    if macdhist[-1] > 0 and plus_di[-1] > minus_di[-1]:
        return 'buy'
    elif macdhist[-1] < 0 and plus_di[-1] > minus_di[-1]:
        return 'sell'
    else:
        return None