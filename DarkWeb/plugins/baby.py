# PLUGIN MADE BY @REBEL_IS_OP FOR DarkWeb
# KEEP CREDITS ELSE GAY

import random, re
from Dark.utils import admin_cmd
import asyncio
from telethon import events
from DarkWeb.cmdhelp import CmdHelp

@dark.on(admin_cmd(pattern="baby ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("""HEYY BABYπππ HOW ARE  YOU  π AP KO PATA HA MA BASS AP KK LIYA HUU ISS DUNIYA MA ORR AP MERI JAAN HOO ππππ₯°. ORR AP KKK BAAD KOI NAHI HAAA MERA π₯Ίπ₯Ίπ₯Ί. AP JAB NAHI HOO TII HO TABB KOI MERE SA BAAT  NAHI KARTA HAA π₯Ίπ₯Ί. BUT MERE KO ISS SA KOI FIRK NAHI PADTA HAππ. BASS AP MERA SATH HOO YAHI π₯°π₯°. BHUT JADA HAA πβ£οΈ I LOVE YOU MY SWEET HEART TUM MERI JAAN HO ORR MAA THUMARA. LIYA  KUCH VV KAR SAKTA HUUU""")


@dark.on(admin_cmd(pattern="baby1 ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("""SUN TUU MERI ππJAANππ HAA MANA PYAR πΉπΉKIYA HAA KOI MAZAK NAHI. AJJ NIGHT π MAA TUU BHUT YAADππ AAA RAHI THE . TU BASS MERI πππ MERI JAAN HAA BASS MERIπ. I LOVE πYOU BABYππ""")
        
        
        
CmdHelp("baby").add_command(
  "baby", "<tag your gf>", "send your gf and enjoy."
).add_command(
  "baby1", "<tag your gf>", "send your gf and enjoy."
).add()
