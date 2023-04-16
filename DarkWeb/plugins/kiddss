from telethon import functions, types, events
from telethon.tl.functions.messages import DeleteHistoryRequest
from DarkWeb import bot as danish_00
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from Dark.utils import admin_cmd, edit_or_reply, sudo_cmd as admin_cmd
from DarkWeb.cmdhelp import CmdHelp

@dark.on(admin_cmd(pattern="bin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    danish = event.pattern_match.group(1)
    chat = "@VoidxBot"
    await event.edit("Searching ur bin 😅😁...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=5366864997))
              await event.client.send_message(chat, "/bin {}".format(LEGEND))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock  @VoidxBot")
              return
          if respond.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()

@dark.on(admin_cmd(pattern="cc ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@VoidxBot"
    await event.edit("Check your cc ......")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=5366864997))
              await event.client.send_message(chat, "/ch {}".format(LEGEND))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @VoidxBot ")
              return
          if respond.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
              
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
    
@dark.on(admin_cmd(pattern="sk ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/key {}".format(danish))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
  
@dark.on(admin_cmd(pattern="redem ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@VoidxBot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=5366864997))
              await event.client.send_message(chat, "/redeem {}".format(danish))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @VoidxBot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
        

@dark.on(admin_cmd(pattern="gen ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    danish = event.pattern_match.group(1)
    chat = "@VoidxBot"
    await event.edit("gen ur cc 😅😁...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=5366864997))
              await event.client.send_message(chat, "/gen {}".format(LEGEND))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @VoidxBot ")
              return
          if respond.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()

@dark.on(admin_cmd(pattern="scr ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    danish = event.pattern_match.group(1)
    chat = "@VoidxBot"
    await event.edit("Scrap ur cc 😅😁...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=5366864997))
              await event.client.send_message(chat, "/scr {}".format(LEGEND))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @VoidxBot ")
              return
          if respond.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
   

   
CmdHelp("kiddss").add_command(
   'gen', None, '.gen 430360 500'
).add_command(
    'scr', None, '.scr username amount '
).add_command(
    'redem', None, '.redem VOID-XXXX-XXXX-XXXX'
).add_command(
    'bin', None, '.bin 430460'
).add_command(
    'sk', None, '.sk sk_live_xxx'
).add_command(
    'cc', None, '.cc cc|mm|yyyy|cvv'
).add()
