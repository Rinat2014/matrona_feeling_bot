from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
# from settings import url_bot_forma


iKM_start_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Google', callback_data=f'url', url="https://google.com")],
])


iKB_admin = InlineKeyboardMarkup(inline_keyboard=[
    [
     InlineKeyboardButton(text=f'Ответы в чат', callback_data=f'fs_answers_to_admin'),
    ],
    [InlineKeyboardButton(text=f'Ответы в XLS', callback_data=f'fs_answers_to_admin_xls')],
    [InlineKeyboardButton(text=f'Добавить админа', callback_data=f'add_admin')],
    [InlineKeyboardButton(text=f'Удалить админа', callback_data=f'show_admin_list_to_del')],
    [InlineKeyboardButton(text=f'Показать список админов', callback_data=f'show_admins')],
])


KB_start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Почасовка чувств"),
        ],
    ],
    resize_keyboard=True,
    # input_field_placeholder='Что Вас интересует?'
)



KB_FS_da_otmena_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Отмена"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Резюмируем опрос'
)


KB_del = ReplyKeyboardRemove()


# возвращаем клавиатуру, которая позволяет делать запросы на удаление админов
def kbDelAdmin(name, user_id):
    kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f'Delete {name}', callback_data=f'drop_admin,{user_id}')],
        ])
    return kb



# возвращаем клавиатуру чувств
# def ikbFeels(feel_names):
#     # inline_keyboard=[]
#     ikb = InlineKeyboardMarkup(inline_keyboard=[])
#     for feel in feel_names:
#         ikb = ikb.add(InlineKeyboardButton(text=f"{feel}", callback_data=f"feel,{feel}"))
    
#     # ikb = InlineKeyboardMarkup(inline_keyboard)
#     return ikb

iKB_Feels_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Гнев', callback_data=f'feel,Гнев') ],
    [InlineKeyboardButton(text=f'Обида', callback_data=f'feel,Обида') ],
    [InlineKeyboardButton(text=f'Возмущение', callback_data=f'feel,Возмущение') ],
    [InlineKeyboardButton(text=f'Раздражение', callback_data=f'feel,Раздражение') ],
    [InlineKeyboardButton(text=f'Злость', callback_data=f'feel,Злость') ],
    [InlineKeyboardButton(text=f'Негодование', callback_data=f'feel,Негодование') ],
    [InlineKeyboardButton(text=f'Недовольство', callback_data=f'feel,Недовольство') ],
    [InlineKeyboardButton(text=f'Презрение', callback_data=f'feel,Презрение') ],
    [InlineKeyboardButton(text=f'Бешенство', callback_data=f'feel,Бешенство') ],
    [InlineKeyboardButton(text=f'Ненависть', callback_data=f'feel,Ненависть') ],
    
    [
    InlineKeyboardButton(text=f'[1]', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])

iKB_Feels_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Ярость', callback_data=f'feel,Ярость') ],
    [InlineKeyboardButton(text=f'Отвращение', callback_data=f'feel,Отвращение') ],
    [InlineKeyboardButton(text=f'Неприязнь', callback_data=f'feel,Неприязнь') ],
    [InlineKeyboardButton(text=f'Истерия', callback_data=f'feel,Истерия') ],
    [InlineKeyboardButton(text=f'Ревность', callback_data=f'feel,Ревность') ],
    [InlineKeyboardButton(text=f'Зависть', callback_data=f'feel,Зависть') ],
    [InlineKeyboardButton(text=f'Досада', callback_data=f'feel,Досада') ],
    [InlineKeyboardButton(text=f'Напряжение', callback_data=f'feel,Напряжение') ],
    [InlineKeyboardButton(text=f'Страдание', callback_data=f'feel,Страдание') ],
    [InlineKeyboardButton(text=f'Протест', callback_data=f'feel,Протест') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'[2]', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])

iKB_Feels_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Принуждение', callback_data=f'feel,Принуждение') ],
    [InlineKeyboardButton(text=f'Пренебрежение', callback_data=f'feel,Пренебрежение') ],
    [InlineKeyboardButton(text=f'Нетерпение', callback_data=f'feel,Нетерпение') ],
    [InlineKeyboardButton(text=f'Враждебность', callback_data=f'feel,Враждебность') ],
    [InlineKeyboardButton(text=f'Вседозволенность', callback_data=f'feel,Вседозволенность') ],
    [InlineKeyboardButton(text=f'Вредность', callback_data=f'feel,Вредность') ],
    [InlineKeyboardButton(text=f'Высокомерие', callback_data=f'feel,Высокомерие') ],
    [InlineKeyboardButton(text=f'Превосходство', callback_data=f'feel,Превосходство') ],
    [InlineKeyboardButton(text=f'Отвержение', callback_data=f'feel,Отвержение') ],
    [InlineKeyboardButton(text=f'Уязвленность', callback_data=f'feel,Уязвленность') ],

    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'[3]', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])
    
iKB_Feels_4 = InlineKeyboardMarkup(inline_keyboard=[   
    [InlineKeyboardButton(text=f'Страх', callback_data=f'feel,Страх') ],
    [InlineKeyboardButton(text=f'Испуг', callback_data=f'feel,Испуг') ],
    [InlineKeyboardButton(text=f'Оцепенение', callback_data=f'feel,Оцепенение') ],
    [InlineKeyboardButton(text=f'Боязнь', callback_data=f'feel,Боязнь') ],
    [InlineKeyboardButton(text=f'Ужас', callback_data=f'feel,Ужас') ],
    [InlineKeyboardButton(text=f'Отчаянне', callback_data=f'feel,Отчаянне') ],
    [InlineKeyboardButton(text=f'Тревога', callback_data=f'feel,Тревога') ],
    [InlineKeyboardButton(text=f'Ошарашенность', callback_data=f'feel,Ошарашенность') ],
    [InlineKeyboardButton(text=f'Замешательство', callback_data=f'feel,Замешательство') ],
    [InlineKeyboardButton(text=f'Растерянность', callback_data=f'feel,Растерянность') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'[4]', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])

iKB_Feels_5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Вина', callback_data=f'feel,Вина') ],
    [InlineKeyboardButton(text=f'Стыд', callback_data=f'feel,Стыд') ],
    [InlineKeyboardButton(text=f'Беспокойство', callback_data=f'feel,Беспокойство') ],
    [InlineKeyboardButton(text=f'Сомнения', callback_data=f'feel,Сомнения') ],
    [InlineKeyboardButton(text=f'Застенчивость', callback_data=f'feel,Застенчивость') ],
    [InlineKeyboardButton(text=f'Подозрение', callback_data=f'feel,Подозрение') ],
    [InlineKeyboardButton(text=f'Опасение', callback_data=f'feel,Опасение') ],
    [InlineKeyboardButton(text=f'Смущение', callback_data=f'feel,Смущение') ],
    [InlineKeyboardButton(text=f'Сломленность', callback_data=f'feel,Сломленность') ],
    [InlineKeyboardButton(text=f'Подвох', callback_data=f'feel,Подвох') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'[5]', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])

iKB_Feels_6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Надменность', callback_data=f'feel,Надменность') ],
    [InlineKeyboardButton(text=f'Ошеломленность', callback_data=f'feel,Ошеломленность') ],
    [InlineKeyboardButton(text=f'Робость', callback_data=f'feel,Робость') ],
    [InlineKeyboardButton(text=f'Угрызения совести', callback_data=f'feel,Угрызения совести') ],
    [InlineKeyboardButton(text=f'Настороженность', callback_data=f'feel,Настороженность') ],
    [InlineKeyboardButton(text=f'Неловкость', callback_data=f'feel,Неловкость') ],
    [InlineKeyboardButton(text=f'Дискомфорт / Неудобство', callback_data=f'feel,Дискомфорт / Неудобство') ],
    [InlineKeyboardButton(text=f'Холодность', callback_data=f'feel,Холодность') ],
    [InlineKeyboardButton(text=f'Неполноценность', callback_data=f'feel,Неполноценность') ],
    [InlineKeyboardButton(text=f'Одиночество', callback_data=f'feel,Одиночество') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'[6]', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])
    
iKB_Feels_7 = InlineKeyboardMarkup(inline_keyboard=[    
    [InlineKeyboardButton(text=f'Грусть', callback_data=f'feel,Грусть') ],
    [InlineKeyboardButton(text=f'Тоскa', callback_data=f'feel,Тоскa') ],
    [InlineKeyboardButton(text=f'Горечь', callback_data=f'feel,Горечь') ],
    [InlineKeyboardButton(text=f'Скорбь', callback_data=f'feel,Скорбь') ],
    [InlineKeyboardButton(text=f'Жалость', callback_data=f'feel,Жалость') ],
    [InlineKeyboardButton(text=f'Жалость к себе', callback_data=f'feel,Жалость к себе') ],
    [InlineKeyboardButton(text=f'Отрешенность', callback_data=f'feel,Отрешенность') ],
    [InlineKeyboardButton(text=f'Беспомощность', callback_data=f'feel,Беспомощность') ],
    [InlineKeyboardButton(text=f'Душевная боль', callback_data=f'feel,Душевная боль') ],
    [InlineKeyboardButton(text=f'Отчужденность', callback_data=f'feel,Отчужденность') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'[7]', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])

iKB_Feels_8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Безвыходность', callback_data=f'feel,Безвыходность') ],
    [InlineKeyboardButton(text=f'Разочарование', callback_data=f'feel,Разочарование') ],
    [InlineKeyboardButton(text=f'Печаль', callback_data=f'feel,Печаль') ],
    [InlineKeyboardButton(text=f'Подавленность', callback_data=f'feel,Подавленность') ],
    [InlineKeyboardButton(text=f'Уныние', callback_data=f'feel,Уныние') ],
    [InlineKeyboardButton(text=f'Безысходность', callback_data=f'feel,Безысходность') ],
    [InlineKeyboardButton(text=f'Удрученность', callback_data=f'feel,Удрученность') ],
    [InlineKeyboardButton(text=f'Загнаность', callback_data=f'feel,Загнаность') ],
    [InlineKeyboardButton(text=f'Нервозность', callback_data=f'feel,Нервозность') ],
    [InlineKeyboardButton(text=f'Усталость', callback_data=f'feel,Усталость') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'[8]', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])

iKB_Feels_9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Потрясение', callback_data=f'feel,Потрясение') ],
    [InlineKeyboardButton(text=f'Сожаление', callback_data=f'feel,Сожаление') ],
    [InlineKeyboardButton(text=f'Скука', callback_data=f'feel,Скука') ],
    [InlineKeyboardButton(text=f'Безнадежность', callback_data=f'feel,Безнадежность') ],
    [InlineKeyboardButton(text=f'Тупик', callback_data=f'feel,Тупик') ],
    [InlineKeyboardButton(text=f'Равнодушие', callback_data=f'feel,Равнодушие') ],
    [InlineKeyboardButton(text=f'Огорчение', callback_data=f'feel,Огорчение') ],
    [InlineKeyboardButton(text=f'Лень', callback_data=f'feel,Лень') ],
    [InlineKeyboardButton(text=f'Апатия / безразличие', callback_data=f'feel,Апатия / безразличие') ],
    [InlineKeyboardButton(text=f'Отверженность', callback_data=f'feel,Отверженность') ],
    
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'[9]', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])
    
iKB_Feels_10 = InlineKeyboardMarkup(inline_keyboard=[    
    [InlineKeyboardButton(text=f'Неуверенность', callback_data=f'feel,Неуверенность') ],
    [InlineKeyboardButton(text=f'Радость', callback_data=f'feel,Радость') ],
    [InlineKeyboardButton(text=f'Счастье', callback_data=f'feel,Счастье') ],
    [InlineKeyboardButton(text=f'Восторг', callback_data=f'feel,Восторг') ],
    [InlineKeyboardButton(text=f'Ликование', callback_data=f'feel,Ликование') ],
    [InlineKeyboardButton(text=f'Приподнятость', callback_data=f'feel,Приподнятость') ],
    [InlineKeyboardButton(text=f'Оживление', callback_data=f'feel,Оживление') ],
    [InlineKeyboardButton(text=f'Окрыленность', callback_data=f'feel,Окрыленность') ],
    [InlineKeyboardButton(text=f'Кураж', callback_data=f'feel,Кураж') ],
    [InlineKeyboardButton(text=f'Увлечение', callback_data=f'feel,Увлечение') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'[10]', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])

iKB_Feels_11 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Интерес', callback_data=f'feel,Интерес') ],
    [InlineKeyboardButton(text=f'Влечение', callback_data=f'feel,Влечение') ],
    [InlineKeyboardButton(text=f'Вдохновение', callback_data=f'feel,Вдохновение') ],
    [InlineKeyboardButton(text=f'Ожидание', callback_data=f'feel,Ожидание') ],
    [InlineKeyboardButton(text=f'Возбуждение', callback_data=f'feel,Возбуждение') ],
    [InlineKeyboardButton(text=f'Воодушевление', callback_data=f'feel,Воодушевление') ],
    [InlineKeyboardButton(text=f'Предвкушение', callback_data=f'feel,Предвкушение') ],
    [InlineKeyboardButton(text=f'Надежда', callback_data=f'feel,Надежда') ],
    [InlineKeyboardButton(text=f'Любопытство', callback_data=f'feel,Любопытство') ],
    [InlineKeyboardButton(text=f'Освобождение', callback_data=f'feel,Освобождение') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'[11]', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])

iKB_Feels_12 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Принятие', callback_data=f'feel,Принятие') ],
    [InlineKeyboardButton(text=f'Довольство', callback_data=f'feel,Довольство') ],
    [InlineKeyboardButton(text=f'Блаженство', callback_data=f'feel,Блаженство') ],
    [InlineKeyboardButton(text=f'Изумление', callback_data=f'feel,Изумление') ],
    [InlineKeyboardButton(text=f'Удивление', callback_data=f'feel,Удивление') ],
    [InlineKeyboardButton(text=f'Одобрение', callback_data=f'feel,Одобрение') ],
    [InlineKeyboardButton(text=f'Энтузиазм', callback_data=f'feel,Энтузиазм') ],
    [InlineKeyboardButton(text=f'Удовольствие', callback_data=f'feel,Удовольствие') ],
    [InlineKeyboardButton(text=f'Экстаз', callback_data=f'feel,Экстаз') ],
    [InlineKeyboardButton(text=f'Удовлетворение', callback_data=f'feel,Удовлетворение') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'[12]', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])
    
iKB_Feels_13 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Обожание', callback_data=f'feel,Обожание') ],
    [InlineKeyboardButton(text=f'Дружелюбие', callback_data=f'feel,Дружелюбие') ],
    [InlineKeyboardButton(text=f'Взаимовыручка', callback_data=f'feel,Взаимовыручка') ],
    [InlineKeyboardButton(text=f'Спокойствие', callback_data=f'feel,Спокойствие') ],
    [InlineKeyboardButton(text=f'Любовь', callback_data=f'feel,Любовь') ],
    [InlineKeyboardButton(text=f'Благодарность', callback_data=f'feel,Благодарность') ],
    [InlineKeyboardButton(text=f'Теплота', callback_data=f'feel,Теплота') ],
    [InlineKeyboardButton(text=f'Доверие', callback_data=f'feel,Доверие') ],
    [InlineKeyboardButton(text=f'Вера', callback_data=f'feel,Вера') ],
    [InlineKeyboardButton(text=f'Нежность', callback_data=f'feel,Нежность') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'[13]', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])

iKB_Feels_14 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Влюбленность', callback_data=f'feel,Влюбленность') ],
    [InlineKeyboardButton(text=f'Симпатия', callback_data=f'feel,Симпатия') ],
    [InlineKeyboardButton(text=f'Самоценность / ценность', callback_data=f'feel,Самоценность / ценность') ],
    [InlineKeyboardButton(text=f'Любовь к себе', callback_data=f'feel,Любовь к себе') ],
    [InlineKeyboardButton(text=f'Комфорт', callback_data=f'feel,Комфорт') ],
    [InlineKeyboardButton(text=f'Безопасность', callback_data=f'feel,Безопасность') ],
    [InlineKeyboardButton(text=f'Защищенность', callback_data=f'feel,Защищенность') ],
    [InlineKeyboardButton(text=f'Забота', callback_data=f'feel,Забота') ],
    [InlineKeyboardButton(text=f'Доброта', callback_data=f'feel,Доброта') ],
    [InlineKeyboardButton(text=f'Жизнелюбие', callback_data=f'feel,Жизнелюбие') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'[14]', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])

iKB_Feels_15 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Очарованность', callback_data=f'feel,Очарованность') ],
    [InlineKeyboardButton(text=f'Искренность', callback_data=f'feel,Искренность') ],
    [InlineKeyboardButton(text=f'Раскаяние', callback_data=f'feel,Раскаяние') ],
    [InlineKeyboardButton(text=f'Умиротворение', callback_data=f'feel,Умиротворение') ],
    [InlineKeyboardButton(text=f'Гордость', callback_data=f'feel,Гордость') ],
    [InlineKeyboardButton(text=f'Восхищение', callback_data=f'feel,Восхищение') ],
    [InlineKeyboardButton(text=f'Уважение', callback_data=f'feel,Уважение') ],
    [InlineKeyboardButton(text=f'Смирение', callback_data=f'feel,Смирение') ],
    [InlineKeyboardButton(text=f'Сопричастность', callback_data=f'feel,Сопричастность') ],
    [InlineKeyboardButton(text=f'Сочувствие / сопереживание', callback_data=f'feel,Сочувствие / сопереживание') ],
        
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'[15]', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'16', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])

iKB_Feels_16 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f'Облегчение', callback_data=f'feel,Облегчение') ],
    [InlineKeyboardButton(text=f'Одобрение', callback_data=f'feel,Одобрение') ],
    [InlineKeyboardButton(text=f'Жизнерадостность', callback_data=f'feel,Жизнерадостность') ],
    [InlineKeyboardButton(text=f'Озарение', callback_data=f'feel,Озарение') ],
    [InlineKeyboardButton(text=f'Увереность', callback_data=f'feel,Увереность') ],
    [InlineKeyboardButton(text=f'Уравновешенность', callback_data=f'feel,Уравновешенность') ],
    
    [
    InlineKeyboardButton(text=f'1', callback_data=f'ikb,1'),
    InlineKeyboardButton(text=f'2', callback_data=f'ikb,2'),
    InlineKeyboardButton(text=f'3', callback_data=f'ikb,3'),
    InlineKeyboardButton(text=f'4', callback_data=f'ikb,4'),
    InlineKeyboardButton(text=f'5', callback_data=f'ikb,5'),
    InlineKeyboardButton(text=f'6', callback_data=f'ikb,6'),
    InlineKeyboardButton(text=f'7', callback_data=f'ikb,7'),
    InlineKeyboardButton(text=f'8', callback_data=f'ikb,8'),
    ],
    [
    InlineKeyboardButton(text=f'9', callback_data=f'ikb,9'),
    InlineKeyboardButton(text=f'10', callback_data=f'ikb,10'),
    InlineKeyboardButton(text=f'11', callback_data=f'ikb,11'),
    InlineKeyboardButton(text=f'12', callback_data=f'ikb,12'),
    InlineKeyboardButton(text=f'13', callback_data=f'ikb,13'),
    InlineKeyboardButton(text=f'14', callback_data=f'ikb,14'),
    InlineKeyboardButton(text=f'15', callback_data=f'ikb,15'),
    InlineKeyboardButton(text=f'[16]', callback_data=f'ikb,16'),
    ],
    [
    InlineKeyboardButton(text=f'✅ Завершить', callback_data=f'done,Finish'),
    ],
])




iKB_Feels = [
    iKB_Feels_1,
    iKB_Feels_2,
    iKB_Feels_3,
    iKB_Feels_4,
    iKB_Feels_5,
    iKB_Feels_6,
    iKB_Feels_7,
    iKB_Feels_8,
    iKB_Feels_9,
    iKB_Feels_10,
    iKB_Feels_11,
    iKB_Feels_12,
    iKB_Feels_13,
    iKB_Feels_14,
    iKB_Feels_15,
    iKB_Feels_16,
]