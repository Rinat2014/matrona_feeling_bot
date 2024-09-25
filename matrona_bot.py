'''
Телеграм бот почасовки чувств  
pip install aiogram peewee apscheduler xlwt

pip install aiogram
pip install peewee
pip install apscheduler
pip install xlwt
'''

import asyncio
import logging
import sys
# import xlwt
import datetime

from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from middleware import SchedulerMiddleware


from settings import *
from settings import admins
from services import *
from orm_classes import *
from fsm_classes import *
from create_bot import dp
import create_bot
from handlers import users, admin, other

from settings import TOKEN   # @matrona_feeling_bot   TOKEN_MATRONA_FEELING_BOT

# ==================================================

# dp = Dispatcher()


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    
    global bot
    # global dp
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    create_bot.bot = bot
    

    # And the run events dispatching
    scheduler = AsyncIOScheduler()
    timezone="Europe/Moscow"

    dp.update.middleware(
        SchedulerMiddleware(scheduler=scheduler),
    )
    scheduler.start()
    await bot.delete_webhook(True)
    await dp.start_polling(bot)






# ================================================== init
def starting_data_admins():
    # добавить данные по админам
    with db:
        # добавляем админов, если база пустая
        # ''' добавление нового админа в БД '''
        # def addNewAdminToDB(user_id, date_time):
        try:
            date_time = datetime.datetime.now()
            print(f'date_time = {date_time}')
            for a_id in admins:
                print(f'a_id = {a_id}')
                # Добавляем шаблон пользователя в базу addUserDB(user_id, first_name, last_name, username, date_time):
                addUserDB(a_id, "", "", "", date_time)
                
                user = User.get(User.user_id == a_id)
                print(user.user_id, user.username)
                
                admin = Admin(
                    admin_id = user,
                    date_time = date_time
                ).save()
                
                print('✅ Add new admin in BD - DONE ')
                # return True
        except Exception as e:
            print('⚠️⚠️⚠️', e)
            # return False

def starting_data_feels():
    # добавить таблицу чувств
    addFeels()    
    print('✅ DONE addFeels  ')
     


def init_db():
    with db:
        db.create_tables([User, Admin, Feel, FeelsCheck])
    print('✅ DONE DB  ')







if __name__ == "__main__":
    print('[INFO] - bot starting ✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅')
    # temp()
    
    # init_db()
    # starting_data_admins()
    # starting_data_feels()
    
    logging.basicConfig(level=logging.INFO, 
                        stream=sys.stdout, 
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    try:
        asyncio.run( main() )
    except KeyboardInterrupt:
        print('✅✅ Goodby')