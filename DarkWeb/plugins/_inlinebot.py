from math import ceil
from re import compile
import asyncio

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import JoinChannelRequest

from DarkWeb import *
from DarkWeb.cmdhelp import *
from Dark.utils import *
from DarkWeb.smex.DARK_Config import Config

Dark_help_pic = Config.HELP_PIC
Dark_row = Config.BUTTONS_IN_HELP
Dark_emoji = Config.EMOJI_IN_HELP
HANDLER = Config.HNDLR


DEFAULTUSER = ALIVE_NAME or "DARK WEB"
USERID = bot.uid
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"

if REBEL_help_pic := Config.HELP_PIC:
    _file_to_replace = REBEL_help_pic
    REBEL_help_pic = REBEL_help_pic
else:
    _file_to_replace = "https://telegra.ph/file/fda905425952724bc9277.jpg"

def button(page, modules):
    Row = Dark_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"{Dark_emoji} " + pair, data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"◀️ ᏰᎯᏣᏦ {Dark_emoji}", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"•{Dark_emoji} ❌ {Dark_emoji}•", data="close"
            ),
            custom.Button.inline(
               f"{Dark_emoji} ᏁᏋﾒᎿ ▶️", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]
 
    modules = CMD_HELP
if Var.BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@DARKWEB_HELP":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            result = await builder.photo(
                file=_file_to_replace,
                text=f"**༆ {mention} ༆**\n__Total Module installed__ ⭆ `{len(CMD_HELP)}`\n**page⭆ ** 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        elif event.text=='':
            result = builder.article(
                "@DarkBOT_SUPPORT",
                text=f"""**Hey! This is DarkBOT\nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        custom.Button.url("🔥 CHANNEL 🔥", "https://t.me/DARK_WEB_UB"),
                        custom.Button.url(
                            "⚡ GROUP ⚡", "https://t.me/DARK_WEB_BOT_SUPPORT"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "🔰 REPO 🔰", "https://github.com/Dark75/DarkBOTOP"),
                        custom.Button.url
                    (
                            "🔰 TUTORIAL 🔰", ""
                    )
                    ],
                ],
                link_preview=True,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "ʏօʊ ƈaռ'ȶ ʊֆɛ \n @ ɖaʀӄաɛɮ ™",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"**༆ {mention} ༆**\n__Total Module installed__ ⭆ `{len(CMD_HELP)}`\n**page⭆ ** 1/{veriler[0]}",
            buttons=veriler[1],
            link_preview=True,
        )
        
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await delete_Dark(event,
              f"⚜️DarkBOT Menu Provider Is now Closed⚜️\n\n         **[© DarkBOT ™](t.me/DarkBOT_SUPPORT)**[⚡🔥]({Dark_help_pic})", 5, link_preview=True
            )
        else:
            Dark_alert = "ʏօʊ ƈaռ'ȶ ʊֆɛ \n @ ɖaʀӄաɛɮ ™"
            await event.answer(Dark_alert, cache_time=0, alert=True)
          
    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "ʏօʊ ƈaռ'ȶ ʊֆɛ \n @ ɖaʀӄաɛɮ ™",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "🔷" + cmd[0], data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("◀️ ᏰᎯᏣᏦ", data=f"page({page})")])
        await event.edit(
            f"**📗 File:** `{commands}`\n**🔢 Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "ʏօʊ ƈaռ'ȶ ʊֆɛ \n @ ɖaʀӄաɛɮ ™",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**📗 File:** `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                result += f"**⚠️ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
        else:
            result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 Commands:** `{HANDLER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 Commands:** `{HANDLER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"**💬 Explanation:** `{command['usage']}`\n\n"
        else:
            result += f"**💬 Explanation:** `{command['usage']}`\n"
            result += f"**⌨️ For Example:** `{HANDLER[:1]}{command['example']}`\n\n"

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("◀️ ᏰᎯᏣᏦ", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )

