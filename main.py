import logging
import telebot
from functions.function_hello_get import *
from functions.valuti import *
from sq_connets.sqlte_connect_files import *
from telebot import types
from functions.daily_citata import *
from functions.function_return_videos import *
from functions.function_return_books_andllll import *
from functions.slovar_finder import *
from functions.return_risk_and_sovet import *
from tests_and_info.soveti_please import *

logging.basicConfig(level=logging.INFO)

bot = telebot.TeleBot('TOKEN_TG')


@bot.message_handler(commands=['start'])
def register_user(message):
    cursor.execute('SELECT * FROM users WHERE tg_id=?', (message.from_user.id,))
    user = cursor.fetchone()
    user_id_name = message.from_user

    if user is None:
        bot.send_message(message.from_user.id,
                         f'{return_time()}, {user_id_name.first_name}!👋 Давайте пройдем регистрацию.\n'
                         f'📝 Введи пожалуйста свой бюджет на месяц: ')
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-'])
        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2
        example_message = f'Решите пример:\n\n{num1} {operator} {num2} = ?'
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text=str(result), callback_data='registration_success'))
        keyboard.add(types.InlineKeyboardButton(text='Ответ неверный', callback_data='registration_failed'))

        bot.send_message(message.from_user.id, example_message, reply_markup=keyboard)

    else:
        bot.send_message(message.from_user.id, '❌ Вы уже зарегистрированы!')


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == 'registration_success':
        bot.send_message(call.from_user.id, text='✅ Вы подтвердили, что вы не бот!')
        bot.send_message(call.from_user.id,
                         f'{return_time()}, {call.from_user.first_name}! Давайте пройдем регистрацию.\n'
                         f'Введи пожалуйста свой бюджет на месяц: ')

        bot.register_next_step_handler(call.message, process_budget_step)

    elif call.data == 'registration_failed':

        bot.answer_callback_query(call.from_user.id, text='❌ Регистрация отклонена. Попробуйте позже.')
    if call.data == 'add_budget':
        bot.send_message(call.from_user.id, 'Введите сумму для добавления бюджета:')
        bot.register_next_step_handler(call.message, add_budget)
    elif call.data == 'add_expense':

        keyboard_catigories = types.InlineKeyboardMarkup()
        keyboard_catigories.add(types.InlineKeyboardButton(text='Транспорт', callback_data='cars'))
        keyboard_catigories.add(types.InlineKeyboardButton(text='Еда', callback_data='food'))
        keyboard_catigories.add(types.InlineKeyboardButton(text='Одежда', callback_data='cloth'))
        keyboard_catigories.add(types.InlineKeyboardButton(text='Кафе, рестораны', callback_data='cofe'))
        keyboard_catigories.add(types.InlineKeyboardButton(text='Образование', callback_data='ucheba'))
        keyboard_catigories.add(types.InlineKeyboardButton(text='Другое', callback_data='other'))

        bot.send_message(call.from_user.id, 'Выберите категорию для добавления расходов:',
                         reply_markup=keyboard_catigories)

    if call.data == 'cars':
        bot.send_message(call.from_user.id, 'Введите сумму для добавления расхода: ')
        bot.register_next_step_handler(call.message, function_add_rashodi_cars)
    if call.data == 'food':
        bot.send_message(call.from_user.id, 'Введите сумму для добавления расхода:')
        bot.register_next_step_handler(call.message, function_add_rashodi_food)
    if call.data == 'cloth':
        bot.send_message(call.from_user.id, 'Введите сумму для добавления расхода:')
        bot.register_next_step_handler(call.message, function_add_rashodi_cloth)
    if call.data == 'cofe':
        bot.send_message(call.from_user.id, 'Введите сумму для добавления расхода:')
        bot.register_next_step_handler(call.message, function_add_rashodi_cofe)
    if call.data == 'ucheba':
        bot.send_message(call.from_user.id, 'Введите сумму для добавления расхода:')
        bot.register_next_step_handler(call.message, function_add_rashodi_ucheba)
    if call.data == 'other':
        bot.send_message(call.from_user.id, 'Введите сумму для добавления расхода:')
        bot.register_next_step_handler(call.message, function_add_rashodi_other)


def process_budget_step(message):
    try:
        budget = int(message.text)

        registration_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''  
            INSERT INTO users (tg_id, budget, expense,
             last_purchase, registration_date, last_update_date, is_registered)
            VALUES (?, ?, 0, "отсутствует", ?, ?, 1)
        ''', (message.from_user.id, budget, registration_date, registration_date))
        conn.commit()

        bot.send_message(message.chat.id, '✅ Регистрация успешно завершена!🎉')
        user_file_name = str(message.from_user.id) + '.txt'
        with open(f'C:/Users/Пользователь/PycharmProjects/aaaaa/users/{str(user_file_name)}', 'w') as user_file:
            user_file.write('')
        user_file.close()
    except ValueError:
        bot.send_message(message.chat.id, '❌ Неверный формат бюджета. Пожалуйста, введите числовое значение.')


@bot.message_handler(commands=['info'])
def start(message):
    user = message.from_user

    photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor/c5fcbc4b-28ba-4d9b-a434-e25353c42cb3.jfif'
    photo_caption = f"{return_time()}, {user.first_name}!👋\n\n" \
                    f"👤 Профиль пользователя:\n\n" \
                    f"ℹ️ Важная информация за день:\n\n" \
                    f"💵 = {function_return_valutes()[0].value}\n" \
                    f"💶 = {function_return_valutes()[1].value}\n\n" \
                    f"🕰 Новости за сегодня: {print_current_date()} {print_current_time()}\n\n" \
                    f"🧑‍💼 Имя: {user.first_name}\n" \
                    f"🆔 Ваш персональный ID: {user.id}\n\n" \
                    f"💡 Для ознакомления со своими финансами и расходами, введите команду /rashod"
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=photo_caption)


@bot.message_handler(commands=['kurs'])
def kurs(message):
    photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor/e41bb881-a9a2-467a-87c8-92e870f618ee.jfif'
    text = f'📈 Курсы ведущих валют\n' \
           f'🔄 Обновлено {print_current_date()} {print_current_time()}\n\n' \
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
    text = f'{user.first_name}, Интеграция банковских счетов временно не работает. Попробуйте немного позже.⚠️'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text)


@bot.message_handler(commands=['help'])
def __help(message):
    photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor/vI3cGKkkClY.jpg'
    text = f'✔️ Помощь и инструкция по боту:✔️ \n\n' \
           f'‼️ Для просмотра той или иной функции Вам следует просто нажать на команду рядом с ее названием.\n\n' \
           f'🔸 Функционал:🔸\n\n' \
           f'⭐ Советы и финансовые термины - /sovet.\n\n    ' \
           f'⭐ Профиль пользователя: /info\n\n' \
           f'⭐ История последних 10 покупок: /history\n\n' \
           f'⭐ Финансовые расходы и доходы - /rashod\n\n' \
           f'⭐ Установка финансовых целей и задач на текущий месяц - команда в разработке\n\n' \
           f'⭐ Интеграция банковских сбережений и электронных кошельков - /schet\n\n' \
           f'⭐ Вывод текущего курса популярных валют - /kurs\n\n' \
           f'⭐ Редактирование своих расходов и доходов - /refactor\n\n' \
           f'⭐ Просмотр образовательных видеороликов - /video\n\n' \
           f'⭐ Получение мотивационной цитаты - /citat\n\n' \
           f'⭐ Рекомендация книг - /books\n\n' \
           f'⭐ История твоих транзакций - /history\n\n' \
           f'⭐ Поиск информации - /search\n\n' \
           f'⭐ Риски в "Финансовой жизни" - /risk\n\n' \
           f'🔸 Инструкция по боту:🔸\n\n' \
           f'Бот написан для полного контроля и слежкой за своими финансами.✅\n'
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
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Добавление суммы к бюджету', callback_data='add_budget'))
        keyboard.add(types.InlineKeyboardButton(text='Добавление суммы к расходу', callback_data='add_expense'))
        with open(photo_path, 'rb') as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption=f'{return_time()}, {user.first_name}\n\n'
                        f'📊 Твои текущие финансовые расходы: \n\n'
                        f'⚙️ {user.first_name}, твоя финансовая статистика за месяц:⚙️ \n'
                        f'💻 ID: {user.id}\n'
                        f'💸 Бюджет на этот месяц: {budget}\n'
                        f'💰 Текущий расход в этом месяце: {current_expense}\n'
                        f'⌚️ Дата последнего обновления бюджета: {last_update_date}\n'
                        f'🏷 Последняя покупка: {last_purchase}', reply_markup=keyboard)

    else:
        bot.reply_to(message, '❌ Вы еще не зарегистрированы! Введите команду /start для регистрации.')


def function_add_rashodi_cars(message):
    user = message.from_user.id
    messages = message.text
    print(user)
    categories = 'cars'
    with open(f'C:/Users/Пользователь/PycharmProjects/aaaaa/users/{str(user) + ".txt"}', 'a') as user_file:

        user_file.write(f'{categories} - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
    user_file.close()

    cursor.execute('SELECT * FROM users WHERE tg_id=?', (user,))
    row = cursor.fetchone()

    if row is not None:
        current_expense = row[3]
        budget = row[2]
        update_budget = budget - int(messages)
        updated_expense = current_expense + int(messages)
        try:

            cursor.execute('UPDATE users SET expense=?, budget=?, last_purchase=? WHERE tg_id=?',
                           (updated_expense, update_budget, categories, user))
            conn.commit()

            bot.send_message(user, f'✅ Расход успешно добавлен. Текущий расход: {updated_expense} 💸')
            cursor.execute('SELECT * FROM rashodi WHERE tg_id=?', (user,))
            rows = cursor.fetchone()
            if rows is not None:
                cars = rows[2]
                updated_expense = cars + int(messages)

                cursor.execute('UPDATE rashodi SET cars=? WHERE tg_id=?',
                               (updated_expense, user))
                conn.commit()
        except OverflowError:
            bot.send_message(user, 'Вы ввели слишком большое число. Попробуйте повторить позже.')

    else:
        bot.send_message(user,
                         '❌ Вы еще не зарегистрированы! Введите команду /start для регистрации.')


def function_add_rashodi_food(message):
    user = message.from_user.id
    messages = message.text
    categories = 'food'
    with open(f'C:/Users/Пользователь/PycharmProjects/aaaaa/users/{str(user) + ".txt"}', 'a') as user_file:

        user_file.write(f'{categories} - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
    user_file.close()

    cursor.execute('SELECT * FROM users WHERE tg_id=?', (user,))
    row = cursor.fetchone()

    if row is not None:
        current_expense = row[3]
        budget = row[2]
        update_budget = budget - int(messages)
        updated_expense = current_expense + int(messages)

        cursor.execute('UPDATE users SET expense=?, budget=?, last_purchase=? WHERE tg_id=?',
                       (updated_expense, update_budget, categories, user))
        conn.commit()

        bot.send_message(user, f'✅ Расход успешно добавлен. Текущий расход: {updated_expense} 💸')
        cursor.execute('SELECT * FROM rashodi WHERE tg_id=?', (user,))
        rows = cursor.fetchone()
        if rows is not None:
            food = rows[2]
            updated_expense = food + int(messages)

            cursor.execute('UPDATE rashodi SET food=? WHERE tg_id=?',
                           (updated_expense, user))
            conn.commit()

    else:
        bot.send_message(user,
                         '❌ Вы еще не зарегистрированы! Введите команду /start для регистрации.')


def function_add_rashodi_cloth(message):
    user = message.from_user.id
    messages = message.text
    categories = 'cloth'
    with open(f'C:/Users/Пользователь/PycharmProjects/aaaaa/users/{str(user) + ".txt"}', 'a') as user_file:

        user_file.write(f'{categories} - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
    user_file.close()

    cursor.execute('SELECT * FROM users WHERE tg_id=?', (user,))
    row = cursor.fetchone()

    if row is not None:
        current_expense = row[3]
        budget = row[2]
        update_budget = budget - int(messages)
        updated_expense = current_expense + int(messages)

        cursor.execute('UPDATE users SET expense=?, budget=?, last_purchase=? WHERE tg_id=?',
                       (updated_expense, update_budget, categories, user))
        conn.commit()

        bot.send_message(user, f'✅ Расход успешно добавлен. Текущий расход: {updated_expense} 💸')
        cursor.execute('SELECT * FROM rashodi WHERE tg_id=?', (user,))
        rows = cursor.fetchone()
        if rows is not None:
            cloth = rows[2]
            updated_expense = cloth + int(messages)

            cursor.execute('UPDATE rashodi SET cloth=? WHERE tg_id=?',
                           (updated_expense, user))
            conn.commit()

    else:
        bot.send_message(user,
                         '❌ Вы еще не зарегистрированы! Введите команду /start для регистрации.')


def function_add_rashodi_cofe(message):
    user = message.from_user.id
    messages = message.text
    categories = 'cofe'
    with open(f'C:/Users/Пользователь/PycharmProjects/aaaaa/users/{str(user) + ".txt"}', 'a') as user_file:

        user_file.write(f'{categories} - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
    user_file.close()

    cursor.execute('SELECT * FROM users WHERE tg_id=?', (user,))
    row = cursor.fetchone()

    if row is not None:
        current_expense = row[3]
        budget = row[2]
        update_budget = budget - int(messages)
        updated_expense = current_expense + int(messages)

        cursor.execute('UPDATE users SET expense=?, budget=?, last_purchase=? WHERE tg_id=?',
                       (updated_expense, update_budget, categories, user))
        conn.commit()

        bot.send_message(user, f'✅ Расход успешно добавлен. Текущий расход: {updated_expense} 💸')
        cursor.execute('SELECT * FROM rashodi WHERE tg_id=?', (user,))
        rows = cursor.fetchone()
        if rows is not None:
            cofe = rows[2]
            updated_expense = cofe + int(messages)

            cursor.execute('UPDATE rashodi SET cofe=? WHERE tg_id=?',
                           (updated_expense, user))
            conn.commit()

    else:
        bot.send_message(user,
                         '❌ Вы еще не зарегистрированы! Введите команду /start для регистрации.')


def function_add_rashodi_ucheba(message):
    user = message.from_user.id
    messages = message.text
    categories = 'ucheba'
    with open(f'C:/Users/Пользователь/PycharmProjects/aaaaa/users/{str(user) + ".txt"}', 'a') as user_file:

        user_file.write(f'{categories} - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
    user_file.close()

    cursor.execute('SELECT * FROM users WHERE tg_id=?', (user,))
    row = cursor.fetchone()

    if row is not None:
        current_expense = row[3]
        budget = row[2]
        update_budget = budget - int(messages)
        updated_expense = current_expense + int(messages)

        cursor.execute('UPDATE users SET expense=?, budget=?, last_purchase=? WHERE tg_id=?',
                       (updated_expense, update_budget, categories, user))
        conn.commit()

        bot.send_message(user, f'✅ Расход успешно добавлен. Текущий расход: {updated_expense} 💸')
        cursor.execute('SELECT * FROM rashodi WHERE tg_id=?', (user,))
        rows = cursor.fetchone()
        if rows is not None:
            ucheba = rows[2]
            updated_expense = ucheba + int(messages)

            cursor.execute('UPDATE rashodi SET ucheba=? WHERE tg_id=?',
                           (updated_expense, user))
            conn.commit()

    else:
        bot.send_message(user,
                         '❌ Вы еще не зарегистрированы! Введите команду /start для регистрации.')


def function_add_rashodi_other(message):
    user = message.from_user.id
    messages = message.text
    categories = 'other'
    with open(f'C:/Users/Пользователь/PycharmProjects/aaaaa/users/{str(user) + ".txt"}', 'a') as user_file:

        user_file.write(f'{categories} - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
    user_file.close()

    cursor.execute('SELECT * FROM users WHERE tg_id=?', (user,))
    row = cursor.fetchone()

    if row is not None:
        current_expense = row[3]
        budget = row[2]
        update_budget = budget - int(messages)
        updated_expense = current_expense + int(messages)

        cursor.execute('UPDATE users SET expense=?, budget=?, last_purchase=? WHERE tg_id=?',
                       (updated_expense, update_budget, categories, user))
        conn.commit()

        bot.send_message(user, f'✅ Расход успешно добавлен. Текущий расход: {updated_expense} 💸')
        cursor.execute('SELECT * FROM rashodi WHERE tg_id=?', (user,))
        rows = cursor.fetchone()
        if rows is not None:
            other = rows[2]
            updated_expense = other + int(messages)

            cursor.execute('UPDATE rashodi SET other=? WHERE tg_id=?',
                           (updated_expense, user))
            conn.commit()

    else:
        bot.send_message(user,
                         '❌ Вы еще не зарегистрированы! Введите команду /start для регистрации.')


@bot.message_handler(commands=['risk'])
def return_sovet(message):
    user = message.from_user
    bot.send_message(user.id,
                     'Ознакомься с рисками,которые могут встретиться тебе на твоем жизненном пути')
    bot.send_message(user.id, function_rabotay_please_ya_zadolbalsya()[0])
    bot.send_message(user.id, function_rabotay_please_ya_zadolbalsya()[1])
    bot.send_message(user.id, function_rabotay_please_ya_zadolbalsya()[2])


@bot.message_handler(commands=['sovet'])
def return_sovet(message):
    user = message.from_user
    bot.send_message(user.id, f'Ваш персональный совет: {function_sovet_last()}')


@bot.message_handler(commands=['search'])
def search_osn(message):
    user = message.from_user
    command_args = message.text.split()

    if len(command_args) < 2:
        bot.reply_to(message, '❌ Некорректный формат команды. Необходим критерий!')
        return
    else:
        if slovar_find(slovar=slovar_unsorted, a=command_args[1]):
            bot.send_message(user.id,
                             f'{command_args[1]} - {slovar_find(slovar=slovar_unsorted, a=command_args[1])}')

        else:
            bot.send_message(user.id, 'Ваш термин не найден или не относится к теме "Финансовая грамотность"\n'
                                      'Проверьте вводимые данные.')


def add_budget(message):
    user = message.from_user.id
    command_args = message.text

    try:
        amount = int(command_args)
    except ValueError:
        bot.send_message(int(user), '❌ Некорректный формат суммы. Пожалуйста, введите целое число.')
        return

    cursor.execute('SELECT * FROM users WHERE tg_id=?', (int(user),))
    row = cursor.fetchone()

    if row is not None:
        budget = row[2]

        updated_budget = budget + amount

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            cursor.execute('UPDATE users SET budget=?, last_update_date=? WHERE tg_id=?',
                           (updated_budget, current_time, int(user)))
            conn.commit()

            bot.send_message(int(user), f'✅ Бюджет успешно обновлен. Текущий бюджет: {updated_budget} 💰')
        except OverflowError:
            bot.send_message(int(user), 'Вы ввели слишком большое число. Попробуйте заново.')
    else:
        bot.send_message(int(user), '❌ Вы еще не зарегистрированы! Введите команду /start для регистрации.')


@bot.message_handler(commands=['citat'])
def citat_gets(message):
    user = message.from_user
    bot.send_message(user.id, f'Цитата дня: \n\n {daily_citat}')


@bot.message_handler(commands=['video'])
def videos_get(message):
    user = message.from_user
    bot.send_message(user.id, function_return_and_get_video())


@bot.message_handler(commands=['books'])
def books_get(message):
    user = message.from_user
    bot.send_message(user.id, function_books())


@bot.message_handler(commands=['history'])
def history(message):
    user = message.from_user
    with open(f'C:/Users/Пользователь/PycharmProjects/aaaaa/users/{str(user.id) + ".txt"}', 'r') as user_file:
        k = user_file.readlines()
        m = ''
        for i in k:
            m += f'⚡ {i}'
        bot.send_message(message.from_user.id, text=f'📊 Ваши последние 10 расходов: \n\n {m}')


bot.polling()
