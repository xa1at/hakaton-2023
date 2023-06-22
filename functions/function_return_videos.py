from tests_and_info.slovar_i_books_v2 import *


def function_return_and_get_video():
    vid = ''
    for i in videos:
        vid += f'📹 {i}\n'
    texts_and_kkk = f'Для улучшения своей финансовой грамотности, советуем к просмотру эти видео:\n\n {vid}'
    return texts_and_kkk
