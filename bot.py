from aiogram import Bot, Dispatcher, F
from aiogram.filters import ChatMemberUpdatedFilter, Command, CommandStart, MEMBER
from aiogram.types import ChatMemberUpdated, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Message, ReplyKeyboardMarkup
from environs import Env
import random
import time

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


button_1 = KeyboardButton(text="Слушать треки")
button_2 = KeyboardButton(text="Смотреть видео")
button_3 = KeyboardButton(text="Узнать новости")
button_4 = KeyboardButton(text="Гадать на строчках")
button_5 = KeyboardButton(text="Подписаться")
button_6 = KeyboardButton(text="Поддержать")
button_7 = KeyboardButton(text="Заказать бота")


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_1, button_2],
        [button_3, button_4],
        [button_5, button_6]
        ],
        resize_keyboard=True)

punchlines = [
    ["Если есть персонажи, то сюжет второстепенен.", "Хлеб насущный", "https://youtu.be/C1DWUpiuUJ4"],
    ["Если б награду давали на шару, она б не ценилась нисколько.", "Не подведи себя сам", "https://youtu.be/QeNoqtzEkx8"],
    ["Перед тем как стать опытным, ты подопытный.", "Исповедь", "https://youtu.be/luRD0QK6a2I"],
    ["Не можешь стать учителем — стань уроком.", "Полубог-полуживотное", "https://youtu.be/B-hMu2j9rLw"],
    ["Победа — полдела, дальше — больше.", "Викрамадитья", "https://youtu.be/lVQEURNbExA"],
    ["То, что не погубит, помотает нервы, вестимо!", "Костры амбиций", "https://youtu.be/MPwCMyxwVQE"],
    ["Этот путь вовсе не тупиковый — напротив, только он и ведёт к трону.", "Наверно", "https://youtu.be/V6Ri3PG8Q1Q"],
    ["Единственный козырь в колоде пока не менялся — это твёрдость руки.", "Так вышло", "https://youtu.be/B2qfITEt7-c"],
    ["Это типа ковчег, а мы тут за тварей.", "Белая княгиня", "https://youtu.be/I9KUJj2l0I4"],
    ["Истина порой восходит на нервной почве.", "Кипарис", "https://youtu.be/l5lM6BoRBMk"],
    ["Вполне хватает твоих действий, чтобы не вникать в смысл твоих слов.", "Позвони (третий раз за вечер)", "https://youtu.be/XGZ842LsPmU"],
    ["Мальчик боится мяча, пока не разобьют лицо.", "Впритык", "https://youtu.be/6w1z0BIt2NM"],
    ["Серьёзный мир — только глупости и приятны. Короче, на глупости вся надежда.", "А вдруг", "https://youtu.be/TE9UFNdOgx8"],
    ["Столько людей полыхнуло впустую, как пух — в каком качестве тебя приглашают к столу?", "С любовью", "https://youtu.be/HknPbkMPbHI"],
    ["Релакс — после финала кубка; здесь нет других пенсионных планов.", "Саламандра", "https://youtu.be/MsaSMWoEzUg"],
    ["Идеи не должны попахивать идиотизмом — они должны или не стесняясь разить им, или ходить по стеночке в пределах парадигмы.", "Иметь", "https://youtu.be/fWWpglvBP0M"]
]


def get_random_line() -> str:
    divination = random.choice(punchlines)
    ready_divination = f"{divination[0]}\n\n\n«{divination[1]}»\n{divination[2]}"
    return ready_divination


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        'Привет, это Миша. Я написал этого бота сам. '
        'Он отдаёт ссылки на релизы, видео и аккаунты в соцсетях, '
        'гадает на строчках из треков, '
        'отвечает на слегка набивший мне оскомину вопрос '
        'о перспективах и сроках выхода новой музыки, '
        'а также принимает помощь от благодарных слушателей.\n'
        'Полный список команд — под кнопкой Menu.',
        reply_markup=keyboard
        )


apple_music_button = InlineKeyboardButton(
    text="Apple Music",
    url="https://music.apple.com/ru/artist/%D0%BC/1471116485"
)
breaking_and_entering_button = InlineKeyboardButton(
    text="Клип «Кража со взломом»",
    url="https://youtu.be/sg7Vig3pFOk"
)
radical_poetry_live_button = InlineKeyboardButton(
    text="«Радикальная поэзия» (Live)",
    url="https://youtu.be/2eBvgMaZ73Y"
)
spotify_button = InlineKeyboardButton(
    text="Spotify",
    url="https://open.spotify.com/artist/5HUVgeazK25dgyTE0dMKFN"
)
suppose_button = InlineKeyboardButton(
    text="Клип «А вдруг»",
    url="https://youtu.be/1nrV5j6f-Bo"
)
suppose_live_button = InlineKeyboardButton(
    text="«А вдруг» (Live)",
    url="https://youtu.be/TE9UFNdOgx8"
)
vk_music_button = InlineKeyboardButton(
    text="VK Музыка",
    url="https://vk.cc/8Ekyio"
)
vk_public_button = InlineKeyboardButton(
    text="Паблик в VK",
    url="https://vk.com/mxxxxxxxxx"
)
yandex_music_button = InlineKeyboardButton(
    text="Яндекс.Музыка",
    url="https://music.yandex.ru/artist/4703830"
)
yandex_tip_button = InlineKeyboardButton(
    text="Яндекс.Чаевые",
    url="https://tips.yandex.ru/guest/payment/5730560"
)
youtube_channel_button = InlineKeyboardButton(
    text="YouTube-канал",
    url="https://www.youtube.com/@mxxxxxxxxx"
)
youtube_music_button = InlineKeyboardButton(
    text="YouTube Music",
    url="https://music.youtube.com/channel/UCC1p_NyxmnshXCABr5tlmsg"
)
youtube_playlist_button = InlineKeyboardButton(
    text="YouTube",
    url="https://www.youtube.com/playlist?list=PLlL8gwnKFC8oPdckcTSvjSZK5OLqkebLM"
)

donations_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [yandex_tip_button]
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
        [suppose_button],
        [suppose_live_button],
        [breaking_and_entering_button],
        [radical_poetry_live_button]
    ]
)


@dp.message(F.text == "Слушать треки")
@dp.message(Command(commands="listen"))
async def process_listen_command(message: Message):
    await message.answer(
        text='Ссылки на стриминговые сервисы:',
        reply_markup=streaming_keyboard
        )


@dp.message(F.text == "Узнать новости")
@dp.message(Command(commands="learn"))
async def process_learn_command(message: Message):
    await message.answer(
        'У меня порой интересуются, выпущу ли новые треки, '
        'и если да, то когда это счастье наступит. '
        'Какие-то песни давно готовы, '
        'какие-то пишутся прямо сейчас, '
        'но выйдут они все, когда стихнет стрельба. '
        'Я слышал доводы, что каждый должен заниматься своим делом, '
        'но, к счастью, могу себе позволить '
        'не выпускать музыку, пока гибнут люди.'
        )


@dp.message(F.text == "Смотреть видео")
@dp.message(Command(commands='watch'))
async def process_watch_command(message: Message):
    await message.answer(
        text='Видео:',
        reply_markup=watch_keyboard
        )


@dp.message(F.text == "Гадать на строчках")
@dp.message(Command(commands='divine'))
async def process_divine_command(message: Message):
    time.sleep(0.5)
    await message.answer(
        get_random_line()
        )


@dp.message(F.text == "Подписаться")
@dp.message(Command(commands="follow"))
async def process_follow_command(message: Message):
    await message.answer(
        text='Подписаться:',
        reply_markup=social_keyboard
        )


@dp.message(F.text == "Поддержать")
@dp.message(Command(commands="donate"))
async def process_donate_command(message: Message):
    await message.answer(
        text='Рад, что песни отзываются настолько, '
        'что возникает желание меня поддержать. '
        'Спасибо. Миша',
        reply_markup=donations_keyboard
        )


@dp.message(Command(commands="order"))
async def process_order_command(message: Message):
    await message.answer(
        text='Привет, это Миша. '
        'К счастью или несчастью '
        '(сам всю жизнь думаю то так, то этак), '
        'музыка никогда не кормила меня.\n'
        'Я бэкенд-разработчик. '
        'Написал этого бота на Python, '
        'использовав библиотеку aiogram — '
        'во-первых, креативного промо ради, '
        'а во-вторых — '
        'чтобы продемонстрировать верхушку айсберга '
        'моих потрясающих навыков программирования :)\n'
        'Если тебе нужен свой телеграм-бот — '
        'или Python backend developer '
        'с чувством прекрасного — пиши на почту\n'
        'ban.gully.0o@icloud.com'
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
