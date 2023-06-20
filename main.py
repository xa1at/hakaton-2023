import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from for_test_file import settings
from functions.function_get_kurs import *
from functions.function_get_datetime import *
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6040960208:AAEwPLomCRMCqtCAtQzKfl1tSh8jq7nYV1Y')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

menu = [
    [InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text"),
     InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image")],
    [InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
     InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
     InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])


@dp.message_handler(commands=['start', 'info'])
async def start(message: types.Message):
    user = message.from_user
    await message.reply(f"Привет, {user.first_name}! Бот разработан на Яп Python. \n Функционал бота в разработке.")

    photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor/publichnoe-foto-v-telegram-1.jpg'
    photo_caption = f"Профиль пользователя:\n\n" \
                    f"information: None\n" \
                    f"Name: {user.first_name}\n" \
                    f"Your tg id: {user.id}\n\n" \
                    f"in developmend\n\n" \
                    f"Для ознакомления со своими финансами и расходами, введите команду /rashod"
    with open(photo_path, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption=photo_caption)


@dp.message_handler(commands=['rashod'])
async def rashod(message: types.Message):
    user = message.from_user
    await message.reply('Функуция в разработке!')

    photo_path = '/musor/images.jfif'
    with open(photo_path, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption=f'Твои текущие финансовые расходы: \n\n'
                                                             f'{user.first_name}, твой профиль....:\n'
                                                             f'{user.id} - твой ID\n'
                                                             f'Бюджет: {settings["бюджет"]}\n'
                                                             f'Текущий расход в этом месеце: {settings["текущий расход"]}\n'
                                                             f'Дата последнего обновления бюджета: {settings["дата получение дохода"]}\n'
                                                             f'Последняя покупка: {settings["последний расход"]}')


@dp.message_handler(commands=['kurs'])
async def kurs(message: types.Message):
    user = message.from_user

    photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor\images.jfif'
    text = f'Текущий курс на {print_current_date()} {print_current_time()}:\n' \
           f'💵 {print_currency_info(1)}'
    with open(photo_path, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption=text)


@dp.message_handler(commands=['schet'])
async def schet(message: types.Message):
    user = message.from_user

    photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor\images.jfif'
    text = ''
    with open(photo_path, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption=text)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    user = message.from_user

    photo_path = 'C:/Users/Пользователь/PycharmProjects/aaaaa/musor\images.jfif'
    text = f'✔️Помощь и инструкция по боту:✔️ \n\n' \
           f'‼️Для просмотра той или иной функции Вам следует просто нажать на команду рядом с ее названием.\n\n' \
           f'🔸Функционал:🔸\n\n' \
           f'⭐ Советы и финансовые термины - команда в разработке.\n' \
           f'⭐ Финансовые расходы и доходы - /rashod\n' \
           f'⭐ Установка финансовых целей и задач на текущий месяц - команда в разработке\n' \
           f'⭐ Интеграция банковских сбережений и электронных кошельков -  /schet\n' \
           f'⭐ Вывод текущего курса популярных валют - /kurs\n' \
           f'⭐ Редактирование своих расходов и доходов - /refactor\n' \
           f'⭐ Настройка своего профиля и уведомлений - /settings\n\n' \
           f'🔸Инструкция по боту:🔸\n\n' \
           f'Бот написан для полного контроля и слежкой за своими финансами.\n'
    with open(photo_path, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption=text)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
