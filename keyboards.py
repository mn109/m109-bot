from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import json

with open('keyboards.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

buttons = data["buttons"]

button_1 = KeyboardButton(text=buttons["listen"])
button_2 = KeyboardButton(text=buttons["watch"])
button_3 = KeyboardButton(text=buttons["learn"])
button_4 = KeyboardButton(text=buttons["divine"])
button_5 = KeyboardButton(text=buttons["follow"])
button_6 = KeyboardButton(text=buttons["donate"])

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_1, button_2],
        [button_3, button_4],
        [button_5, button_6]
    ],
    resize_keyboard=True
)

apple_music_button = InlineKeyboardButton(
    text=buttons["apple_music"]["text"],
    url=buttons["apple_music"]["url"]
)
breaking_and_entering_button = InlineKeyboardButton(
    text=buttons["breaking_and_entering"]["text"],
    url=buttons["breaking_and_entering"]["url"]
)
radical_poetry_live_button = InlineKeyboardButton(
    text=buttons["radical_poetry_live"]["text"],
    url=buttons["radical_poetry_live"]["url"]
)
spotify_button = InlineKeyboardButton(
    text=buttons["spotify"]["text"],
    url=buttons["spotify"]["url"]
)
suppose_button = InlineKeyboardButton(
    text=buttons["suppose"]["text"],
    url=buttons["suppose"]["url"]
)
suppose_live_button = InlineKeyboardButton(
    text=buttons["suppose_live"]["text"],
    url=buttons["suppose_live"]["url"]
)
telegram_channel_button = InlineKeyboardButton(
    text=buttons["telegram_channel"]["text"],
    url=buttons["telegram_channel"]["url"]
)
vk_music_button = InlineKeyboardButton(
    text=buttons["vk_music"]["text"],
    url=buttons["vk_music"]["url"]
)
vk_public_button = InlineKeyboardButton(
    text=buttons["vk_public"]["text"],
    url=buttons["vk_public"]["url"]
)
yandex_music_button = InlineKeyboardButton(
    text=buttons["yandex_music"]["text"],
    url=buttons["yandex_music"]["url"]
)
yandex_tips_button = InlineKeyboardButton(
    text=buttons["yandex_tips"]["text"],
    url=buttons["yandex_tips"]["url"]
)
youtube_button = InlineKeyboardButton(
    text=buttons["youtube"]["text"],
    url=buttons["youtube"]["url"]
)
youtube_music_button = InlineKeyboardButton(
    text=buttons["youtube_music"]["text"],
    url=buttons["youtube_music"]["url"]
)

donations_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [yandex_tips_button]
    ]
)

social_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [telegram_channel_button],
        [vk_public_button]
    ]
)

streaming_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [apple_music_button],
        [spotify_button],
        [vk_music_button],
        [youtube_button],
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
