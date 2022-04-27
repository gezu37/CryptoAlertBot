import asyncio
import csv
from aiogram.types.bot_command import BotCommand
from aiogram.utils.exceptions import BotBlocked
from trend import register_handlers_trend
from MostSearch import register_handlers_searched
from BTCupdates import register_handlers_subscribe
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token="5088468387:AAHUbnEmXjZhDjSLefJ79nvpvVsAGS9_1qA", parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/trend", description="Показать максимальные рост и падения за последние сутки"),
        BotCommand(command="/searched", description="Показать какие монеты чаще всего искали в последнее время"),
        BotCommand(command="/updates", description="Ежедневные уведомления о цене BTC")
    ]
    await bot.set_my_commands(commands)


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")
    return True


@dp.callback_query_handler(text="subscribe")
async def subscribe(call: types.CallbackQuery):
    user_id = str(call.from_user.id)
    with open('users_id.csv', mode='w') as users_id:
        user_writer = csv.writer(users_id, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        user_writer.writerow(user_id)
    await call.message.answer("Вы подписались на уведомления по изменению цены Bitcoin")
    await call.answer()


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    register_handlers_trend(dp)
    register_handlers_searched(dp)
    register_handlers_subscribe(dp)

    await set_commands(bot)
    await dp.skip_updates()
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
    