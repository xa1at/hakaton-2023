from datetime import datetime


months_dict = {
    'January': 'января',
    'February': 'февраля',
    'March': 'марта',
    'April': 'апреля',
    'May': 'мая',
    'June': 'июня',
    'July': 'июля',
    'August': 'августа',
    'September': 'сентября',
    'October': 'октября',
    'November': 'ноября',
    'December': 'декабря'
}

def print_current_date():
    now = datetime.now()
    month = now.strftime("%B")
    month_ru = months_dict.get(month)
    year = now.strftime("%Y")
    day = now.strftime("%d")
    return f"{day} {month_ru} {year} года"

def print_current_time():
    now = datetime.now()
    hours = now.strftime("%H")
    minutes = now.strftime("%M")
    return f"{hours} часов, {minutes} минут"

