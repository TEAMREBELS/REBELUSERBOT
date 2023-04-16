import os
import sys
import time

from telethon import TelegramClient
from telethon.sessions import StringSession

from DarkWeb.smex.DARK_Config import Config
from DarkWeb.helpers import functions as simpdef
from var import Var

StartTime = time.time()
darkversion = "1.0"
Darkversion = "1.0"
botversion = "1.0"

os.system("pip install --upgrade pip")

if Var.STRING_SESSION:
    session_name = str(Var.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)


CMD_LIST = {}
# for later purposes
CMD_HELP = {}
CMD_HELP_BOT = {}
BRAIN_CHECKER = []
INT_PLUG = ""
LOAD_PLUG = {}
LOAD_ASSISTANT = {}

# PaperPlaneExtended Support Vars
ENV = os.environ.get("ENV", False)

Dark_ID = ["1418571871"]

""" PPE initialization. """

import asyncio
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger

import pylast
from pySmartDL import SmartDL
from requests import get

# Bot Logs setup:
if bool(ENV):
    if CONSOLE_LOGGER_VERBOSE := sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False")):
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
        )
    LOGS = getLogger(__name__)

try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except:
    HEROKU_APP = None

    if CONFIG_CHECK := os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None
    ):
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)

    BOTLOG_CHATID = os.environ.get("DARKWEB_ID", None)
    try:
        BOTLOG_CHATID = int(DARKWEB_ID)
    except:
        pass


    HNDLR = os.environ.get("HNDLR", r".")
    BOTLOG = os.environ.get("BOTLOG", "False")
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
    DARKWEB_ID = os.environ.get("DARKWEB_ID", None)
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
    DB_URI = os.environ.get("DATABASE_URL", None)
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    REDIRECTCHANNEL = os.environ.get("REDIRECTCHANNEL", None)
    PING_PIC = os.environ.get("PING_PIC", None)
    ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
    SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
    COUNTRY = str(os.environ.get("COUNTRY", "India"))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    PM_MASSAGE = os.environ.get("PM_MASSAGE", None)
    CUSTOM_AFK = os.environ.get("CUSTOM_AFK", None)
    UPSTREAM_REPO_URL = os.environ.get(
        "UPSTREAM_REPO_URL", "https://github.com/TEAMREBELS/REBELBOTSS.git"
    )

 
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    BIO_MSG = os.environ.get("BIO_MSG", None)

    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
    if LASTFM_USERNAME != "None":
        lastfm = pylast.LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    else:
        lastfm = None

    # Google Drive Module
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./downloads")
else:
  
    PLACEHOLDER = None

if not os.path.exists("bin"):
    os.mkdir("bin")

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
SUDO_LIST = {}


from DarkWeb.cmdhelp import CmdHelp
from DarkWeb.helpers import *
from DarkWeb.helpers import functions as REBELdef
