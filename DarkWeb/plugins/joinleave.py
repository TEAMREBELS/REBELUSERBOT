#cradit @Shinchan7222

import os
from Dark.utils import admin_cmd

from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import (
    GetAdminedPublicChannelsRequest,
    LeaveChannelRequest,
)
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User

from . import *


@dark.on(admin_cmd(pattern="join (.*)"))
@dark.on(sudo_cmd(pattern="join (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bc = event.pattern_match.group(1)
    event = await edit_or_reply(event, "Trying Joining")
    try:
        await event.client(functions.channels.JoinChannelRequest(channel=bc))
        await event.edit("Succesfully Joined")
    except Exception as e:
        await event.edit(str(e))
        
@dark.on(admin_cmd(pattern="leave (.*)"))
@dark.on(sudo_cmd(pattern="leave (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bc = event.pattern_match.group(1)
    event = await edit_or_reply(event, "leaving")
    try:
        await event.client(functions.channels.LeaveChannelRequest(channel=bc))
        await event.edit("Succesfully left")
    except Exception as e:
        await event.edit(str(e))