from tests_and_info.slovar_i_books_v2 import *


def function_books():
    book = ''
    for i in books:
        book += f'📖 {i}\n'
    texts_and_kkk = f'Для улучшения своей финансовой грамотности, советуем к прочтению эти книги.\n' \
                    f'Они помогут Вам разобраться и улучшить свою финансовую грамотность.\n\n {book}'
    return texts_and_kkk
