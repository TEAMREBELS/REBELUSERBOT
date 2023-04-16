import asyncio
from asyncio import sleep
import telethon.utils
from telethon import events
from telethon.errors import rpcbaseerrors

from DarkWeb import BOTLOG, BOTLOG_CHATID, CMD_HELP
from Dark.utils import admin_cmd, sudo_cmd, errors_handler, edit_or_reply
from DarkWeb.cmdhelp import CmdHelp
from Dark.util import re

async def get_target_message(event):
    if event.is_reply and (await event.get_reply_message()).sender_id == borg.uid:
        return await event.get_reply_message()
    async for message in borg.iter_messages(await event.get_input_chat(), limit=20):
        if message.out:
            return message


async def await_read(chat, message):
    chat = telethon.utils.get_peer_id(chat)

    async def read_filter(read_event):
        return read_event.chat_id == chat and read_event.is_read(message)

    fut = borg.await_event(events.MessageRead(inbox=False), read_filter)

    if await is_read(borg, chat, message):
        fut.cancel()
        return

    await fut


@dark.on(admin_cmd(pattern="(del)(?:ete)?$"))
@dark.on(admin_cmd(pattern="(edit)(?:\s+(.*))?$"))
async def delete(event):
    await event.delete()
    command = event.pattern_match.group(1)
    if command == "edit":
        text = event.pattern_match.group(2)
        if not text:
            return
    target = await get_target_message(event)
    if target:
        chat = await event.get_input_chat()
        await await_read(chat, target)
        await asyncio.sleep(0.5)
        if command == "edit":
            await borg.edit_message(chat, target, text)
        else:
            await borg.delete_messages(chat, target, revoke=True)

@dark.on(admin_cmd(pattern=r"purge", outgoing=True))
@dark.on(sudo_cmd(pattern=r"purge", allow_sudo=True))
@errors_handler
async def fastpurger(purg):
    """ For .purge command, purge all messages starting from the reply. """
    chat = await purg.get_input_chat()
    msgs = []
    count = 0

    async for msg in purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "`Fast purge complete!\n`Purged " + str(count) + " messages.",
    )

    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID, "Purge of " + str(count) + " messages done successfully."
        )
    await sleep(2)
    await done.delete()


# @register(outgoing=True, pattern="^.purgeme")
@dark.on(admin_cmd(pattern=r"purgeme", outgoing=True))
@dark.on(sudo_cmd(pattern=r"purgeme", allow_sudo=True))
@errors_handler
async def purgeme(delme):
    """ For .purgeme, delete x count of your latest message."""
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "`Purge complete!` Purged " + str(count) + " messages.",
    )
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID, "Purge of " + str(count) + " messages done successfully."
        )
    await sleep(2)
    i = 1
    await smsg.delete()


@dark.on(admin_cmd(pattern=r"sd", outgoing=True))
@dark.on(sudo_cmd(pattern=r"sd", allow_sudo=True))
@errors_handler
async def selfdestruct(destroy):
    """ For .sd command, make seflf-destructable messages. """
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID, "sd query done successfully")

CmdHelp("purge").add_command(
  "del", "<reply to a msg>", "Deletes the replied msg."
).add_command(
  "edit", "<reply to a msg>", "Edits the replied msg"
).add_command(
  "purge", "<reply>", "Purges all messages starting from the reply."
).add_command(
  "purgeme", "<count>", "Deletes 'x' amount of your latest messages."
).add_command(
  "sd", "<time> <message>", "Creates a message that selfdestructs in 'x' seconds. Keep the seconds under 100 since it puts your bot to sleep"
).add()
