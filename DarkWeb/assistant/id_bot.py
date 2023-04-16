from telethon import events
from telethon.utils import pack_bot_file_id


@tgbot.on(events.NewMessage(pattern="^/id"))
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await tgbot.send_message(
                event.chat_id,
                f"Current Chat ID: `{str(event.chat_id)}`\nFrom User ID: `{str(r_msg.sender_id)}`\nBot API File ID: `{bot_api_file_id}`",
            )

        else:
            await tgbot.send_message(
                event.chat_id,
                f"Current Chat ID: `{str(event.chat_id)}`\nFrom User ID: `{str(r_msg.sender_id)}`",
            )

    else:
        await tgbot.send_message(
            event.chat_id, f"Current Chat ID: `{str(event.chat_id)}`"
        )
