import asyncio
import time
from telethon import version
from datetime import datetime

from DarkWeb import ALIVE_NAME, darkversion, StartTime
from DarkWeb.cmdhelp import CmdHelp
from DarkWeb.smex.DARK_Config import Config
from DarkWeb.utils import admin_cmd, sudo_cmd
from DarkWeb import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK WEB"

ludosudo = Config.SUDO_USERS

sudou = "True" if ludosudo else "False"
DARK = bot.uid

edit_time = 1
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/f81fb8ca000cf65364546.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "  __**π₯π₯βΞ±ΡΠΊΟΡΠ² bot ΞΉΡ ΟΞ·βΞΉΞ·Ρπ₯π₯**__\n\n" + "**ββββββββββββββββββββββ**\n\n"


pm_caption += (
    f"                βε½‘ πα©π’Ε¦οΌ₯ε°Ί ε½‘β\n                  **γ[{DEFAULTUSER}](tg://user?id={DARK})γ**\n\n"
)
pm_caption += "ββββββββββββββ\n"
pm_caption += f"β£ β«  Telethon β£ `{version.__version__}` \n"
pm_caption += f"β£ β« Version β£ `{darkversion}`\n"
pm_caption += f"β£ β« Sudo β£ `{sudou}`\n"
pm_caption += "β£ β« Creator β£ [Rebel](https://t.me/REBEL_IS_OP)\n"
pm_caption += "β£ β« Channel β£ [Join](https://t.me/DARK_WEB_UB)\n"
pm_caption += "β£ β« Support β£ [Support](https://t.me/DARK_WEB_BOT_SUPPORT)\n"
pm_caption += "ββββββββββββββββ\n"
pm_caption += " [π₯ππ΄πΏπΎπ₯](https://github.com/TEAMDARKS/DarkWeb) πΉ [ππ»πππππππ](https://github.com/TEAMDARKS/DarkWeb/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    DarkWeb = await edit_or_reply(alive, "`Building Alive....`")
    await alive.get_chat()
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1, caption=pm_caption)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "DARK WEB"
DARK_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "LEGENDARY AF DARK WEB"
mention = f"[{DEFAULTUSER}](tg://user?id={bot.uid})"

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += f"{time_list.pop()}, "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))
xnxx = (datetime.now() - datetime.now()).microseconds / 1000
    
@dark.on(admin_cmd(outgoing=True, pattern="dark$"))
@dark.on(sudo_cmd(pattern="dark$", allow_sudo=True))
async def amireallyalive(alive):
    smexxx = await edit_or_reply(alive, "`Building Alive....`")
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if DARK_IMG:
        REBEL_caption = f"**βΌ ΓwΓ±Γͺr β : {mention}\n"
        REBEL_caption +=    "____Κα΄α΄ sα΄α΄α΄α΄s____**\n"
        REBEL_caption += "β­ββββββββββββββ\n"
        REBEL_caption += f"β£β β£ Telethon β `1.24.0`\n"
        REBEL_caption += f"β£β β£ ΙaΚΣΥ‘ΙΙ?  β `1.0`\n"
        REBEL_caption += f"β£β β£ Uptime β `{uptime}`\n"
        REBEL_caption += f"β£β β£ Ping β   `{xnxx}`\n"
        REBEL_caption += f"β£β β£ Sudo β   `{sudou}`\n"
        REBEL_caption += "β°ββββββββββββββ"
        await alive.client.send_file(
            alive.chat_id, DARK_IMG, caption=REBEL_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**βΌ ΓwΓ±Γͺr β : {mention}\n"
                f"____Κα΄α΄ sα΄α΄α΄α΄s____**\n"
            "β­ββββββββββββββ\n"
            f"β£β β£ Telethon β `1.24.0`\n"
            f"β£β β£ ΙaΚΣΥ‘ΙΙ?  β `1.0`\n"
            f"β£β β£ Uptime β `{uptime}`\n"
            f"β£β β£ Ping β   `{xnxx}`\n"
            f"β£β β£ Sudo β   `{sudou}`\n"
            "β°ββββββββββββββ"
            ,
        )


CmdHelp("alive").add_command("alive", None, "To check am i alive").add_command(
    "dark", None, "To check am i alive with your favorite alive pic"
).add()
