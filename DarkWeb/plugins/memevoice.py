# Credits to @spechide and his team for @TROLLVOICEBOT
# made by @R3b3l0p_the_badass from the snippets of waifu AKA stickerizerbot....
# kang karega kya madarchod?
# aukaat h bsdk teri...jake baap ka loda chus ke aa....


import re

from DarkWeb import bot
from Dark.utils import admin_cmd, sudo_cmd, edit_or_reply
from DarkWeb.cmdhelp import CmdHelp
from DarkWeb.helpers.functions import deEmojify


@dark.on(admin_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@dark.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(R3b3l0p):
    Dark = R3b3l0p.pattern_match.group(1)
    if not Dark:
        if R3b3l0p.is_reply:
            (await R3b3l0p.get_reply_message()).message
        else:
            await edit_or_reply(R3b3l0p, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(Dark))}")

    await troll[0].click(
        R3b3l0p.chat_id,
        reply_to=R3b3l0p.reply_to_msg_id,
        silent=True if R3b3l0p.is_reply else False,
        hide_via=True,
    )
    await R3b3l0p.delete()
    

CmdHelp("memevoice").add_command(
  "mev", "<meme txt>", "Searches and uploads the meme in voice format (if any)."
).add()
