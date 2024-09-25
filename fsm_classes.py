from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


# fsm states for add admins
class AddAdmin(StatesGroup):
    admin_id = State()


# fsm users data
class DataUsers(StatesGroup):
    # - Как к вам обращаться?
    name = State()
    # - Заполним хэштег вида #имя_фамилия.
    tag = State()

    texts = {
        'DataUsers:name': 'Введите имя заново:',
        'DataUsers:tag': 'Введите хэштег вида #имя_фамилия:',
    }

# fsm states for add feel_check
class AddFeel(StatesGroup):
    waiting_data = State()


