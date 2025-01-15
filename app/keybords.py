from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='chat',callback_data='chat')],
    [KeyboardButton(text='person', callback_data='person')],
    [KeyboardButton(text='help', callback_data='help')]
], resize_keyboard=True)


settings_pers= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='id',callback_data='link_pers')],
    [InlineKeyboardButton(text='link/username',callback_data='id_pers')]
    ])

settings_chat= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='id',callback_data='link_chat')],
    [InlineKeyboardButton(text='link/username',callback_data='id_chat')]
    ])

trakOranalitic= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='аналитика',callback_data='analitics')],
    [InlineKeyboardButton(text='трекинг',callback_data='trak')]
    ])
