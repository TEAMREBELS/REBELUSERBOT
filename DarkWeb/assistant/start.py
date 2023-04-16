# DARK WEB 

import asyncio
import io
import os
import re
from datetime import datetime

import heroku3
from telegraph import Telegraph, upload_file
from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest

from DarkWeb import bot
from DarkWeb.smex.DARK_Config import Config
from DarkWeb.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from DarkWeb.sql_helper.botusers_sql import add_me_in_db, his_userid
from DarkWeb.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)
from var import Var

Dark_ID = "config.DARKWEB_ID"
BOT_PIC = Config.BOT_PIC or "https://telegra.ph/file/2ea23de03e268b1d026c2.jpg"
Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
path = Config.TMP_DOWNLOAD_DIRECTORY
if not os.path.isdir(path):
    os.makedirs(path)
telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    starkbot = await tgbot.get_me()
    bot_id = starkbot.first_name
    bot_username = starkbot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    vent = event.chat_id
    starttext = f"𝙷𝙴𝙻𝙻𝙾, {firstname} ! 𝙽𝙸𝙲𝙴 𝚃𝙾 𝙼𝙴𝙴𝚃 𝚈𝙾𝚄, 𝚆𝙴𝙻𝙻 𝙸 𝙰𝙼 {bot_id}, 𝙰𝙽 𝙿𝙾𝚆𝙴𝚁𝙵𝚄𝙻𝙻 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙱𝙾𝚃.\n\nMy [➤ ᗰᗩՏTᗴᖇ](tg://user?id={bot.uid}) \n\n 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚃𝙰𝙻𝙺 | 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃. \n\n 𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙲𝙰𝙽 𝙳𝙴𝙿𝙻𝙾𝚈 𝙵𝚁𝙾𝙼 𝙱𝚄𝚃𝚃𝙾𝙽 𝙱𝙴𝙻𝙾𝙴.\n\n𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 [『𝐃𝐀𝐑𝐊𝐖𝐄𝐁』](https://t.me/DARK_WEB_UB)"
    if event.sender_id == bot.uid:
        await tgbot.send_file(
            event.chat_id,
            BOT_PIC,
            message=f"𝙷𝙸 𝙼𝙰𝚂𝚃𝙴𝚁, 𝙸𝚃𝚂 𝙼𝙴 {bot_id}, 𝚈𝙾𝚄𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃! \n\n 𝚆𝙷𝙰𝚃 𝚈𝙾𝚄 𝚆𝙰𝙽𝙽𝙰 𝙳𝙾 𝚃𝙾𝙳𝙰𝚈 ?",
            buttons=[
                [
                    custom.Button.inline("📊 sᴛᴀᴛs", data="users"),
                    custom.Button.inline("ᴀssɪsᴛᴀɴᴛ ᴄᴏᴍᴍᴀɴᴅ", data="gibcmd"),
                ],
                [
                    custom.Button.inline("⚙️ sᴇᴛᴛɪɴɢ️", data="setting"),
                    custom.Button.inline("ʙʀᴏᴀᴅᴄᴀsᴛ", data="Darkbrod"),
                ],
                [
                    Button.url(
                        "ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await tgbot.send_file(
            event.chat_id,
            BOT_PIC,
            message=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴀʀᴋᴡᴇʙ", data="deploy")],
                [Button.url("Sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", "https://t.me/DARK_WEB_BOT_SUPPORT")],
            ],
        )


# Data's


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"setting"))
)  # pylint: disable=oof
async def setting(event):
    await event.edit(
        "Browse through the available options:",
        buttons=[
            [
                custom.Button.inline("ᴀʟɪᴠᴇ", data="alivessrr"),
                custom.Button.inline("ɴʟɪɴᴇ", data="inlineaa"),
            ],
            [
                custom.Button.inline("ᴘᴍ sᴇᴛᴛɪɴɢ", data="pmsetting"),
                custom.Button.inline("sᴜᴅᴏ sᴇᴛᴛɪɴɢ", data="sudosetting"),
            ],
            [custom.Button.inline("ʙᴀᴄᴋ", data="home")],
        ],
    )


# -------------------------- bottom --------------- #


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"alivessrr"))
)  # pylint: disable=oof
async def alivessrr(event):
    await event.edit(
        "Browse through the available options:",
        buttons=[
            [
                custom.Button.inline("Aʟɪᴠᴇ ɴᴀᴍᴇ", data="alv_name"),
                custom.Button.inline("Aʟɪᴠᴇ Tᴇxᴛ", data="alv_txt"),
            ],
            [
                custom.Button.inline("Aʟɪᴠᴇ ᴍᴇᴅɪᴀ", data="alv_pic"),
                custom.Button.inline("ᴘɪɴɢ Mᴇᴅɪᴀ", data="ping_pic"),
            ],
            [custom.Button.inline("ʙᴀᴄᴋ", data="setting")],
        ],
    )


# ------------------- button2 ------------------#


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"inlineaa"))
)  # pylint: disable=oof
async def inlineaa(event):
    await event.edit(
        "Browse through the available options:",
        buttons=[
            [
                custom.Button.inline("Iɴʟɪɴᴇ Pɪᴄ", data="inline_pic"),
                custom.Button.inline("Eᴍᴏᴊɪ ɪɴ Hᴇʟᴘ", data="inl_emj"),
            ],
            [custom.Button.inline("ʙᴀᴄᴋ", data="setting")],
        ],
    )


# ---------------------- button 3 ------------- #


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"pmsetting"))
)  # pylint: disable=oof
async def pmsetting(event):
    await event.edit(
        "Browse through the available options:",
        buttons=[
            [
                custom.Button.inline("ᴘᴍ ᴛᴇxᴛ", data="pm_txt"),
                custom.Button.inline("ᴘᴍ ᴘɪᴄ", data="pm_pic"),
            ],
            [custom.Button.inline("ᴀᴘᴘʀᴏᴠᴇᴅ", data="pm_data")],
            [custom.Button.inline("ʙᴀᴄᴋ", data="setting")],
        ],
    )


# --------------------- sudo ----------------- #


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"sudosetting"))
)  # pylint: disable=oof
async def sudosetting(event):
    await event.edit(
        "Browse through the available options:",
        buttons=[
            [
                custom.Button.inline("ᴀᴅᴅ sᴜᴅᴏ ᴜsᴇʀs", data="sud_users"),
                custom.Button.inline("sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅ", data="sud_cmmd"),
            ],
            [custom.Button.inline("ʙᴀᴄᴋ", data="setting")],
        ],
    )


# ------------------------ back ----------------#


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"home"))
)  # pylint: disable=oof
async def home(event):
    await event.edit(
        "𝙷𝙸 𝙼𝙰𝚂𝚃𝙴𝚁, 𝙸𝚃𝚂 𝙼𝙴 {bot_id}, 𝚈𝙾𝚄𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃! \n\n 𝚆𝙷𝙰𝚃 𝚈𝙾𝚄 𝚆𝙰𝙽𝙽𝙰 𝙳𝙾 𝚃𝙾𝙳𝙰𝚈 ?",
        buttons=[
            [
                custom.Button.inline("📊 sᴛᴀᴛs", data="users"),
                custom.Button.inline("ᴀssɪsᴛᴀɴᴛ ᴄᴏᴍᴍᴀɴᴅ", data="gibcmd"),
            ],
            [
                custom.Button.inline("⚙️ sᴇᴛᴛɪɴɢ️", data="setting"),
                custom.Button.inline("ʙʀᴏᴀᴅᴄᴀsᴛ", data="Darkbrod"),
            ],
            [
                Button.url("ᴅᴀʀᴋᴡᴇʙ ᴜᴘᴅᴀᴛᴇ", "t.me/DARK_WEB_UB"),
                Button.url("ᴅᴀʀᴋᴡᴇʙ sᴜᴘᴘᴏʀᴛ", "t.me/DARK_WEB_BOT_SUPPORT"),
            ],
        ],
    )


# ------------------ deploy ---------------- #


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"deploy"))
)  # pylint: disable=oof
async def deploy(event):
    await event.edit(
        "Browse through the available options:",
        buttons=[
            [
                (
                    custom.Button.url(
                        "ʀᴇᴘᴏsɪᴛᴏʀʏ", url="https://github.com/Dark75/DarkSBOTS"
                    )
                ),
                (custom.Button.url("ᴜᴘᴅᴀᴛᴇ", url="t.me/DARK_WEB_UB")),
            ],
            [custom.Button.url("sᴜᴘᴘᴏʀᴛ", url="t.me/DARK_WEB_BOT_SUPPORT")],
        ],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "List Of Total Users In Bot. \n\n"
        for starked in total_users:
            users_list += f"==> {int(starked.chat_id)} \n"
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await tgbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="Total Users In Your Bot.",
                allow_cache=False,
            )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def gibcmd(event):
    await event.delete()
    chumty = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n➤ /purge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \n➤ /del - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"
    await tgbot.send_message(event.chat_id, chumty)


# Bot Permit.
@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if is_he_added(event.sender_id):
        return
    if event.raw_text.startswith("/"):
        pass
    elif event.sender_id == bot.uid:
        return
    else:
        await event.get_sender()
        event.chat_id
        sed = await event.forward_to(bot.uid)
        # Add User To Database ,Later For Broadcast Purpose
        # (C) @SpecHide
        add_me_in_db(sed.id, event.sender_id, event.id)


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    msg = await event.get_reply_message()
    user_id, reply_message_id = his_userid(msg.id)
    if event.sender_id == bot.uid and not event.text.startswith("/"):
        await tgbot.send_message(user_id, event.message)


# broadcast
@tgbot.on(
    events.NewMessage(
        pattern="^/broadcast ?(.*)", func=lambda e: e.sender_id == bot.uid
    )
)
async def sedlyfsir(event):
    msgtobroadcast = event.pattern_match.group(1)
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for starkcast in userstobc:
        try:
            sent_count += 1
            await tgbot.send_message(int(starkcast.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except Exception as e:
            try:
                logger.info(f"Error : {error_count}\nError : {e} \nUsers : {chat_id}")
            except:
                pass
    await tgbot.send_message(
        event.chat_id,
        f"Broadcast Done in {sent_count} Group/Users and I got {error_count} Error and Total Number Was {len(userstobc)}",
    )


@tgbot.on(
    events.NewMessage(pattern="^/stats ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    starkisnoob = get_all_users()
    await event.reply(
        f"**Stats Of Your Bot** \nTotal Users In Bot => {len(starkisnoob)}"
    )


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"Darkbrod"))
)  # pylint: disable=oof
async def Darkbrod(event):
    if event.sender_id != bot.uid:
        await event.answer("You can't use this bot")
        return
    await tgbot.send_message(
        event.chat_id, "Send the message you want to broadcast!\nSend /cancel to stop."
    )
    async with event.client.conversation(bot.uid) as conv:
        response = conv.wait_event(events.NewMessage(chats=bot.uid))
        response = await response
        themssg = response.message.message
    if themssg is None:
        await tgbot.send_message(event.chat_id, "An error has occured...")
    if themssg == "/cancel":
        await tgbot.send_message(event.chat_id, "Broadcast cancelled!")
        return
    userstobc = get_all_users()
    err = 0
    success = 0
    lmao = await tgbot.send_message(
        event.chat_id, f"Starting broadcast to {userstobc} users."
    )

    start = datetime.now()
    for ok in userstobc:
        try:
            await tgbot.send_message(int(ok.chat_id), themssg)
            success += 1
            await asyncio.sleep(0.1)
        except Exception as e:
            err += 1
            try:
                await tgbot.send_message(
                    Var.DarkBODARKWEB_ID,
                    f"**Error**\n{str(e)}\nFailed for user: {chat_id}",
                )
            except BaseException:
                pass
    end = datetime.now()
    ms = (end - start).seconds
    done_mssg = """
Broadcast completed!\n
Sent to `{}` users in `{}` seconds.\n
Failed for `{}` users.\n
""".format(
        success, ms, err, userstobc
    )
    await lmao.edit(done_mssg)
    try:
        await tgbot.send_message(
            Var.Dark_ID,
            f"#Broadcast\nCompleted sending a broadcast to {success} users.",
        )
    except BaseException:
        await tgbot.send_message(
            event.chat_id, "Please add me to your Private log group for proper use."
        )


@tgbot.on(events.NewMessage(pattern="^/help", func=lambda e: e.sender_id == bot.uid))
async def starkislub(event):
    grabonx = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot"
    await event.reply(grabonx)


@tgbot.on(
    events.NewMessage(pattern="^/block ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        await event.reply("Already Blacklisted")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("Blacklisted This Dumb Person")
        await tgbot.send_message(
            user_id, "You Have Been Blacklisted And You Can't Message My Master Now."
        )


@tgbot.on(
    events.NewMessage(pattern="^/unblock ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("Not Even. Blacklisted 🤦🚶")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("DisBlacklisted This Dumb Person")
        await tgbot.send_message(
            user_id, "Congo! You Have Been Unblacklisted By My Master."
        )


# -------------------------alive_pic---------------------- #


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"alv_pic"))
)  # pylint: disable=C0321
async def alv_pic(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, "Send me a pic so as to set it as your alive pic."
        )
        async with event.client.conversation(bot.uid) as conv:
            await conv.send_message("Send /cancel to cancel the operation!")
            response = await conv.get_response()
            try:
                themssg = response.message.message
                if themssg == "/cancel":
                    await conv.send_message("Operation cancelled!!")
                    return
            except:
                pass
            media = await event.client.download_media(response, "Alive_Pic")
            try:
                x = upload_file(media)
                url = f"https://telegra.ph/{x[0]}"
                os.remove(media)
            except BaseException:
                return await conv.send_message("Error!")
        Dark1 = "ALIVE_PIC"
        if Var.HEROKU_APP_NAME is not None:
            app = Heroku.app(Var.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
            return
        xx = await tgbot.send_message(
            event.chat_id, "Changing your Alive Pic, please wait for a minute"
        )
        heroku_var = app.config()
        heroku_var[Dark1] = f"{url}"
        mssg = f"Successfully changed your alive pic. New alive pic {url} \nafter 1 min do ping|alive check your bot working or not"
        await xx.edit(mssg)
    else:
        await event.answer("You can't use this bot.", alert=True)


# -------------------- alive text ------------------- #


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alv_txt")))
async def alv_txt(event):
    if event.sender_id == bot.uid:
        await event.delete()
        Dark2 = "ALIVE_MSG"
        if Var.HEROKU_APP_NAME is not None:
            app = Heroku.app(Var.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
            return
        async with event.client.conversation(bot.uid) as conv:
            await conv.send_message(
                "Send the text which you want as your alive text.\nUse /cancel to cancel the operation."
            )
            response = conv.wait_event(events.NewMessage(chats=bot.uid))
            response = await response
            themssg = response.message.message
            if themssg is None:
                await conv.send_message("Error!")
                return
            if themssg == "/cancel":
                return await conv.send_message("Cancelled!!")
            heroku_var = app.config()
            xx = await tgbot.send_message(
                event.chat_id, "Changing your Alive Message, please wait for a minute"
            )
            heroku_var[Dark2] = f"{themssg}"
            mssg = f"successful Changed your alive text \n after 1 min do ping|alive check your bot working or not"
            await xx.edit(mssg)
    else:
        await event.answer("You can't use this bot.", alert=True)


# ------------------------ pm massage ------------------------ #


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pm_txt")))
async def pm_txt(event):
    if event.sender_id == bot.uid:
        await event.delete()
        Dark3 = "PM_MASSAGE"
        if Var.HEROKU_APP_NAME is not None:
            app = Heroku.app(Var.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
            return
        async with event.client.conversation(bot.uid) as conv:
            await conv.send_message(
                "Send the text which you want as your PMPermit Message!\nUse /cancel to cancel the operation."
            )
            response = conv.wait_event(events.NewMessage(chats=bot.uid))
            response = await response
            themssg = response.message.message
            if themssg is None:
                await conv.send_message("Error!")
                return
            if themssg == "/cancel":
                await conv.send_message("Cancelled!!")
            heroku_var = app.config()
            heroku_var[Dark3] = f"{themssg}"
            xx = await tgbot.send_message(
                event.chat_id,
                "successful Changed your PMPermit Message from\nafter 1 min do ping|alive check your bot working or not",
            )
    else:
        await event.answer("You can't use this bot.", alert=True)


# ------------------------- pm pic ------------------#


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"pm_pic"))
)  # pylint: disable=C0321
async def pm_pic(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, "Send me a pic so as to set it as your PMPermit pic."
        )
        async with event.client.conversation(bot.uid) as conv:
            await conv.send_message("Send /cancel to cancel the operation!")
            response = await conv.get_response()
            try:
                themssg = response.message.message
                if themssg == "/cancel":
                    await conv.send_message("Operation cancelled!!")
                    return
            except:
                pass
            media = await event.client.download_media(response, "PM_PIC")
            try:
                x = upload_file(media)
                url = f"https://telegra.ph/{x[0]}"
                os.remove(media)
            except BaseException:
                return await conv.send_message("Error!")
        Dark4 = "PM_PIC"
        if Var.HEROKU_APP_NAME is not None:
            app = Heroku.app(Var.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
            return
        xx = await tgbot.send_message(
            event.chat_id, "Changing your PMPermit Pic, please wait for a minute"
        )
        heroku_var = app.config()
        heroku_var[Dark4] = f"{url}"
        mssg = f"Successfully changed your PMPermit pic. Please wait for a minute.\n"
        await xx.edit(mssg)
    else:
        await event.answer("You can't use this bot.", alert=True)


# --------------------- inline emoji -------------- #


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"inl_emj")))
async def inl_emj(event):
    if event.sender_id == bot.uid:
        await event.delete()
        Dark5 = "EMOJI_IN_HELP"
        if Var.HEROKU_APP_NAME is not None:
            app = Heroku.app(Var.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
            return
        async with event.client.conversation(bot.uid) as conv:
            await conv.send_message(
                "Send the emoji  which you want as your help emoji.\nUse /cancel to cancel the operation."
            )
            response = conv.wait_event(events.NewMessage(chats=bot.uid))
            response = await response
            themssg = response.message.message
            if themssg is None:
                await conv.send_message("Error!")
                return
            if themssg == "/cancel":
                return await conv.send_message("Cancelled!!")
            heroku_var = app.config()
            heroku_var[Dark5] = f"{themssg}"
            xx = await tgbot.send_message(
                event.chat_id,
                "successful Changed your help emoji \nafter 1 min do ping|alive check your bot working or not",
            )
    else:
        await event.answer("You can't use this bot.", alert=True)


# ------------------------- sudo command ------------------ #


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sud_cmmd")))
async def sud_users(event):
    if event.sender_id == bot.uid:
        await event.delete()
        Dark7 = "SUDO_HNDLR"
        if Var.HEROKU_APP_NAME is not None:
            app = Heroku.app(Var.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
            return
        async with event.client.conversation(bot.uid) as conv:
            await conv.send_message(
                "Send the symbol  which you want as your sudo users command.\nUse /cancel to cancel the operation."
            )
            response = conv.wait_event(events.NewMessage(chats=bot.uid))
            response = await response
            themssg = response.message.message
            if themssg is None:
                await conv.send_message("Error!")
                return
            if themssg == "/cancel":
                return await conv.send_message("Cancelled!!")
            heroku_var = app.config()
            heroku_var[Dark7] = f"{themssg}"
            xx = await tgbot.send_message(
                event.chat_id,
                "successful change your sudo users command \nafter  min do ping|alive check your bot working or not",
            )
    else:
        await event.answer("You can't use this bot.", alert=True)


# ------------------------------ sudo users------------------- #


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sud_users")))
async def sud_users(event):
    if event.sender_id == bot.uid:
        await event.delete()
        Dark8 = "SUDO_USERS"
        if Var.HEROKU_APP_NAME is not None:
            app = Heroku.app(Var.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
            return
        async with event.client.conversation(bot.uid) as conv:
            await conv.send_message(
                "Send the user id  which you want to added you sudo.\nUse /cancel to cancel the operation."
            )
            response = conv.wait_event(events.NewMessage(chats=bot.uid))
            response = await response
            themssg = response.message.message
            if themssg is None:
                await conv.send_message("Error!")
                return
            if themssg == "/cancel":
                return await conv.send_message("Cancelled!!")
            heroku_var = app.config()
            heroku_var[Dark8] = f"{themssg}"
            xx = await tgbot.send_message(
                event.chat_id,
                "successfull add your sudo users \n new user id`{themssg}`\nafter 5 min do ping|alive check your bot working or not",
            )
    else:
        await event.answer("You can't use this bot.", alert=True)


# ------------------------------ pm data ------------------- #


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pm_data")))
async def pm_data(event):
    if event.sender_id != bot.uid:
        return
    await event.delete()
    Dark9 = "PM_DATA"
    if Var.HEROKU_APP_NAME is not None:
        app = Heroku.app(Var.HEROKU_APP_NAME)
    else:
        mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
        return
    async with event.client.conversation(bot.uid) as conv:
        await conv.send_message(
            "Send `ENABLE` OR `DESABLE`  set you pm data .\nUse /cancel to cancel the operation."
        )
        response = conv.wait_event(events.NewMessage(chats=bot.uid))
        response = await response
        themssg = response.message.message
        if themssg is None:
            await conv.send_message("Error!")
            return
        if themssg == "/cancel":
            return await conv.send_message("Cancelled!!")
        heroku_var = app.config()
        heroku_var[Dark9] = f"{themssg}"
        xx = await tgbot.send_message(
            event.chat_id,
            "successfull set you pm data\nafter  min do ping|alive check your bot working or not",
        )
    # else:
    #    await event.answer("You can't use this bot.", alert=True)


# ------------------------- alive name ----------------------- #


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alv_name")))
async def alv_name(event):
    if event.sender_id != bot.uid:
        return
    await event.delete()
    Dark10 = "ALIVE_NAME"
    if Var.HEROKU_APP_NAME is not None:
        app = Heroku.app(Var.HEROKU_APP_NAME)
    else:
        mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
        return
    async with event.client.conversation(bot.uid) as conv:
        await conv.send_message(
            "Send the name  which you want to added you alive name .\nUse /cancel to cancel the operation."
        )
        response = conv.wait_event(events.NewMessage(chats=bot.uid))
        response = await response
        themssg = response.message.message
        if themssg is None:
            await conv.send_message("Error!")
            return
        if themssg == "/cancel":
            return await conv.send_message("Cancelled!!")
        heroku_var = app.config()
        heroku_var[Dark10] = f"{themssg}"
        xx = await tgbot.send_message(
            event.chat_id,
            "successfull set you alive name\nafter 1 min do ping|alive check your bot working or not",
        )
    # else:
    #    await event.answer("You can't use this bot.", alert=True)


# -_--------------------- inline pic ------------------- #


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"inline_pic"))
)  # pylint: disable=C0321
async def inline_pic(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, "Send me a pic so as to set it as your inline pic."
        )
        async with event.client.conversation(bot.uid) as conv:
            await conv.send_message("Send /cancel to cancel the operation!")
            response = await conv.get_response()
            try:
                themssg = response.message.message
                if themssg == "/cancel":
                    await conv.send_message("Operation cancelled!!")
                    return
            except:
                pass
            media = await event.client.download_media(response, "HELP_PIC")
            try:
                x = upload_file(media)
                url = f"https://telegra.ph/{x[0]}"
                os.remove(media)
            except BaseException:
                return await conv.send_message("Error!")
        Dark11 = "HELP_PIC"
        if Var.HEROKU_APP_NAME is not None:
            app = Heroku.app(Var.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
            return
        xx = await tgbot.send_message(
            event.chat_id,
            "successful Changing your inline Pic, please wait for a minute",
        )
        heroku_var = app.config()
        heroku_var[Dark11] = f"{url}"
        mssg = f"Successfully changed your inline pic. Please wait for a minute.\n"
        await xx.edit(mssg)
    else:
        await event.answer("You can't use this bot.", alert=True)


# -------------------------------------- ping pic ------------------------------ #


@tgbot.on(
    events.callbackquery.CallbackQuery(data=re.compile(b"ping_pic"))
)  # pylint: disable=C0321
async def ping_pic(event):
    if event.sender_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id, "Send me a pic so as to set it as your inline pic."
        )
        async with event.client.conversation(bot.uid) as conv:
            await conv.send_message("Send /cancel to cancel the operation!")
            response = await conv.get_response()
            try:
                themssg = response.message.message
                if themssg == "/cancel":
                    await conv.send_message("Operation cancelled!!")
                    return
            except:
                pass
            media = await event.client.download_media(response, "PING_PIC")
            try:
                x = upload_file(media)
                url = f"https://telegra.ph/{x[0]}"
                os.remove(media)
            except BaseException:
                return await conv.send_message("Error!")
        Dark12 = "PING_PIC"
        if Var.HEROKU_APP_NAME is not None:
            app = Heroku.app(Var.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
            return
        xx = await tgbot.send_message(
            event.chat_id, "successful Changing your ping Pic, please wait for a minute"
        )
        heroku_var = app.config()
        heroku_var[Dark12] = f"{url}"
        mssg = f"Successfully changed your ping pic. Please wait for a minute.\n"
        await xx.edit(mssg)
    else:
        await event.answer("You can't use this bot.", alert=True)
