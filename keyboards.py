from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


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
    resize_keyboard=True
    )


apple_music_button = InlineKeyboardButton(
    text="Apple Music",
    url="https://music.apple.com/ru/artist/%D0%BC/1471116485"
)
breaking_and_entering_button = InlineKeyboardButton(
    text="Клип «Кража со взломом»",
    url="https://youtu.be/sg7Vig3pFOk"
)
github_button = InlineKeyboardButton(
    text="Код бота на GitHub",
    url="https://github.com/mn109/m109-bot"
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
telegram_channel_button = InlineKeyboardButton(
    text="Канал в Telegram",
    url="https://t.me/mxxxxgram"
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
yandex_tips_button = InlineKeyboardButton(
    text="Яндекс.Чаевые",
    url="https://tips.yandex.ru/guest/payment/5730560"
)
youtube_button = InlineKeyboardButton(
    text="YouTube",
    url="https://www.youtube.com/channel/UCC1p_NyxmnshXCABr5tlmsg"
)
youtube_music_button = InlineKeyboardButton(
    text="YouTube Music",
    url="https://music.youtube.com/channel/UCC1p_NyxmnshXCABr5tlmsg"
)

dev_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [github_button]
    ]
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
