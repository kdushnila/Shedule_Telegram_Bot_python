import asyncio
import logging

from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from schedule_func import schedule_function

logger = logging.getLogger(__name__)


async def main():
    logger.info("Starting bot")

    bot: Bot = Bot(token='Your bot token')
    dp: Dispatcher = Dispatcher()

    @dp.message(CommandStart())
    async def process_start_command(message: Message):
        await message.answer(text="Bot has started")
        print(message.from_user.id)
        schedule_function()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
