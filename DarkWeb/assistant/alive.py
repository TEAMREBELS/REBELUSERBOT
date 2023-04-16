from telethon import events

from DarkWeb import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝐃𝐀𝐑𝐊 𝐖𝐄𝐁"
PM_IMG = "https://telegra.ph/file/8d3ef1032a204144ae074.mp4"
pm_caption = "➥ **Assistant :** `ONLINE`\n\n" + "➥ **ՏYՏTᗴᗰՏ ՏTᗩTՏ**\n"
pm_caption += "➥ **Telethon:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.8.6` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch  ** : `master`\n"
pm_caption += f"➥ **Version** : `2.0`\n"
pm_caption += f"➥ **Master** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/REBEL75/REBELSBOTS/blob/master/LICENSE)\n"
pm_caption += "➥ **CopyRight** :[『𝐑𝐄𝐁𝐄𝐋𝐁𝐎𝐓』](https://t.me/DARK_WEB_UB)\n"
pm_caption += "[『𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓 𝐁𝐘 𝐃𝐀𝐑𝐊𝐖𝐄𝐁』](https://t.me/DARK_WEB_UB)"

@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
