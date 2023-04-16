from DarkWeb import bot, CMD_HELP, ALIVE_NAME
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from Dark.utils import admin_cmd, sudo_cmd, edit_or_reply
from DarkWeb.cmdhelp import CmdHelp
import html
from telethon import events
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.events import ChatAction

Dark = str(ALIVE_NAME) if ALIVE_NAME else "Dark User"
papa = borg.uid



async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await edit_or_reply(event, "**Som3thing W3nt Wr0ng**\n`Can you please provide me a user id`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await edit_or_reply(event, "**Som3thing W3nt Wr0ng**\n", str(err))           
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await edit_or_reply(event, str(err))
        return None
    return user_obj

@dark.on(admin_cmd(pattern="gban ?(.*)"))
@dark.on(sudo_cmd(pattern="gban ?(.*)", allow_sudo=True))
async def gban(userbot):
    if userbot.fwd_from:
        return
    ids = userbot
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        DarkWeb = await edit_or_reply(ids, "Trying to gban this retard!")
    else:
        DarkWeb = await edit_or_reply(ids, "`JANAB ABB APP KII KALLI GAND FAT JAYAGE🖕🖕🤣`")
    hum = await userbot.client.get_me()
    await DarkWeb.edit(f"`🔥BETA BAAP SAAA PANAGA NAHI ABB DEKHO KYA HOO GAAA TERA. ABBB TERI KALLI GAND KO FAR DUU GA`")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await DarkWeb.edit(f"**Something W3NT Wrong 🤔**")
    if user:
        if user.id == 1418571871:
            return await DarkWeb.edit(
                f"`SUNO TERI KALLI GAND FAR DUU TU  APNA BAAP KOO GMUTE KARA GAA RANDI SALA OKAD BANA PHALA`"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await DarkWeb.edit(f"Gbaning This retard🚶\n\nTotal Chats :- `{a}`")
            except:
                b += 1
    else:
        await DarkWeb.edit(f"`Either reply to a user or gib me user id/name`")
    try:
        if gmute(user.id) is False:
            return await DarkWeb.edit(f"**Error! User already gbanned.**")
    except:
        pass
    return await DarkWeb.edit(
        f"[{user.first_name}](tg://user?id={user.id}) Beta BAAP SA PANGA NAHI [{Dark}](tg://user?id={papa}) TU BETA HA MERA BETA HE RAH.\n\n**Gban Successful 🔥\nAffected Chats😏 : {a} **"
    )

@dark.on(admin_cmd(pattern="ungban ?(.*)"))
@dark.on(sudo_cmd(pattern="ungban ?(.*)", allow_sudo=True))
async def gunban(userbot):
    if userbot.fwd_from:
        return
    ids = userbot
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        DarkWeb = await edit_or_reply(ids, "`Trying to ungban this kid...`")
    else:
        DarkWeb = await edit_or_reply(ids, "`Ungban in progress...`")
    hum = await userbot.client.get_me()
    await DarkWeb.edit(f"`RUKO JARA SABAR KARO KAR RAHA HU...`")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await DarkWeb.edit("**Som3ting W3nt Wr0ng**")
    if user:
        if user.id == 1418571871:
            return await DarkWeb.edit("**SUNO TERI KALLI GAND FAR DUU TU  APNA BAAP KOO GMUTE KARA GAA RANDI SALA OKAD BANA PHALA**")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await DarkWeb.edit(f"SALA RUK JAA KAR RAHA HUU NAHI JADA JALDI HAA TOO KHUD KAA BOT BANA LO JAYO.\nChats:- `{a}`")
            except:
                b += 1
    else:
        await DarkWeb.edit("**Reply to a user**")
    try:
        if ungmute(user.id) is False:
            return await DarkWeb.edit("**Error! User already ungbanned.**")
    except:
        pass
    return await DarkWeb.edit(
        f"**[{user.first_name}](tg://user?id={user.id}) AUR BETA GAND HO GAYE CHOTI YA ABHI VV BADA HA.**\n\nUngban Successful 🔥\nChats :- `{a}`"
    )




@dark.on(ChatAction)
async def handler(R3b3l0p): 
   if R3b3l0p.user_joined or R3b3l0p.user_added:      
       try:       	
         from DarkWeb.sql_helper.gmute_sql import is_gmuted
         guser = await R3b3l0p.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await R3b3l0p.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(R3b3l0p.chat_id, guser.id, view_messages=False)                              
                    await R3b3l0p.reply(
                     f"⚠️⚠️**Warning**⚠️⚠️\n\n`Gbanned User Joined the chat!!`\n"                      
                     f"**⚜️ Victim Id ⚜️**:\n[{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**🔥 Action 🔥**  :\n`Banned this piece of shit....` **AGAIN!**")                                                
                 except:       
                    R3b3l0p.reply("`Sheit!! No permission to ban users.\n@admins ban this retard.\nGlobally Banned User And A Potential Spammer`\n**Make your group a safe place by cleaning this shit**")                   
                    return
                  
                  
CmdHelp("gban_gmute").add_command(
  'gban', '<reply> / <userid> / <username>', 'Gbans the targeted user and adds to gban watch list'
).add_command(
  'ungban', '<reply> / <userid> / <username>', 'Unbans the targeted user and removes them from gban watch list. Grants another Chance'
).add_command(
  'gmute', '<reply>/ <userid>/ <username>', 'Gmutes the targeted user. Works only if you have delete msg permission. (Works on admins too)'
).add_command(
  'ungmute', '<reply>/ <userid>/ <username>', 'Ungmutes the user. Now targeted user is free'
).add()
