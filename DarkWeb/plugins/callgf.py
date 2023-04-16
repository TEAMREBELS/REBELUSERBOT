"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio
from Dark.utils import admin_cmd, edit_or_reply, sudo_cmd

from DarkWeb.cmdhelp import CmdHelp


@dark.on(admin_cmd(pattern=r"callgf"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

   # input_str = event.pattern_match.group(1)

   # if input_str == "call":

    await event.edit("𝗖𝗮𝗹𝗹𝗶𝗻𝗴")

    animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` [Legend](t.me/Legend_Mr_Hacker) ,`Please Connect me to my Gf,@Sweetie_Kumari`",
            "`User Authorised.`",
            "`Calling Girlfriend Of legend`  `At +917254561556`",
            "`Private  Call Connected...`",
            "`Me: Hello Dear, Please Ban This Telegram Account.`",    
            "`GF: May I Know Who Is This?`",
            "`Me: Yo Brah, itz me`  ",
            "`GF: OMG!!! Long time no see, Wassup LEGEND...\nI'll Make Sure That Guy Account Will Get Banned Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`GF: Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`GF: Yes Sir, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
            "`GF: Sure Sur \nTC Bye Bye ;)`",
            "`Private Call Disconnected.`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])
CmdHelp("callgf").add_command(
    'callgf', None, 'From Using This U will get username of LegendGirlFriend'
).add()
