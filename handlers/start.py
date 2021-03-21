from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I Hi [OFFLINE] ꜱʜᴀᴍɪʟ 🇮🇳🇮🇳 😉️!

I'm Group Music Bot Friend of @shamilnelli 😏️.

I can play Music In Telegram Groups Via Voice Chat! 😌️.

Made with ❤️ @redbullfed.

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ How To Use This Bot", url="https://telegra.ph/How-To-Use-TGMusicsBot-03-21"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 creator", url="https://t.me/shamilnelli"
                    ),
                    InlineKeyboardButton(
                        "support group 🔈", url="https://t.me/redbullfed"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
