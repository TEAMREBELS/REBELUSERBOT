# Copyright (C) Midhun KM
#
# Please Don't Kang Without Credits
# A Plugin For Assistant Bot
# x0x

from datetime import datetime

from telethon import events

from DarkWeb import bot


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += f"{time_list.pop()}, "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@tgbot.on(events.NewMessage(pattern="^/ping", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await tgbot.send_message(
        event.chat_id,
        f"**╔═══╗╔══╗╔═╗─╔╗╔═══╗\n║╔═╗║╚╣─╝║║╚╗║║║╔═╗║\n║╚═╝║─║║─║╔╗╚╝║║║─╚╝\n║╔══╝─║║─║║╚╗║║║║╔═╗\n║║───╔╣─╗║║─║║║║╚╩═║\n╚╝───╚══╝╚╝─╚═╝╚═══╝**\n ➲ `{ms}`",
    )
