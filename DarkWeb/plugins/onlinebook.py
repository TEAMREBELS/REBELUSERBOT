import datetime

from telethon import events

from telethon.errors.rpcerrorlist import YouBlockedUserError

from telethon.tl.functions.account import UpdateNotifySettingsRequest

from Dark.utils import admin_cmd



@dark.on(admin_cmd("ebook ?(.*)"))

async def _(event):

    if event.fwd_from:

        return 

    if not event.reply_to_msg_id:

       await event.edit("Reply to any number.")

       return

    reply_message = await event.get_reply_message() 

    if not reply_message.text:

       await event.edit("abe book ke name ko reply kar. ")

       return

    chat = "@zlibrarybot"
    sender = reply_message.sender

    async with borg.conversation(chat) as conv:

          try:     

              response = conv.wait_event(events.NewMessage(incoming=True,from_users=884313324))

              await borg.forward_messages(chat, reply_message)

              response = await response 

          except YouBlockedUserError: 

              await event.reply("```Please unblock @zlibrarybot and try again```")

              return

          if response.text.startswith("Unfortunately"):

             await event.edit("cant find this book check spell or give full name of book.still have problem contact @veryhelpful")

          else: 

             await event.edit(f"{response.message.message}")