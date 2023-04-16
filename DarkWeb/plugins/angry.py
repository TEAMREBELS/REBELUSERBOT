import asyncio
import random
from telethon import events
from Dark.utils import admin_cmd

from . import *

@dark.on(admin_cmd(pattern=r"^🤬", outgoing=True))
@dark.on(sudo_cmd(pattern=r"^🤬", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "𝙸 𝚊𝚖 𝚊𝚗𝚐𝚛𝚢 ")
    deq = deque(list("😡🔥😡🔥🤬🔥🤬🔥🤬𝚅2.𝙾🔥😡🔥🤬😡🔥🤬🤬🔥😡"))
    for _ in range(100):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)
        
CmdHelp("𝚊𝚗𝚐𝚛𝚢").add_command(
  "🤬", None, "υѕє αи∂ ѕєє"
).add()