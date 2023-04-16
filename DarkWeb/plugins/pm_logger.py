"""Log Pm messages into a private group

"""
import asyncio
import logging
import os
import sys
from asyncio import sleep

from telethon import events

from DarkWeb import bot
from DarkWeb.smex.DARK_Config import Config
from Dark.utils import admin_cmd, register
from DarkWeb.cmdhelp import CmdHelp

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARN
)

NO_PM_LOG_USERS = []

BOTLOG_CHATID = Config.DARKWEB_ID

@dark.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(event):
    sender = await event.get_sender()
    if Config.NO_PM_LOG_USERS and not sender.bot:
        chat = await event.get_chat()
        if chat.id not in NO_PM_LOG_USERS and chat.id != bot.uid:
            try:
                e = await bot.get_entity(int(Config.DARKWEB_ID))
                fwd_message = await bot.forward_messages(e, event.message, silent=True)
            except Exception as e:
                # logger.warn(str(e))
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print(e)


@dark.on(admin_cmd(pattern="elog ?(.*)"))
async def set_no_log_p_m(event):
    if Config.DARKWEB_ID is not None:
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id in NO_PM_LOG_USERS:
                NO_PM_LOG_USERS.remove(chat.id)
                await event.edit("Will Log Messages from this chat")
                await asyncio.sleep(3)
                await event.delete()


@dark.on(admin_cmd(pattern="nlog ?(.*)"))
async def set_no_log_p_m(event):
    if Config.DARKWEB_ID is not None:
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id not in NO_PM_LOG_USERS:
                NO_PM_LOG_USERS.append(chat.id)
                await event.edit("Won't Log Messages from this chat")
                await asyncio.sleep(3)
                await event.delete()

CmdHelp("pm_logger").add_command(
  "elog", "<chat>", "Enables logging pm messages from the selected chat."
).add_command(
  "nlog", "<chat>", "Disables logging pm messages from the selected chat. Use .elog to enable it again."
).add()
