import logging
import telebot
from functions.function_hello_get import *
from functions.valuti import *
from sq_connets.sqlte_connect_files import *
import datetime


logging.basicConfig(level=logging.INFO)

bot = telebot.TeleBot('6040960208:AAEwPLomCRMCqtCAtQzKfl1tSh8jq7nYV1Y')


@bot.message_handler(commands=['start'])
def register_user(message):
    cursor.execute('SELECT * FROM users WHERE tg_id=?', (message.from_user.id,))
    user = cursor.fetchone()
    user_id_name = message.from_user

    if user is None:
        bot.send_message(message.chat.id, f'{return_time()}, {user_id_name.first_name}! Давайте пройдем регистрацию.\n'
                                          f'Введи пожалуйста свой бюджет на месяц: ')

        bot.register_next_step_handler(message, process_budget_step)

    else:
        bot.send_message(message.chat.id, 'Вы уже зарегистрированы!')


def process_budget_step(message):
    try:
        budget = int(message.text)

        registration_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''  
            INSERT INTO users (tg_id, budget, expense,
             last_purchase, registration_date, last_update_date, is_registered)
            VALUES (?, ?, 0, "отсутствует", ?, ?, 1)
        ''', (message.from_user.id, budget, registration_date, registration_date))
        conn.commit()

        bot.send_message(message.chat.id, 'Регистрация успешно завершена!')
        user_file_name = str(message.from_user.id) + '.txt'
        with open(f'C:/Users/Пользователь/PycharmProjects/aaaaa/users/{str(user_file_name)}', 'w') as user_file:
            user_file.write('')
        user_file.close()
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат бюджета. Пожалуйста, введите числовое значение.')


@bot.message_handler(commands=['info'])
def start(message):
    user = message.from_user

    photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor/c5fcbc4b-28ba-4d9b-a434-e25353c42cb3.jfif'
    photo_caption = f"{return_time()}, {user.first_name}!\n\n" \
                    f"Профиль пользователя:\n\n" \
                    f"information: None\n" \
                    f"Name: {user.first_name}\n" \
                    f"Your tg id: {user.id}\n\n" \
                    f"in development\n\n" \
                    f"Для ознакомления со своими финансами и расходами, введите команду /rashod"
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=photo_caption)


@bot.message_handler(commands=['kurs'])
def kurs(message):
    photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor/e41bb881-a9a2-467a-87c8-92e870f618ee.jfif'
    text = f'Курсы ведущих валют\n' \
           f'Обновлено {print_current_date()} {print_current_time()}\n\n' \
           f'💰 USD - {function_return_valutes()[0].value} ₽\n' \
           f'💰 EUR - {function_return_valutes()[1].value} ₽\n' \
           f'💰 GBP - {function_return_valutes()[2].value} ₽\n' \
           f'💰 KZT - {function_return_valutes()[3].value} ₽\n' \
           f'💰 GEL - {function_return_valutes()[4].value} ₽ \n' \
           f'💰 TRY - {function_return_valutes()[5].value} ₽ \n' \
           f'💰 CNY - {function_return_valutes()[6].value} ₽\n' \
           f'💰 JPY - {function_return_valutes()[7].value} ₽\n'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text)


@bot.message_handler(commands=['schet'])
def schet(message):
    user = message.from_user

    photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor/349ce560-36a7-4f19-8550-e16c1889d4e7.jfif'
    text = f'{user.first_name}, Интеграция банковских счетов временно не работает. Попробуйте немного позже.'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text)


@bot.message_handler(commands=['help'])
def __help(message):
    photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor/vI3cGKkkClY.jpg'
    text = f'✔️Помощь и инструкция по боту:✔️ \n\n' \
           f'‼️Для просмотра той или иной функции Вам следует просто нажать на команду рядом с ее названием.\n\n' \
           f'🔸Функционал:🔸\n\n' \
           f'⭐ Советы и финансовые термины - команда в разработке.\n' \
           f'⭐ Профиль пользователя: /info\n' \
           f'⭐ Финансовые расходы и доходы - /rashod\n' \
           f'⭐ Установка финансовых целей и задач на текущий месяц - команда в разработке\n' \
           f'⭐ Интеграция банковских сбережений и электронных кошельков -  /schet\n' \
           f'⭐ Вывод текущего курса популярных валют - /kurs\n' \
           f'⭐ Редактирование своих расходов и доходов - /refactor\n' \
           f'⭐ Настройка своего профиля и уведомлений - /settings\n\n' \
           f'🔸Инструкция по боту:🔸\n\n' \
           f'Бот написан для полного контроля и слежкой за своими финансами.\n'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text)


@bot.message_handler(commands=['rashod'])
def rashod(message):
    user = message.from_user
    cursor.execute('SELECT * FROM users WHERE tg_id=?', (user.id,))
    row = cursor.fetchone()

    if row is not None:
        budget = row[2]
        current_expense = row[3]
        last_purchase = row[4]
        last_update_date = row[6]

        photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor/e41bb881-a9a2-467a-87c8-92e870f618ee.jfif'
        with open(photo_path, 'rb') as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption=f'{return_time()}, {user.first_name}\n\n'
                        f'Твои текущие финансовые расходы: \n\n'
                        f'⚙️ {user.first_name}, твои расходы за этот месяц....:⚙️ \n'
                        f'💻 ID: {user.id}\n'
                        f'💸 Бюджет на этот месяц   : {budget}\n'
                        f'💰 Текущий расход в этом месяце: {current_expense}\n'
                        f'⌚️ Дата последнего обновления бюджета: {last_update_date}\n'
                        f'🏷 Последняя покупка: {last_purchase}'
            )
    else:
        bot.reply_to(message, 'Вы еще не зарегистрированы! Введите команду /start для регистрации.')


@bot.message_handler(commands=['add_b'])
def add_budget(message):
    user = message.from_user
    command_args = message.text.split()

    if len(command_args) < 2:
        bot.reply_to(message, 'Некорректный формат команды. Введите сумму для добавления к бюджету.')
        return

    try:
        amount = int(command_args[1])
    except ValueError:
        bot.reply_to(message, 'Некорректный формат суммы. Пожалуйста, введите целое число.')
        return

    cursor.execute('SELECT * FROM users WHERE tg_id=?', (user.id,))
    row = cursor.fetchone()

    if row is not None:
        budget = row[2]

        updated_budget = budget + amount

        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('UPDATE users SET budget=?, last_update_date=? WHERE tg_id=?',
                       (updated_budget, current_time, user.id))
        conn.commit()

        bot.reply_to(message, f'Бюджет успешно обновлен. Текущий бюджет: {updated_budget}')
    else:
        bot.reply_to(message, 'Вы еще не зарегистрированы! Введите команду /start для регистрации.')


@bot.message_handler(commands=['add_r'])
def add_expense(message):
    user = message.from_user
    command_args = message.text.split()

    if len(command_args) < 3:
        bot.reply_to(message, 'Некорректный формат команды. Введите сумму и описание покупки.')
        return

    try:
        amount = int(command_args[1])
    except ValueError:
        bot.reply_to(message, 'Некорректный формат суммы. Пожалуйста, введите целое число.')
        return

    description = ' '.join(command_args[2:])
    with open(f'C:/Users/Пользователь/PycharmProjects/aaaaa/users/{str(user.id) + ".txt"}', 'w') as user_file:

        user_file.write(f'{description} - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    user_file.close()

    cursor.execute('SELECT * FROM users WHERE tg_id=?', (user.id,))
    row = cursor.fetchone()

    if row is not None:
        current_expense = row[3]
        budget = row[2]
        update_budget = budget - amount
        updated_expense = current_expense + amount



        cursor.execute('UPDATE users SET expense=?, budget=?, last_purchase=? WHERE tg_id=?',
                       (updated_expense, update_budget, description, user.id))
        conn.commit()

        bot.reply_to(message, f'Расход успешно добавлен. Текущий расход: {updated_expense}')
    else:
        bot.reply_to(message, 'Вы еще не зарегистрированы! Введите команду /start для регистрации.')


@bot.message_handler(commands=['history'])
def add_expense(message):
    user = message.from_user
    with open(f'C:/Users/Пользователь/PycharmProjects/aaaaa/users/{str(user.id) + ".txt"}', 'r') as user_file:
        user_file.readlines()
    print(user_file.readlines())
    user_file.close()


bot.polling()
