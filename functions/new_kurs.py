from pycbrf.toolbox import ExchangeRates
from datetime import datetime

time  = str(datetime.now())[::10]
print(time)

rates = ExchangeRates(str(datetime.now())[::10])
result = rates['EUR']

print(result)