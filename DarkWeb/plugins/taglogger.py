from telethon import custom, events
from telethon.tl.types import Channel
from telethon.utils import get_display_name

from DarkWeb.smex.DARK_Config import Config

if Config.DARKWEB_ID:
    tagger = int(Config.DARKWEB_ID)

if Config.DARKWEB_ID:

    @dark.on(
        events.NewMessage(
            incoming=True,
            blacklist_chats=Config.UB_BLACK_LIST_CHAT,
            func=lambda e: (e.mentioned),
        )
    )
    async def all_messages_catcher(event):
        # the bot might not have the required access_hash to mention the
        # appropriate PM
        await event.forward_to(Var.BOT_USERNAME)

        # construct message
        # the message format is stolen from @MasterTagAlertBot
        ammoca_message = ""

        R3b3l0p = await event.client.get_entity(event.sender_id)
        if R3b3l0p.bot or R3b3l0p.verified or R3b3l0p.support:
            return

        R3b3l0pm = f"[{get_display_name(R3b3l0p)}](tg://user?id={R3b3l0p.id})"

        where_ = await event.client.get_entity(event.chat_id)

        where_m = get_display_name(where_)
        button_text = "See the tag 📬"

        if isinstance(where_, Channel):
            message_link = f"https://t.me/c/{where_.id}/{event.id}"
        else:
            # not an official link,
            # only works in DrKLO/Telegram,
            # for some reason
            message_link = f"tg://openmessage?chat_id={where_.id}&message_id={event.id}"
            # Telegram is weird :\

        ammoca_message += f"{R3b3l0pm} `just tagged you...` \nWhere?\nIn [{where_m}]({message_link})\n__Tap to go the tagged msg__📬🚶"
        if tagger is not None:
            await bot.send_message(
                entity=tagger,
                message=ammoca_message,
                link_preview=False,
                buttons=[[custom.Button.url(button_text, message_link)]],
                silent=True,
            )
        else:
            return
