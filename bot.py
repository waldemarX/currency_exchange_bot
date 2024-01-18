import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

logger = logging.getLogger(__name__)


async def main() -> None:

    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
               '%(lineno)d - %(name)s - %(message)s'
        )
    logger.info('Starting bot')

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
