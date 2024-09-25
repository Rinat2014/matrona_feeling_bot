from datetime import datetime, timedelta
from aiogram.filters import CommandStart, Command, StateFilter 
from aiogram import F, Bot, types
from aiogram.types import Message, FSInputFile

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from services import *
# from create_bot import *
from create_bot import dp, bot
from keyboards import *
from settings import *
from fsm_classes import *



# ================================================== commands

@dp.message(CommandStart())
async def command_start_handler(msg: types.Message) -> None:
    # add user in db
    prn(msg)
    print("username = ", msg.chat.username, "       msg.from_user.id = ", msg.from_user.id)

    # если пользователь новый, добавляем в базу
    addUserDB(msg.from_user.id, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.username, msg.date)

    text = f'''Привет, {msg.chat.username}!
Данный бот поможет тебе заполнять почасовку чувств.
Для старта, нажимай кнопку внизу 👇
'''
    
    # если данных пользователя нету (первый запуск)
    if isDataUserAlreadyDB(msg.from_user.id):
        pass

    


    # try:
    if msg.text == '/start':
        pass # если отправлена команда /start (без параметров)
    else:
        # перешли по реферальной ссылке
        command, referer_id = msg.text.split(' ', 1)
        prn(f'referer {referer_id}', f'user {msg.from_user.id}' )
        
        addRefererDB(msg.from_user.id, referer_id, msg.date)
        print('addRefererDB DONE')
        
    
    # await msg.answer(text, reply_markup=iKM_start_btn)
    await msg.answer(text, reply_markup=KB_start_btn)
    # await msg.answer(text, reply_markup=KB_del)


# @dp.message(Command('help'))
# async def help_command(msg: Message) -> None:
#     text = '''Бот поможет вам зарегистрироваться на бесплатное наставничество Терра Челябинск. И получать оповещения от организаторов.'''
#     await msg.answer(text, reply_markup=iKM_help_btn)

@dp.message(Command('referal'))
async def referal_command(msg: Message) -> None:
    text = f'''Ваша реферальная ссылка URL?start={msg.from_user.id}'''
    await msg.answer(text)


@dp.message(Command('reflist'))
async def reflist_command(msg: Message) -> None:
    count, user_list = showRefererListDB(msg.from_user.id)
    text = f'''Список приглашенных людей ( {count} ) \n\n<pre>{user_list}</pre>'''
    await msg.answer(text)


@dp.message(Command('present'))
async def present_command(msg: Message) -> None:
    count, user_list = showRefererListDB(msg.from_user.id)
    if count >= 2:
        text = f''' У вас больше 2-х приглашенных. Получите обещаный подарок! '''
        present_file = 'who.pdf'
        await msg.answer(text)
        await msg.answer_document(FSInputFile(present_file))
    else:
        count_need = 2 - count
        text = f''' У вас меньше 2-х приглашенных.\nДля получения подарка, вам необходимо пригласить {getBeautifulDisplay(count_need)}'''
        await msg.answer(text)
        text = f'''Ваша реферальная ссылка URL?start={msg.from_user.id}'''
        await msg.answer(text)













































# ================================================== callbacks

''' обработка нажатий по кнопочкам почасовки чувств и эмоций '''
@dp.callback_query(AddFeel.waiting_data, F.data.startswith('feel'))
async def add_feel_handler(call: types.CallbackQuery, state: FSMContext):
    print(f'add_feel_handler = {call.data}')
    # await call.answer()
    # вытаскиваем команду и параметр - название чувства
    command, feel_name = call.data.split(',', 1)
    await call.answer(f"{feel_name} - сохранено")

    data = await state.get_data()
    print(f'data = {data}')
    user_data = data.get('user_data', [])
    # print(f'user_data = {user_data}')
    user_data.append(feel_name)
    # print(f'user_data append = {user_data}')
    # обновляем данные сессии
    await state.update_data(user_data=user_data)



''' завершаю заполнение почасовки '''
@dp.callback_query(AddFeel.waiting_data, F.data.startswith('done'))
async def finish_feel_handler(call: types.CallbackQuery, state: FSMContext):
    # print(f'finish_feel_handler = {call.data}')
    print('✅✅✅')
    prn(call)
    await call.answer()
    data = await state.get_data()
    print(f'data = {data}')
    user_data = data.get('user_data', [])
    print(f'user_data = {user_data}')
    date_time = datetime.datetime.now()
    # Прохожуь по всему массиву чувств и заношу в базу
    # for feel_name in user_data:
    if user_data:
        addManyFeelCheck(call.from_user.id, user_data)
        text = ', '.join(user_data)
    else:
        text = "Ждем в следующий раз 🙏"

    await state.clear()
    await call.message.edit_text(text, reply_markup=None)






''' переключение клавиатуры '''
@dp.callback_query(AddFeel.waiting_data, F.data.startswith('ikb'))
async def change_ikb_handler(call: types.CallbackQuery, state: FSMContext):
    command, num = call.data.split(',', 1)
    # ikb, feel, num = call.data.split('_', 3)
    num = int(num)
    print(f'num = {num}')
    text = f"Список чувств и эмоций: Страница {num} из {len(iKB_Feels)}"
    await call.message.edit_text(text, reply_markup=iKB_Feels[num-1])



































# ================================================== FSM start waiting_feel


# ''' создаем пользовательскую сессию и сессионный массив для хранения данных '''
# @dp.message(AddFeel.waiting_data)
# async def add_feel_save_handler(msg: Message, state: FSMContext):
    
#     # data = await state.get_data()
    
#     await state.update_data(admin_id=msg.text)
    
#     # if addNewAdminToDB(data):   text = 'Новый администратор добавлен!'
#     # else:                           text = f'⚠️ Ошибка '
        
#     # await state.clear()
#     text = 'начинаем сессию...'
#     await msg.answer(text)

















# # добавляем данные пользователя имя и хэштег
# @dp.message(StateFilter(None), F.text == 'Изменить данные')
# @dp.message(StateFilter(None), F.text == 'Ввести данные')
# async def add_name_handler(msg: Message, state: FSMContext):
#     await msg.answer('Введите ваше имя', reply_markup=KB_del)
#     await state.set_state(DataUsers.name)

# @dp.message(StateFilter('*'), Command('отмена'))
# @dp.message(StateFilter('*'), F.text.casefold() == 'отмена')
# async def cancel_handler(msg: Message, state: FSMContext) -> None:
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.clear()
#     await msg.answer('Отмена. Все данные сброшены.')




# @dp.message(StateFilter('*'), Command('назад'))
# @dp.message(StateFilter('*'), F.text.casefold() == 'назад')
# async def back_handler(msg: Message, state: FSMContext) -> None:
#     current_state = await state.get_state()
#     print(f'current_state = {current_state}')
#     # if current_state == DataUser.name:
#     #     await msg.answer('Предыдущего шага нет, введите ваше имя или напишите отмена')
#     # previous = None
#     # for step in DataUser.__all_states__:
#     #     if step.state == current_state:
#     #         await state.set_state(previous)
#     #         await msg.answer(f'Вы вернулись на предыдущий шаг\n{DataUser.texts[previous.state]}')
#     #         return
#     #     previous = step


# @dp.message(DataUsers.name, F.text)
# async def add_name_handler(msg: Message, state: FSMContext):
#     await state.update_data(name=msg.text)
#     await msg.answer('Введите хэштег вида #имя_фамилия')
#     await state.set_state(DataUsers.tag)


# @dp.message(DataUsers.tag, F.text)
# async def add_name_handler(msg: Message, state: FSMContext):
#     await state.update_data(tag=msg.text)
#     # await msg.answer('Ваши данные записаны:')
#     data = await state.get_data()
#     text = f'''<pre>Ваши данные:

# Ваше имя: {data['name']}
# Хэштег: {data['tag']}
# </pre>
# '''
#     # добавляем/обновляем данные пользователя 
#     addDataUsersToDB(msg.from_user.id, data['name'], data['tag'])

#     await msg.answer(text)
#     # await state.clear()
    

#     # await state.set_state(FinanceSurveyUsers.city)







# # добавляем данные пользователя имя и хэштег
# @dp.message(StateFilter(None), F.text == 'Изменить данные')
# @dp.message(StateFilter(None), F.text == 'Ввести данные')
# async def add_name_handler(msg: Message, state: FSMContext):
#     await msg.answer('Введите ваше имя', reply_markup=KB_del)
#     await state.set_state(DataUsers.name)

# @dp.message(StateFilter('*'), Command('отмена'))
# @dp.message(StateFilter('*'), F.text.casefold() == 'отмена')
# async def cancel_handler(msg: Message, state: FSMContext) -> None:
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.clear()
#     await msg.answer('Отмена. Все данные сброшены.')





















































# ================================================== Message

@dp.message(Command('hourly_feelings'))
@dp.message(StateFilter(None), F.text == 'Почасовка чувств')
# @dp.message(F.text == 'Почасовка чувств')
async def add_feel_handler(msg: Message, state: FSMContext) -> None:
    text = f"Список чувств и эмоций: Страница 1 из {len(iKB_Feels)}"
    text1 = f"Остановись, сделай несколько глубоких вдохов. Прислушайся к себе..."
    await state.set_state(AddFeel.waiting_data)
    await msg.delete()
    await msg.answer(text1, reply_markup=KB_del)
    await msg.answer(text, reply_markup=iKB_Feels_1)
    await state.update_data(data_msg_id=msg.message_id)
    prn(msg)





@dp.message(StateFilter('*'), F.text.casefold() == 'Почасовка чувств')
async def comment_feel_handler(msg: Message) -> None:
    text = "Вы уже начали заполнять список чувств и эмоций"
    await msg.answer(text)






# эхо сообщения с задержкой
# @dp.message()
# async def echo_handler(
#     message: types.Message, bot: Bot, apscheduler: AsyncIOScheduler
# ) -> None:
#     """
#     Handler will forward receive a message back to the sender

#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         dt = datetime.datetime.now() + timedelta(seconds=5)
#         # print(dt, bot, message.chat.id, message.text)
#         apscheduler.add_job(
#             send_message_scheduler,
#             trigger="date",
#             run_date=dt,
#             kwargs={
#                 "bot": bot,
#                 "message": message.text,
#                 "user_id": message.chat.id,
#             },
#         )
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")