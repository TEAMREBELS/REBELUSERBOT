from telethon import events

from DarkWeb import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "๐๐๐๐ ๐๐๐"
PM_IMG = "https://telegra.ph/file/8d3ef1032a204144ae074.mp4"
pm_caption = "โฅ **Assistant :** `ONLINE`\n\n" + "โฅ **ีYีTแดแฐี ีTแฉTี**\n"
pm_caption += "โฅ **Telethon:** `1.15.0` \n"
pm_caption += "โฅ **Python:** `3.8.6` \n"
pm_caption += "โฅ **Database Status:**  `Functional`\n"
pm_caption += "โฅ **Current Branch  ** : `master`\n"
pm_caption += f"โฅ **Version** : `2.0`\n"
pm_caption += f"โฅ **Master** : {DEFAULTUSER} \n"
pm_caption += "โฅ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "โฅ **License** : [GNU General Public License v3.0](github.com/REBEL75/REBELSBOTS/blob/master/LICENSE)\n"
pm_caption += "โฅ **CopyRight** :[ใ๐๐๐๐๐๐๐๐ใ](https://t.me/DARK_WEB_UB)\n"
pm_caption += "[ใ๐๐๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐๐๐๐ใ](https://t.me/DARK_WEB_UB)"

@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
