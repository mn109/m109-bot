from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboards
import random
import time
import data

router = Router()

punchlines = data.punchlines


def get_random_line() -> str:
    divination = random.choice(data.punchlines)
    ready_divination = f"{divination[0]}\n\n\n«{divination[1]}»\n{divination[2]}"
    return ready_divination


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(data.START_MESSAGE,
                         reply_markup=keyboards.keyboard
                         )


@router.message(F.text == "Слушать треки")
@router.message(Command(commands="listen"))
async def process_listen_command(message: Message):
    await message.answer(
        data.LISTEN_MESSAGE,
        reply_markup=keyboards.streaming_keyboard
        )


@router.message(F.text == "Узнать новости")
@router.message(Command(commands="learn"))
async def process_learn_command(message: Message):
    await message.answer(
        data.LEARN_MESSAGE,
        reply_markup=keyboards.keyboard
        )


@router.message(F.text == "Смотреть видео")
@router.message(Command(commands="watch"))
async def process_watch_command(message: Message):
    await message.answer(
        data.WATCH_MESSAGE,
        reply_markup=keyboards.watch_keyboard
        )


@router.message(F.text == "Гадать на строчках")
@router.message(Command(commands="divine"))
async def process_divine_command(message: Message):
    time.sleep(1)
    await message.answer("☴")
    time.sleep(1)
    await message.answer(
        get_random_line()
        )


@router.message(F.text == "Подписаться")
@router.message(Command(commands="follow"))
async def process_follow_command(message: Message):
    await message.answer(
        data.FOLLOW_MESSAGE,
        reply_markup=keyboards.social_keyboard
        )


@router.message(F.text == "Поддержать")
@router.message(Command(commands="donate"))
async def process_donate_command(message: Message):
    await message.answer(
        data.DONATE_MESSAGE,
        reply_markup=keyboards.donations_keyboard
        )


@router.message(Command(commands="order"))
async def process_order_command(message: Message):
    await message.answer(
        data.ORDER_MESSAGE,
        reply_markup=keyboards.keyboard
    )


@router.message()
async def process_other_answers(message: Message):
    await message.answer(
        data.OTHER_MESSAGE
        )
