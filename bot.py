from aiogram import Bot, Dispatcher
from aiogram.filters import ChatMemberUpdatedFilter, Command, CommandStart, MEMBER
from aiogram.types import ChatMemberUpdated, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from environs import Env
import random
import time

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

punchlines = [
    ["Если есть персонажи, то сюжет второстепенен.", "Хлеб насущный"],
    ["Релакс — после финала кубка; здесь нет других пенсионных планов.", "Саламандра"],
    ["Идеи не должны попахивать идиотизмом — они должны или не стесняясь разить им, или ходить по стеночке в пределах парадигмы.", "Иметь"]
]


def get_random_line() -> str:
    divination = random.choice(punchlines)
    ready_divination = f"{divination[0]}\n\n«{divination[1]}»"
    return ready_divination


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        'Этот бот отдаёт ссылки на релизы да страницы в соцсетях, '
        'гадает на строчках из треков '
        'и принимает донаты.\n'
        'Список команд — под кнопкой Menu.'
        )


apple_music_button = InlineKeyboardButton(
    text='Apple Music',
    url='https://music.apple.com/ru/artist/%D0%BC/1471116485'
)
spotify_button = InlineKeyboardButton(
    text='Spotify',
    url='https://open.spotify.com/artist/5HUVgeazK25dgyTE0dMKFN'
)
vk_music_button = InlineKeyboardButton(
    text='VK Музыка',
    url='https://vk.cc/8Ekyio'
)
vk_public_button = InlineKeyboardButton(
    text='VK',
    url='https://vk.com/mxxxxxxxxx'
)
yandex_music_button = InlineKeyboardButton(
    text='Яндекс.Музыка',
    url='https://music.yandex.ru/artist/4703830'
)
yandex_tips_button = InlineKeyboardButton(
    text='Яндекс.Чаевые',
    url='https://tips.yandex.ru/guest/payment/5730560'
)
youtube_channel_button = InlineKeyboardButton(
    text='YouTube',
    url='https://www.youtube.com/@mxxxxxxxxx'
)
youtube_music_button = InlineKeyboardButton(
    text='YouTube Music',
    url='https://music.youtube.com/channel/UCC1p_NyxmnshXCABr5tlmsg'
)

donations_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [yandex_tips_button]
    ]
)

social_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [vk_public_button],
        [youtube_channel_button]
    ]
)

streaming_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [apple_music_button],
        [spotify_button],
        [vk_music_button],
        [youtube_music_button],
        [yandex_music_button]
    ]
)


@dp.message(Command(commands='listen'))
async def process_listen_command(message: Message):
    await message.answer(
        text='Ссылки на стриминговые сервисы:',
        reply_markup=streaming_keyboard
        )


@dp.message(Command(commands='divine'))
async def process_divine_command(message: Message):
    time.sleep(1)
    await message.answer(
        get_random_line()
        )


@dp.message(Command(commands='subscribe'))
async def process_subscribe_command(message: Message):
    await message.answer(
        text='Подписаться:',
        reply_markup=social_keyboard
        )


@dp.message(Command(commands='support'))
async def process_support_command(message: Message):
    await message.answer(
        text='Спасибо!',
        reply_markup=donations_keyboard
        )


@dp.message()
async def process_other_answers(message: Message):
    await message.answer(
        'Увы, бот не понял команду — '
        'он умеет только выдавать ссылки на стриминги да официальные страницы, '
        'помогает гадать на строчках из треков '
        'и принимает донаты.\n'
        'Вот доступные команды: \n'
        '/listen — слушать треки на стриминговых сервисах\n'
        '/divine — гадать на строчках из треков\n'
        '/subscribe — подписаться на страницы\n'
        '/support — закинуть денег\n'
        'Список доступен под кнопкой Menu.'
        )


@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def process_user_unblocked_bot(event: ChatMemberUpdated):
    await bot.send_message(chat_id=event.from_user.id, text="С возвращением :)")


if __name__ == '__main__':
    dp.run_polling(bot)
