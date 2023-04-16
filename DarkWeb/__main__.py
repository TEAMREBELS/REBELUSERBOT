import os
from sys import argv
import sys
import asyncio
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon import Button, TelegramClient, custom, events
from telethon import TelegramClient
from var import Var
from DarkWeb.smex.DARK_Config import Config
from DarkWeb import bot
from DarkWeb import *
from DarkWeb.utils import load_module, start_assistant
from DarkWeb import LOAD_PLUG, darkversion
from pathlib import Path
import telethon.utils

chuty = "Config.BOT_USERNAME"
REBEL_PIC = "https://telegra.ph/file/31bfaed9335e61d61b084.jpg"
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)

os.system("pip install -U telethon")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        print("Initialisation finished with no errors")
        print("🔰ՏTᗩᖇT 𝘿𝘼𝙍𝙆𝙒𝙀𝘽🔰")
        bot.loop.run_until_complete(add_bot(Var.BOT_USERNAME))
        print("⚡𝘿𝘼𝙍𝙆𝙒𝙀𝘽 𝘾𝙊𝙈𝙋𝙇𝙀𝙏𝙀 𝙎𝙀𝙏𝙐𝙋⚡")
    else:
        bot.start()


import glob
path = 'DarkWeb/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))
        

if LOAD_ASSISTANT == True:
    path = "DarkWeb/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                start_assistant(shortname.replace(".py", ""))
            except Exception as er:
                print(er)
else:
    print("Assitant is Not Loading As U Have Disabled")


import DarkWeb._core

print(f"""Hello sir i am DarkWeb!! DarkWeb VERSION :- {Darkversion} YOUR DarkWeb IS READY! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES https://t.me/DARK_WEB_UB .""")

xnxx = f"ɖaʀӄաɛɮ ɮօȶ ɪs ᴅᴇᴘʟᴏʏᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ \n\n ᴛʀʏ ᴄᴏᴍᴍᴀɴᴅ `.ping` ᴀɴᴅ `.dark` \n\n ᴀɴʏ ǫᴜᴇʀʏ/ɪssᴜᴇ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇʀʏ/ɪssᴜᴇ \n\n ᴛʜᴀɴᴋs ғᴏʀ ᴅᴇᴘʟᴏʏɪɴɢ"
# xvideo = [            
#                  [
#                     Button.url(" αѕѕιѕтαηт ", "https://t.me/{chuty}?start=True"),
#                     Button.url(" ѕυρρσят ¢нαт ", "https://t.me/DARK_WEB_BOT_SUPPORT"),
#                 ],
#             ],

async def DARK_is_on():
    try:
        if Config.DARKWEB_ID != 0:
            await bot.send_file(Config.DARKWEB_ID, REBEL_PIC, caption=xnxx,)
    except Exception as e:
        LOGS.info(str(e))

bot.loop.create_task(DARK_is_on())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
