import requests


def get_currency_rates():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=usd,eur&vs_currencies=rub'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        usd_rate = data['usd']['rub']
        return usd_rate
    else:
        return None


def convert_to_rub(amount, rate):
    return amount * rate


def print_currency_info(kol):
    usd = get_currency_rates()
    if usd:
        return f"1 доллар = {usd} рублей"
        amount = kol
        rub_amount_usd = convert_to_rub(amount, usd)
        return f"{amount} долларов = {rub_amount_usd} рублей"



