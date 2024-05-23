from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboards
import random
import time
import json

router = Router()

with open('punchlines.json', 'r', encoding='utf-8') as f:
    punchlines = json.load(f)

with open('messages.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)

START_MESSAGE = messages["START_MESSAGE"]
DONATE_MESSAGE = messages["DONATE_MESSAGE"]
FOLLOW_MESSAGE = messages["FOLLOW_MESSAGE"]
LEARN_MESSAGE = messages["LEARN_MESSAGE"]
LISTEN_MESSAGE = messages["LISTEN_MESSAGE"]
OTHER_MESSAGE = messages["OTHER_MESSAGE"]
WATCH_MESSAGE = messages["WATCH_MESSAGE"]

def get_random_line() -> str:
    divination = random.choice(punchlines)
    ready_divination = f"{divination['punchline']}\n\n\n«{divination['track_title']}»\n{divination['track_YouTube_link']}"
    return ready_divination


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        START_MESSAGE,
        reply_markup=keyboards.keyboard
        )


@router.message(F.text == "Слушать треки")
@router.message(Command(commands="listen"))
async def process_listen_command(message: Message):
    await message.answer(
        LISTEN_MESSAGE,
        reply_markup=keyboards.streaming_keyboard
        )


@router.message(F.text == "Узнать новости")
@router.message(Command(commands="learn"))
async def process_learn_command(message: Message):
    await message.answer(
        LEARN_MESSAGE,
        reply_markup=keyboards.keyboard
        )


@router.message(F.text == "Смотреть видео")
@router.message(Command(commands="watch"))
async def process_watch_command(message: Message):
    await message.answer(
        WATCH_MESSAGE,
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
        FOLLOW_MESSAGE,
        reply_markup=keyboards.social_keyboard
        )


@router.message(F.text == "Поддержать")
@router.message(Command(commands="donate"))
async def process_donate_command(message: Message):
    await message.answer(
        DONATE_MESSAGE,
        reply_markup=keyboards.donations_keyboard
        )


@router.message()
async def process_other_answers(message: Message):
    await message.answer(
        OTHER_MESSAGE
        )
