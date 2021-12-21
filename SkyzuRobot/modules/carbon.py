from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from SkyzuRobot import pbot
from SkyzuRobot.utils.errors import capture_err
from SkyzuRobot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_text(
        f"""✨ **Hey I'm 𝙳ᴇᴠɪʟ✗𝙰ɳɠɛƖ** 

**Owner repo : [𝗔𝖙𝖙𝖎𝖙𝖚𝖉𝖊 𝗸𝖎𝖓𝖌](https://t.me/Attitude_king_vj)**
**Python Version :** `{y()}`
**Library Version :** `{o}`
**Telethon Version :** `{s}`
**Pyrogram Version :** `{z}`

**join Support Group click button bellow.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support", url="https://t.me/tgcalls_MusicXchat"
                    ),
                    InlineKeyboardButton("Updates", url="https://t.me/tgcalls_Music_update"),
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
