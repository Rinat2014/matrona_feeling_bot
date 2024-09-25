# Структура файла:

# Commands
# Callbacks
# FSM commands
# Messages






import xlwt
from datetime import datetime, timedelta

from aiogram import F, types
from aiogram.types import Message, FSInputFile
from aiogram.fsm.strategy import FSMStrategy
# from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


from settings import *
from services import *
# from orm_classes import *
from fsm_classes import *
from create_bot import dp, bot
from keyboards import *




from aiogram.filters import Command, StateFilter 
from aiogram import F, Bot, types


from services import *
# from create_bot import dp
# from terra_reports import dp
from keyboards import KB_start_btn
from settings import *














































# ================================================== commands


''' админка '''                             ''' набор кнопок для администрирования '''
@dp.message(Command('admin'))
async def admin_handler(msg: Message):
    if isAdmin(msg.from_user.id):
        pass
        msg_text = 'Админка'
        await msg.answer(msg_text, 
                         reply_markup=iKB_admin) # основное взаимодействие идет через клавиатуру
    else:
        pass
        msg_text = 'You are not admin!'
        await msg.answer(msg_text)













# ================================================================================ adminka
''' получаем файл базы  '''
@dp.message(Command('admin'))
async def admin_command(msg: Message) -> None:
    print('🔴 admin command - DB backup ', msg.chat.id, datetime.now())
    # запросивший должен быть админом
    if msg.chat.id == admin_id:
        await msg.answer_document(FSInputFile(db_file))


''' отправка сообщения всем пользователям  '''
@dp.message(Command('admin_send_message'))
async def send_message_command(msg: Message) -> None:
    print('🔴 admin command - send message all users', msg.chat.id, datetime.now())
    # запросивший должен быть админом
    if msg.chat.id == admin_id:
        # вытаскиваем id всех пользователей users_id
        users_id = getUsersId()
        print('users_id = ', users_id)
        for id in users_id:
            # msg = 'Message for all users'
            await bot.send_message(chat_id=int(id), text=message_for_all_users)











































# ================================================== callbacks


''' показать всех админов на удаление '''
@dp.callback_query(F.data == "show_admin_list_to_del")
async def show_admin_list(call: types.CallbackQuery):
    await call.answer()
    admins = Admin.select() # делаем всю выборку из базы по админам
    # 1) создать inline кнопку для удаления текущего админа
    # 2) подготовить сообщение с данными админа
    for admin in admins: # проходимся по каждому элементу и добавляем в сообщение на вывод
        text = f'<code>{admin.admin_id.user_id}</code> - {admin.admin_id.first_name} - @{admin.admin_id.username}\n'
        iKB_delete_admin = kbDelAdmin(admin.admin_id.first_name, admin.admin_id.user_id)     
        await call.message.answer(f'{text}', reply_markup=iKB_delete_admin)



''' удаляем конкретного админа '''
@dp.callback_query(F.data.startswith("drop_admin"))
async def delete_admin(call: types.CallbackQuery):
    await call.answer()
    command, drop_admin_id = call.data.split(',', 1)
    user = User.get(User.user_id == drop_admin_id) 
    admin = Admin.get(Admin.admin_id == user)
    admin.delete_instance() # удаляем этого админа
    # username = admin.admin_id.username if admin.admin_id.username != '' else 
    await call.message.answer(f'Пользователь  @{admin.admin_id.username} удален из администраторов')



''' показать всех админов '''
@dp.callback_query(F.data == "show_admins")
async def show_all_admins(call: types.CallbackQuery):
    await call.answer()
    if isAdmin(call.from_user.id):
        admins = Admin.select() # делаем всю выборку из базы по админам
        text = ''
        for admin in admins: # проходимся по каждому элементу и добавляем в сообщение на вывод
            text += f'<code>{admin.admin_id.user_id}</code> - {admin.admin_id.first_name} - @{admin.admin_id.username}\n'
        print(f'text = {text}')
        # text += ''
        await call.message.answer(f'<b>Список админов:</b>\n{text}')
    else:
        pass
        msg_text = 'You are not admin!'
        await call.message.answer(msg_text)



''' добавляем новых админов '''
@dp.callback_query(StateFilter(None), F.data == "add_admin")
async def add_new_admins(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    if isAdmin(call.from_user.id):
        await call.message.answer(f'Введите id пользователя, которого хотите сделать админом.\nЧтоб узнать свой id воспользуйтесь командой /me_info\nНовый администратор должен быть пользователем бота (минимум один раз запустить бота /start)')
        await state.set_state(AddAdmin.admin_id)
    else:
        msg_text = 'You are not admin!'
        await call.message.answer(msg_text)



''' вывод таблицы ответов для админа '''
@dp.callback_query(F.data == "fs_answers_to_admin")
async def get_answers_to_admin(call: types.CallbackQuery):
    await call.answer()

    # answers = Answer.select() # делаем всю выборку из базы
    # text = ''
    # for ans in answers:
    #     text += f'Имя: {ans.name}\nТелефон:<code>{ans.phone}</code> \nВопрос: {ans.description}\nДата: {ans.answer_date}\n\n'
    # print(f'text = {text}')
    text = 'Пока не работает, заходите в другой раз.'
    # text = 'Выводим данные ответов (админка)'
    await call.message.answer(f'<b>Данные: </b>\n\n{text}')


# ''' вывод таблицы ответов для админа в xls формате '''
# @dp.callback_query(F.data == "fs_answers_to_admin_xls")
# async def get_answers_to_admin_in_xls(call: types.CallbackQuery):
#     await call.answer()

#     if isAdmin(call.from_user.id):
#         text = 'данные в виде эксель таблицы'
#         await call.message.answer(f'<b>Данные: </b>\n\n{text}')

    #     # 1) Делаем выборку, которая нам нужна. По началу это будет вся база
    #     # 2) создаем файл xls, с которым будем работать, в формате: simple_inquirer_bot__iser_id.xls (нет необходимости, просто сохраняем с нужным именем)
    #     # 3) добавляем ему заголовки столбцов
    #     # 4) Проходимся по всему циклу ответов и заносим данные в xls файл
    #     # 5) сохраняем файл
    #     # 6) отправляем файл, ответом пользователю
    #     # готово
        
        
    #     # 1) Выборка
    #     fss = ''#FinancialSurvey.select() # делаем всю выборку из базы
        
    #     text = ''
    #     # 2) создаем файл для работы
    #     # now = datetime(call.message.date)
    #     now = call.message.date
    #     file_name = f'{now.strftime("%Y_%m_%d__%H_%M_%S")}__bot_reports.xls'
    #     # file_name = f'simple_inquirer_bot__{call.from_user.id}.xls'
    #     # 3) добавляем ему заголовки столбцов
    #     book = xlwt.Workbook(encoding="utf-8")
    #     sheet1 = book.add_sheet("Financial survey")
    #     sheet1.write(0, 0, "Имя")
    #     sheet1.write(0, 1, "Возраст")
    #     sheet1.write(0, 2, "Город")
    #     sheet1.write(0, 3, "Работа")
    #     sheet1.write(0, 4, "Уровень фин.грамотности")
    #     sheet1.write(0, 5, "Накопления")
    #     sheet1.write(0, 6, "Инструменты")
    #     sheet1.write(0, 7, "Пассивный доход")
    #     sheet1.write(0, 8, "Цели")
    #     sheet1.write(0, 9, "Обучение")
    #     sheet1.write(0, 10, "Моя польза для вас")
    #     sheet1.write(0, 11, "Телефон")
    #     sheet1.write(0, 12, "Дата")
    #     # 4) Проходимся по всему циклу ответов и заносим данные в xls файл
    #     for fs in fss:
    #         row = int(fs.id)
    #         sheet1.write(row, 0, fs.name)
    #         sheet1.write(row, 1, fs.age)
    #         sheet1.write(row, 2, fs.city)
    #         sheet1.write(row, 3, fs.job)
    #         sheet1.write(row, 4, fs.grade)
    #         sheet1.write(row, 5, fs.fin_count)
    #         sheet1.write(row, 6, fs.fin_tools)
    #         sheet1.write(row, 7, fs.fin_passive)
    #         sheet1.write(row, 8, fs.goals)
    #         sheet1.write(row, 9, fs.study)
    #         sheet1.write(row, 10, fs.benefit)
    #         sheet1.write(row, 11, fs.phone)
    #         sheet1.write(row, 12, fs.date_time)
    #     # 5) сохраняем файл
    #     book.save(file_name)
    #     # 6) отправляем файл, ответом пользователю
    #     # await call.answer_document(FSInputFile(my_csv_file), caption=f'rows {rows}')
    #     # await call.answer
    #     # await call.message.answer(f'<b>Данные: </b>\n\n{text}')
    #     await bot.send_document(call.from_user.id, FSInputFile(file_name), caption='Фин опросы')
    # else:
    #     pass
    #     msg_text = 'You are not admin!'
    #     await call.message.answer(msg_text)





































# ================================================== FSM add admins

''' добавляем нового админа - обработка присланного id-шника'''
@dp.message(AddAdmin.admin_id, F.text)
async def add_admin_save_handler(msg: Message, state: FSMContext):
    if isAdmin(msg.from_user.id):
        await state.update_data(admin_id=msg.text)
        data = await state.get_data()
        admin_id = data['admin_id']
        prn(admin_id)
        if addNewAdminToDB(admin_id):   text = 'Новый администратор добавлен!'
        else:                           text = f'⚠️ Ошибка '
            
        await state.clear()
        await msg.answer(text)

    else:
        await msg.answer('You are not admin! 🧐 ')