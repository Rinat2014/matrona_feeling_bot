import datetime
from orm_classes import *
from aiogram import Bot




# ================================================== services def

''' просто симпатичный вывод в консоль '''
def prn(arg = '', arg2=''):
    pass
    print('='*40, 'start')
    print()
    print(arg)
    print()
    print(arg2)
    print()
    print('='*40, 'end')



''' есть ли такой пользователь уже в таблице пользователей `Users`? '''
def isAlreadyDB(user_id):
    try:
        with db:
            user = User.get(User.user_id == user_id)
            if user:
                return True
            else:
                return False
    except DoesNotExist:
        print("Объект не найден в таблице `users`")
        print('⚠️⚠️ - isAlreadyDB', DoesNotExist)
        return False
    except Exception as e:
        print('⚠️⚠️⚠️ - isAlreadyDB', e)
        return False

''' есть ли данные пользователя в базе? '''
def isDataUserAlreadyDB(user_id):
    try:
        with db:
            user = User.get(User.user_id == user_id)
            print(f'user = {user}')
            data = DataUser.get(DataUser.user_id == user)
            print(f'data.user_name = {data}         data.user_tag = {data.user_tag}')
            if data.user_name and data.user_tag:
                return True
            else:
                return False
    except DoesNotExist:
        print("Объект не найден в таблице `users`")
        print('⚠️⚠️ - isAlreadyDB', DoesNotExist)
        return False
    except Exception as e:
        print('⚠️⚠️⚠️ - isAlreadyDB', e)
        return False


''' добавляем нового пользователя в базу, если его еще нет '''
def addUserDB(user_id, first_name, last_name, username, date_time):
    if isAlreadyDB(user_id):
        pass # если есть в базе, обновляем данные, если изменились
        print(f'⚠️ user = {username}    id = {user_id} - Already Exitsts')
    else:
        user = User( user_id = user_id, 
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    date_time = date_time).save()
        print('✅ добавили нового пользователя в базу')


''' проверяем, а не админ ли этот пользователь? '''
def isAdmin(id=0):
    admins_id = []
    admins = Admin.select() # делаем всю выборку из базы по id-шникам админов
     
    # print('='*40, 'admins')
    # print(admins)
    
    for admin in admins:
        print(f'admin id = {admin.admin_id.user_id}')
        admins_id.append(admin.admin_id.user_id)

    # print(f'admins_id = {admins_id}')
    
    if id in admins_id:
        return True
    else:
        return False

''' добавление нового админа в БД '''
def addNewAdminToDB(user_id, date_time):
    try:
        if isAdmin(user_id):
            pass # такой админ уже есть
        else:
            pass # добавляем нового админа
            user = User.get(User.user_id == user_id)
            print(user.user_id, user.username)
            with db:
                admin = Admin(
                    admin_id = user,
                    date_time = date_time
                ).save()
            print('✅ Add new admin in BD - DONE ')
            return True
    except Exception as e:
        print('⚠️⚠️⚠️ - addNewAdminToDB: ', e)
        return False


# def addDataUsersToDB(user_id, date_time, name, tag):
#     try:
#         user = User.get(User.user_id == user_id)
#         print(user.user_id, user.username)

#         data = DataUser.get()
#         with db:
#             data = DataUser(
#                 user_id = user,
#                 date_time = date_time,
#                 user_name = name,
#                 user_tag = tag
#             ).save()
#         print('✅ Add new admin in BD - DONE ')
#         return True
#     except Exception as e:
#         print('⚠️⚠️⚠️', e)
#         return False

''' отправляем сообщение с задержкой и кнопкой подтверждения '''
async def send_message_scheduler(bot: Bot, message: str, user_id: int):
    await bot.send_message(chat_id=int(user_id), text=message)



# ''' отправка сообщений '''
# async def send_user_message(bot: Bot, message: str, user_id: int):
#     await bot.send_message(chat_id=int(user_id), text=message)



''' этого пользователя уже приглашали ? '''
def isAlreadyInviteRefererdDB(user_id):
    try:
        with db:
            user = User.get(User.user_id == user_id)
            user_obj = Referal.get(Referal.user_id == user)
            if user_obj:
                return True
            else:
                return False
    except DoesNotExist:
        print("✅ Пользователь не найден в таблице, добавляем")
        print('⚠️⚠️ - isAlreadyInviteRefererdDB', DoesNotExist)
        return False
    except Exception as e:
        print('⚠️⚠️⚠️ - isAlreadyInviteRefererdDB', e)
    

''' фиксируем кто кого пригласил '''
def addRefererDB(user_id, referer_id, date_time):
    # 1) мимо идут: приглашение самого себя
    # 2) уже приглашенные
    # 3) записываем только уникальных приглашенных

    print(user_id, referer_id, 'addReferralsDB start =================================')

    
    
    
    print('print(int(user_id) == int(referer_id)) =         ', int(user_id) == int(referer_id))
    
    # print(isAlreadyInviteRefererdDB(user_id))

    if int(user_id) == int(referer_id): # (1)
        print('самаклик ===========')
        return
    elif isAlreadyInviteRefererdDB(user_id):   # (2)
        print('уже приглашали ===========')
        return
    else:                               # (3)    уникальный челик
        try:
            with db:
                user    = User.get(User.user_id == user_id)
                referer = User.get(User.user_id == referer_id)
                if user and referer:    
                    ref = Referal( user_id = user, 
                                   referer_id = referer,
                                   date_time = date_time).save()
                    print('✅ добавили ref  user_id = ', user_id, ' referer_id = ', referer_id)
                    return
                
        except DoesNotExist:
            print("Объект не найден в таблице")
            print('⚠️⚠️ - addRefererDB', DoesNotExist)
            return
        except Exception as e:
            print('⚠️⚠️⚠️ - addRefererDB', e)
            return
    
    
    
    print(user_id, referer_id, 'addReferralsDB finish =================================')





''' Сколько приглашенных '''
def countRefererDB(referer_id):
    try:
        with db:
            count_referer = Referal.select(Referal.referer_id == referer_id)
            len_count_referer = len(count_referer)
            print('len count_referer = ', len_count_referer )
            return len_count_referer
    except DoesNotExist:
        print("Объект не найден в таблице")
        print('⚠️⚠️ - countRefererDB', DoesNotExist)
    except Exception as e:
        print('⚠️⚠️⚠️ - countRefererDB', e)



def showRefererListDB(referer_id):
    try:
        with db:
            
            user_referer = User.get(User.user_id == referer_id) # находим в таблице пользователей
            all_referers = Referal.select().where(Referal.referer_id == user_referer) # ищем всех кого пригласил
            
            len_count_referer = len(all_referers)
            print('all referer = ', len_count_referer )
            # prn('showRefererListDB', str(referer))
            user_list = ''
            for ref in all_referers:
                user_list += f'{ref.user_id.first_name}\n'
            
            print(f'{user_list}')


            return len_count_referer, user_list
    except DoesNotExist:
        print("Объект не найден в таблице")
        print('⚠️⚠️ - showRefererListDB', DoesNotExist)
    except Exception as e:
        print('⚠️⚠️⚠️ - showRefererListDB', e)



def getUsersId():
    try:
        with db:
            users_id = []
            users = User.select() 
            for user in users:
                users_id.append(user.user_id)
                print(user.user_id)
            
            # print(f'{user_list}')


            return users_id
    except DoesNotExist:
        print("Объект не найден в таблице")
        print('⚠️⚠️ - showRefererListDB', DoesNotExist)
    except Exception as e:
        print('⚠️⚠️⚠️ - showRefererListDB', e)


def getBeautifulDisplay(n):
    if n == 1: return '1-го человека' 
    if n == 2: return '2-х человек' 
    if n > 2 and n < 9: return f'n-х человек'  
    if n >= 9: return f'n человек'  



''' добавляем таблицу чувств '''
def addFeels():
    from settings import feels
    try:
        with db:
            # date_time = datetime.datetime.now()
            # print(f'date_time = {date_time}')
            for feel_name in feels:
                feel = Feel( name = feel_name ).save()
                # return True
        print('✅ Add feels in BD - DONE ')
    except Exception as e:
        print('⚠️⚠️⚠️ - addFeels:', e)
    

# ''' создаем инлайн кнопки для чувств '''
# def inlineFeelButtons():
#     pass

def addFeelCheck(user_id, feel_name, date_time=None):
    try:
        with db:
            if date_time:   pass
            else:           date_time = datetime.datetime.now()
            
            user = User.get(User.user_id == user_id)
            feel = Feel.get(Feel.name == feel_name)
            feel_check = FeelsCheck(feel_user_id = user, feel_check = feel, date_time = date_time ).save()
            
        print('✅ feel_check - DONE ')
    except Exception as e:
        print('⚠️⚠️⚠️ - addFeelCheck:', e)


def addManyFeelCheck(user_id, feel_names):
    try:
        with db:
            date_time = datetime.datetime.now()
            user = User.get(User.user_id == user_id)

            feels = []

            for feel_name in feel_names:
                feel = Feel.get(Feel.name == feel_name)
                feels.append({'feel_user_id':user, 'feel_check':feel, 'date_time':date_time})

            print(f'feels------------------\n{feels}')    
                
                
            # feel = Feel.get(Feel.name == feel_name)
            # feel_check = FeelsCheck(feel_user_id = user, feel_check = feel, date_time = date_time ).save()
            FeelsCheck.insert_many(feels).execute()
            
            print(f'user_id = {user} \nfeel_names = {feel_names}')
            
        print('✅✅✅✅✅ feel_check - DONE ')
    except Exception as e:
        print('⚠️⚠️⚠️ - addFeelCheck:', e)