import os
# TOKEN = os.environ['TOKEN_BLAGODARU_BOT']
TOKEN = os.environ['TOKEN_MATRONA_FEELING_BOT']

db_file = 'db.sqlite'

# сколько нужно пригласить людей
referal_condition_count = 2

# админы
admins = [173625247]

# словарь чувств
feels = ["Гнев", "Обида", "Возмущсние", "Раздражение", "Злость", "Негодованне", "Недовольство", "Презрение", "Бешенство", "Ненависть", "Ярость", "Отвращение", "Неприязнь", "Истерия", "Ревность", "Зависть", "Досада", "Напряжение", "Страдание", "Протест", "Принужденке", "Пренебрежение", "Нетерпение", "Ераждебность", "Вседозволенность", "Вредность", "Высокомерне", "Превосходство", "Отверженне", "Уязвленность", "Страх", "Испуг", "Оцепенение", "Боязнь", "Ужас", "Отчаянне", "Тревога", "Ошарашенность", "Замешательство", "Растерянность", "Вина", "Стыд", "Беспокойство", "Сомненив", "Застенчивость", "Подозрение", "Опасенне", "Смущенне", "Сломленность", "Подвох", "Надменность", "Ошеломленность", "Робость", "Угрызення совести", "Настороженность", "Неловкость", "Дискомфорт/Неудобство", "Холодность", "НеполноценНость", "Одиночество", "Грусть", "Тоскa", "Горечь", "Скорбь", "Жалость", "Жалость ксебе", "Отрешенность", "Бесломощность", "Душевная боль", "Отчужденность", "Безвыходность", "Разочарование", "Печаль", "Подавленность", "Уныние", "Безысходность", "Удрученность", "Загнаность", "Нервозность", "Усталость", "Потрясение", "Сожаление", "Скука", "Без надежность", "Тупик", "Равнодушне", "Огорченне", "Лень", "Апатня/ безразличие", "Отверженность", "Неуверенность", "Радость", "Счастье", "Восторг", "Ликование", "Приподнятость", "Оживленне", "Окрыленность", "Кураж", "Увлеченне", "Интерес", "Влеченне", "Вдохновенне", "Ожидание", "Возбуждение", "Воодушевленне", "Предвкушенне", "Надежда", "Любопытство", "Освобождение", "Принятне", "Довольство", "Блаженство", "Изумление", "Удивление", "Одобрение", "Энтузиазм", "Удовольствке", "Экстаз", "Удовлетворение", "Обожание", "Дружелюбие", "Взанмовыручка", "Спокойствие", "Любовь", "Благодарно сть", "Теплота", "Доверие", "Вера", "Нежность", "Влюбленность", "Симпатня", "Самоценность / ценность", "Любовь Ксебе", "Комфорт", "Безоласность", "Защищенность", "Забота", "Доброта", "Жизнелюбие", "Очарованность", "Искренность", "Раскаянне", "Умиротворение", "Гордость", "Восхнщенне", "Уваженче", "Смирение", "Сопричастность", "Сочувствие / сопереживанне", "Облегчение", "Одобренне", "Жизнерадостность", "Озарение", "Увереность", "Уравновешенность"]