import re

from DarkWeb import bot
from Dark.utils import admin_cmd, sudo_cmd, edit_or_reply
from DarkWeb.cmdhelp import CmdHelp
from DarkWeb.helpers.functions import deEmojify


@dark.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@dark.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(R3b3l0p):
    Dark = R3b3l0p.pattern_match.group(1)
    if not Dark:
        if R3b3l0p.is_reply:
            (await R3b3l0p.get_reply_message()).message
        else:
            await edit_or_reply(R3b3l0p, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(Dark))}")

    await troll[0].click(
        R3b3l0p.chat_id,
        reply_to=R3b3l0p.reply_to_msg_id,
        silent=True if R3b3l0p.is_reply else False,
        hide_via=True,
    )
    await R3b3l0p.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()
