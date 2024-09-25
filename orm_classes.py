from peewee import *
from settings import db_file


db = SqliteDatabase(db_file)


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    date_time = DateTimeField()
    class Meta:
        database = db

class User(BaseModel):
    user_id = IntegerField()
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    username = CharField(null=True)
    class Meta:
        db_table = 'users'

class Admin(BaseModel):
    admin_id = ForeignKeyField(User, unique=True)
    class Meta:
        db_table = 'admins'

# class Referal(BaseModel):
#     user_id = ForeignKeyField(User, unique=True)    # Кто пришел по рекомендации (по реферальной ссылке)
#     referer_id = ForeignKeyField(User)              # От кого пришел человек |  кто пригласил | реферер
#     class Meta:
#         db_table = 'referals'

class Feel(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField(max_length=100)
    class Meta:
        database = db

class FeelsCheck(BaseModel):
    feel_user_id = ForeignKeyField(User)
    feel_check = ForeignKeyField(Feel)
    class Meta:
        db_table = 'feel_check'



# class DataUser(BaseModel):
#     data_user_id = ForeignKeyField(User, unique=True)
#     data_user_feel = 
#     class Meta:
#         db_table = 'data_users'

