import os

from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os

    class Config(object):
        LOGGER = True
        LOCATION = os.environ.get("LOCATION", None)
        SUDO_HNDLR = os.environ.get("SUDO_HNDLR", r"\.")
        OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", r"\.")
        TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "DARKWEB")
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
        BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
        BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
        BOTLOG = os.environ.get("BOTLOG", "False")
        DUAL_LOG = os.environ.get("DUAL_LOG", None)
        MAX_MESSAGE_SIZE_LIMIT = 4095
        UB_BLACK_LIST_CHAT = {
            int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
        }
        MAX_ANTI_FLOOD_MESSAGES = 10
        ANTI_FLOOD_WARN_MODE = ChatBannedRights(until_date=None, view_messages=None, send_messages=True)
        CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
        G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", True))
        MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        if DARKWEB_ID := os.environ.get("DARKWEB_ID", None):
            DARKWEB_ID = int(DARKWEB_ID)
        NC_LOG_P_M_S = os.environ.get("NC_LOG_P_M_S", None)
        DB_URI = os.environ.get("DATABASE_URL", None)
        BUTTONS_IN_HELP = int(os.environ.get("BUTTONS_IN_HELP", 7))
        NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(os.environ.get("NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 3))
        PM_MASSAGE = os.environ.get("PM_MASSAGE","PLEASE DO NOT SPAM MY DM, I WILL REPLY YOU AFTER COME BACK ONLINE!",)
        EMOJI_IN_HELP = os.environ.get("EMOJI_IN_HELP", "💙")
        HNDLR = os.environ.get("HNDLR", None)
        SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
        GROUP_REG_SED_EX_BOT_S = os.environ.get("GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot")
        TEMP_DIR = os.environ.get("TEMP_DIR", None)
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        watermark_path = os.environ.get("watermark_path", None)
        CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
        GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
        ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
        ALIVE_MSG = os.environ.get("ALIVE_MSG", None)
        ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
        HELP_PIC = os.environ.get("HELP_PIC", None)
        PING_PIC = os.environ.get("PING_PIC", None)
        BIO_MSG = os.environ.get("BIO_MSG", None)
        UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/TEAMDARKS/DARKWEB")
        STRING_SESSION = os.environ.get("STRING_SESSION", None)
        BOT_MODE = os.environ.get("BOT_MODE", "ON")
        PM_DATA = os.environ.get("PM_DATA", "ENABLE")
        PM_PIC = os.environ.get("PM_PIC", None)
        BOT_PIC = os.environ.get("BOT_PIC", None)

else:

    class Config(object):
        DB_URI = None
