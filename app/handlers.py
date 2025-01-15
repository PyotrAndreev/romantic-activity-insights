from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keybords as kb

import asyncpg
DATABASE_CONFIG = {
    "host": "project-for-love-sikalovaes.db-msk0.amvera.tech",
    "port": 5432,
    "user": "admin",
    "password": "YFIk.,jdysqghjtrn3",
    "database": "dblove"
}
async def get_db_connection():
    return await asyncpg.connect(**DATABASE_CONFIG)

router= Router()

class Reg(StatesGroup):
    name=State()

class Reg_two(StatesGroup):
    name=State()

class Reg_link(StatesGroup):
    name=State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в бот!\n Наш бот поможет получить аналитику о человеке, время его максимальной активности и аналитику чата в Telegram. \n Под строкой у вас появились кнопки, выберите какую информацию вы хотите получить: о человеке или чате',
                          reply_markup=kb.main)

@router.message(Command('id'))
async def cmd_id(message: Message):
    await message.reply(f'Привет. Твой ID:{message.from_user.id}')



@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда help')


@router.message(F.text == 'chat')
async def how_are_you(message: Message):
    await message.answer('Вы выбрали аналитику чата!\n Выберите способ отправки адреса: ссылка или id', 
                         reply_markup=kb.settings_chat)

@router.message(F.text == 'person')
async def how_are_you(message: Message):
    await message.answer('Вы выбрали аналитику человека! Выберите, какая информация вам интересна: аналитика человека или трекинг активности человека', reply_markup=kb.trakOranalitic)

@router.callback_query(F.data == 'analitics')
async def how_are_you(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Вы выбрали аналитику человека!\n Выберите способ отправки адреса: ссылка или id', 
                         reply_markup=kb.settings_pers)

@router.callback_query(F.data == 'trak')
async def how_are_you(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Вы выбрали трекинг человека!\n Выберите способ отправки адреса: ссылка или id', 
                         reply_markup=kb.settings_pers)


@router.callback_query(F.data == 'link_pers')
async def link_pers(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    # await callback.message.answer('Отправьте ссылку на человека!')
    await state.set_state(Reg_link.name)
    await callback.message.answer('Введите ссылку человека')

@router.callback_query(F.data == 'link_chat')
async def link_chat(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    # await callback.message.answer('Отправьте ссылку на чат!')
    await state.set_state(Reg_link.name)
    await callback.message.answer('Введите ссылку чата')

@router.callback_query(F.data == 'id_pers')
async def id_pers(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    # await callback.message.answer('Отправьте id человека!')
    await state.set_state(Reg.name)
    await callback.message.answer('Введите ID человека')

# @router.callback_query(F.data == 'id_chat')
# async def id_chat(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.answer('Отправьте id чата!')


@router.callback_query(F.data == 'id_chat')
async def id_chat(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    # await callback.message.answer('Отправьте id чата!')
    await state.set_state(Reg_two.name)
    await callback.message.answer('Введите ID чата')



@router.message(F.text == 'help')
async def how_are_you(message: Message):
    await message.answer('По всем вопросам обращайтесь к Петру \n'
                         )


@router.message(Reg_link.name)
async def reg_two(message:Message, state:FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    # await state.set_state()
    await message.answer(f'Спасибо! Ждите информацию. Сейчас информации не будет')
    await state.clear()

@router.message(Reg.name)
async def reg(message:Message, state:FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await state.set_state()
    await message.answer(f'Спасибо! Ждите информацию по ID: {data["name"]}')
    conn = await get_db_connection()
    rows = await conn.fetch("SELECT text FROM tg_groups_messages LIMIT 3")


        


    rows = await conn.fetch(f"SELECT * FROM tg_users_last WHERE user_name= '{data["name"]}'")
    await conn.close()

    if rows:
        response = "\n".join([str(row) for row in rows])
    else:
        response = "Данные отсутствуют."

    await message.answer(f"Получены данные:\n{response}")
    await state.clear()
        



@router.message(Reg_two.name)
async def reg_two(message:Message, state:FSMContext):
    try:
        await state.update_data(name=message.text)
        data = await state.get_data()
        await state.set_state()
        await message.answer(f'Спасибо! Ждите информацию по ID: {data["name"]}')
        
      
        conn = await get_db_connection()
       
        rows = await conn.fetch("SELECT * FROM tg_groups_messages LIMIT 3")
        # rows = await conn.fetch(f"SELECT * FROM tg_groups_messages WHERE chat_id= '{data["name"]}'")
        await conn.close()

        if rows:
            response = "\n".join([str(row) for row in rows])
        else:
            response = "Данные отсутствуют."

        await message.answer(f"Получены данные:\n{response}")
        await state.clear()
        
    except Exception as e:
        await message.answer(f"Ошибка при получении данных: {e}\n Попробуйте снова (нажмите на кнопку)")




@router.message(Command("check_db"))
async def cmd_check_db(message: Message):
    try:
        # Пробуем подключиться к базе данных
        conn = await get_db_connection()
        await conn.close()  # Закрываем подключение после проверки
        await message.answer("Подключение к базе данных успешно установлено.")
    except Exception as e:
        # Если возникла ошибка, сообщаем её
        await message.answer(f"Ошибка подключения к базе данных: {e}")

