import asyncio
import requests
from telethon import functions

from DarkWeb.smex.DARK_Config import Config
from DarkWeb import CMD_LIST, SUDO_LIST
from Dark.utils import admin_cmd, edit_or_reply, sudo_cmd

@bot.on(admin_cmd(pattern="help ?(.*)", outgoing=True))
@bot.on(sudo_cmd(allow_sudo=True, pattern="help ?(.*)"))
async def yardim(event):
    if event.fwd_from:
        return
    tgbotusername = Config.BOT_USERNAME
    input_str = event.pattern_match.group(1)
    if tgbotusername is not None or REBEL_input == "text":
        results = await event.client.inline_query(tgbotusername, "@DARKWEB_HELP")
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await edit_or_reply(event, ["NO_BOT"])

        if input_str in CMD_LIST:
            string = "Commands found in {}:\n".format(input_str)
            for i in CMD_LIST[input_str]:
                string += "  " + i
                string += "\n"
            await event.edit(string)
        else:
            await event.edit(input_str + " is not a valid plugin!")
