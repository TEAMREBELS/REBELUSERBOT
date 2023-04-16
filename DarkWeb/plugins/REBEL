import time

from DarkWeb.utils import admin_cmd, edit_or_reply, sudo_cmd
from DarkWeb import ALIVE_NAME, StartTime
from DarkWeb.smex.DARK_Config import Config


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
USERID = bot.uid
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


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


@dark.on(admin_cmd(outgoing=True, pattern="rebel$"))
@dark.on(sudo_cmd(pattern="rebel$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if DARK_IMG:
        REBEL_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        REBEL_caption += "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"
        REBEL_caption += "__**ʙᴏᴛ sᴛᴀᴛᴜs**__\n\n"
        REBEL_caption += "**➪ ᴛᴇʟᴇᴛʜᴏɴ :** `1.24.0`\n"
        REBEL_caption += f"**➪ ʀᴇʙᴇʟʙᴏᴛ :**`3.2`\n"
        REBEL_caption += f"**➪ ᴜᴘᴛɪᴍᴇ   :** `{uptime}\n`"
        REBEL_caption += f"**➪ ᴍᴀsᴛᴇʀ    :** {mention}\n"
        await alive.client.send_file(
            alive.chat_id, DARK_IMG, caption=REBEL_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ \n"
            f"     __**ʙᴏᴛ sᴛᴀᴛᴜs**__\n\n"
            f"**➪ ᴛᴇʟᴇᴛʜᴏɴ :** `1.24.0`\n"
            f"**➪ ʀᴇʙᴇʟʙᴏᴛ :** `3.2`\n"
            f"**➪ ᴜᴘᴛɪᴍᴇ      :** `{uptime}\n`"
            f"**➪ ᴍᴀsᴛᴇʀ        :** {mention}\n",
        )
