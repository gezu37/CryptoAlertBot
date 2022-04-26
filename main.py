import asyncio
from aiogram.types.bot_command import BotCommand
from trend import register_handlers_trend
from MostSearch import register_handlers_searched
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token="5088468387:AAHUbnEmXjZhDjSLefJ79nvpvVsAGS9_1qA", parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/trend", description="Показать максимальные рост и падения за последние сутки"),
        BotCommand(command="/searched", description="Показать какие монеты чаще всего искали в последнее время")
    ]
    await bot.set_my_commands(commands)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    register_handlers_trend(dp)
    register_handlers_searched(dp)

    await set_commands(bot)
    await dp.skip_updates()
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
    