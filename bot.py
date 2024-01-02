from aiogram import Bot, Dispatcher
from aiogram.filters import ChatMemberUpdatedFilter, Command, CommandStart, MEMBER
from aiogram.types import ChatMemberUpdated, InlineKeyboardButton, InlineKeyboardMarkup, Message
from environs import Env
import random
import time

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

punchlines = [
    ["Если есть персонажи, то сюжет второстепенен.", "Хлеб насущный", "https://youtu.be/C1DWUpiuUJ4"],
    ["Если б награду давали на шару, она б не ценилась нисколько.", "Не подведи себя сам", "https://youtu.be/QeNoqtzEkx8"],
    ["Перед тем как стать опытным, ты подопытный.", "Исповедь", "https://youtu.be/luRD0QK6a2I"],
    ["Не можешь стать учителем — стань уроком.", "Полубог-полуживотное", "https://youtu.be/B-hMu2j9rLw"],
    ["Победа — полдела, дальше — больше.", "Викрамадитья", "https://youtu.be/lVQEURNbExA"],
    ["Мальчик боится мяча, пока не разобьют лицо.", "Впритык", "https://youtu.be/6w1z0BIt2NM"],
  #  [],
    ["Столько людей полыхнуло впустую, как пух — в каком качестве тебя приглашают к столу?", "С любовью", "https://youtu.be/HknPbkMPbHI"],
    ["Релакс — после финала кубка; здесь нет других пенсионных планов.", "Саламандра", "https://youtu.be/MsaSMWoEzUg"],
    ["Идеи не должны попахивать идиотизмом — они должны или не стесняясь разить им, или ходить по стеночке в пределах парадигмы.", "Иметь", "https://youtu.be/fWWpglvBP0M"]
]


def get_random_line() -> str:
    divination = random.choice(punchlines)
    ready_divination = f"{divination[0]}\n\n\n\n\n«{divination[1]}»\n{divination[2]}"
    return ready_divination


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        'Этот бот отдаёт ссылки на релизы, видео и страницы М в соцсетях, '
        'гадает на строчках из его треков ',
        'сообщает о перспективах выхода новой музыки'
        'и принимает помощь.\n'
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
    text='Паблик в VK',
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
    text='YouTube-канал',
    url='https://www.youtube.com/@mxxxxxxxxx'
)
youtube_playlist_button = InlineKeyboardButton(
    text='Плейлист на YouTube',
    url='https://www.youtube.com/playlist?list=PLlL8gwnKFC8oPdckcTSvjSZK5OLqkebLM'
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

watch_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [youtube_playlist_button]
    ]
)


@dp.message(Command(commands='listen'))
async def process_listen_command(message: Message):
    await message.answer(
        text='Ссылки на стриминговые сервисы:',
        reply_markup=streaming_keyboard
        )


@dp.message(Command(commands='learn'))
async def process_learn_command(message: Message):
    await message.answer(
        'У меня порой интересуются, выпущу ли новые треки, '
        'и если да, то когда это счастье наступит. '
        'Песни выйдут, когда стихнет стрельба — '
        'я слышал доводы, что каждый должен заниматься своим делом, '
        'но, к счастью, могу себе позволить не выпускать музыку, '
        'пока люди натурально гибнут.'
        )


@dp.message(Command(commands='watch'))
async def process_watch_command(message: Message):
    await message.answer(
        text='Плейлист с видео:',
        reply_markup=watch_keyboard
        )


@dp.message(Command(commands='divine'))
async def process_divine_command(message: Message):
    time.sleep(1)
    await message.answer(
        get_random_line()
        )


@dp.message(Command(commands='follow'))
async def process_follow_command(message: Message):
    await message.answer(
        text='Подписаться:',
        reply_markup=social_keyboard
        )


@dp.message(Command(commands='support'))
async def process_support_command(message: Message):
    await message.answer(
        text='Привет, это Миша. '
        'Рад, что песни отзываются настолько, '
        'что возникает желание меня поддержать! '
        'Под этим сообщением — ссылка на Яндекс.Чаевые.\n'
        'Но особо ценной — бесценной! — помощью будет, '
        'если тем или иным образом устроишь мне собеседование '
        'в какую-нибудь компанию на должность бэкенд-разработчика на Python — '
        'я сам написал этого бота-визитку, '
        'использовав библиотеку aiogram, '
        'чтобы продемонстрировать верхушку айсберга '
        'моих невероятных навыков программирования :)\n'
        'Почта: ban.gully.0o@icloud.com',
        reply_markup=donations_keyboard
        )


@dp.message()
async def process_other_answers(message: Message):
    await message.answer(
        'Увы, бот не понял команду. '
        'Список команд доступен по кнопке Menu.'
        )


@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def process_user_unblocked_bot(event: ChatMemberUpdated):
    await bot.send_message(chat_id=event.from_user.id, text="С возвращением :)")


if __name__ == '__main__':
    dp.run_polling(bot)
