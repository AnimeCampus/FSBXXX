# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from bot import Bot
from config import OWNER
from Data import Data
from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, Message


@Bot.on_message(filters.private & filters.incoming & filters.command("about"))
async def _about(client: Bot, msg: Message):
    await client.send_message(
        msg.chat.id,
        Data.ABOUT.format(client.username, OWNER),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.mbuttons),
    )


@Bot.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(client: Bot, msg: Message):
    try:
        await client.send_photo(
            msg.chat.id,
            photo="https://graph.org/file/120bf7519b24e50dd0b46.jpg",
            caption="<b>Donate..</b>\n" + Data.HELP,
            reply_markup=InlineKeyboardMarkup(Data.buttons),
            parse_mode="html",  # Set parse_mode to "html" for HTML formatting.
        )
    except Exception as e:
        print(f"Error sending image: {e}")



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        try:
            await query.message.edit_text(
                text=Data.ABOUT.format(client.username, OWNER),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.mbuttons),
            )
        except MessageNotModified:
            pass
    elif data == "help":
        try:
            await client.send_photo(
                chat_id=query.message.chat.id,
                photo=Data.HELP_IMAGE,  # Use the URL of the image you want to display.
                caption="<b>Donate..</b>\n" + Data.HELP,
                reply_to_message_id=query.message.message_id,
                parse_mode="html",
            )
        except MessageNotModified:
            pass
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass


