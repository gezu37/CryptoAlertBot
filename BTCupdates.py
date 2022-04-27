from aiogram import Dispatcher, types


async def cmd_subscribe(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Подписаться", callback_data="subscribe"))
    await message.answer("Подписаться на уведомления?", reply_markup=keyboard)


def register_handlers_subscribe(dp: Dispatcher):
    dp.register_message_handler(cmd_subscribe, commands="updates")
