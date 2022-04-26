from aiogram import Dispatcher, types
from MostSearchCollect import collect_data_search
import json
from aiogram.utils.markdown import hlink, hbold


async def mostsearched(message: types.Message):
    collect_data_search()

    with open('result_a.json') as file:
        data = json.load(file)
    for item in data:
        link_part = item.get("slug")
        link = f"https://coinmarketcap.com/ru/currencies/{link_part}/"
        answ = f'{hlink(item.get("name"), link)}\n' \
               f'{hbold("Price change24h: ")}{item.get("priceChange24h")}%\n'
        await message.answer(answ)


def register_handlers_searched(dp: Dispatcher):
    dp.register_message_handler(mostsearched, commands="searched")