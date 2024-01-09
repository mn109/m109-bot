from aiogram import Bot, Dispatcher
#from environs import Env
import asyncio
import handlers
from config import Config, load_config

config: Config = load_config()
TOKEN: str = config.tg_bot.token

#env = Env()
#env.read_env()

#TOKEN = env('TOKEN')


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
