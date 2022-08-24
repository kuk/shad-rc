
from aiogram import (
    Bot,
    Dispatcher,
)
from aiogram.types import ParseMode

from neludim.const import BOT_TOKEN

from .middlewares import setup_middlewares
from .filters import setup_filters
from .handlers import setup_handlers


def init_bot():
    return Bot(
        token=BOT_TOKEN,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


def bot_dispatcher(bot):
    return Dispatcher(bot)


def setup_bot(context):
    setup_middlewares(context)
    setup_filters(context)
    setup_handlers(context)
