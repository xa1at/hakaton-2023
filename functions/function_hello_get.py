import random
import time

random_priv_utro = ['Доброе утро', 'Доброго утречка', 'Утро доброе', 'Привет', 'Приветствую', 'Здравствуй']
random_priv_den = ['Добрый день', 'День добрый', 'Привет', 'Приветствую', 'Здравствуй']
random_priv_vecher = ['Добрый вечер', 'Вечер добрый', 'Привет', 'Приветствую', 'Здравствуй']
random_priv_other = ['Доброй ночи', 'Привет', 'Приветствую', 'Здравствуй', 'Здравствуйте']


def return_time():
    time_seychas = time.strftime('%H')
    if 5 <= int(time_seychas) <= 11:
        return random.choice(random_priv_utro)
    elif 11 < int(time_seychas) <= 16:
        return random.choice(random_priv_den)
    elif 16 < int(time_seychas) <= 21:
        return random.choice(random_priv_vecher)
    else:
        return random.choice(random_priv_other)
