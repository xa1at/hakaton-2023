from pycbrf.toolbox import ExchangeRates
from datetime import datetime
from functions.function_get_datetime import *

ltime = datetime.now()
temptime = str(ltime)
time = temptime[:10]
allvaluti = ExchangeRates(time)


def function_return_valutes():
    usd = allvaluti['USD']
    eur = allvaluti['EUR']
    gbp = allvaluti['GBP']  # фунты
    kzt = allvaluti['KZT']  # тенге
    gel = allvaluti['GEL']  # лари грузия
    tr_y = allvaluti['TRY']  # лира
    cny = allvaluti['CNY']  # юань
    jpy = allvaluti['JPY']  # йена
    return usd, eur, gbp, kzt, gel, tr_y, cny, jpy
