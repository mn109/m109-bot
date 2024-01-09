from aiogram import Bot, Dispatcher
import asyncio
import handlers
from config import Config, load_config

config: Config = load_config()
TOKEN: str = config.tg_bot.token


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
