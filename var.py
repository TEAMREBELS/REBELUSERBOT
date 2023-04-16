import os

class Var(object):
    ENV = bool(os.environ.get("ENV", False))
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "1418571871").split()}
    WHITELIST_USERS = {int(x) for x in os.environ.get("WHITELIST_USERS", "").split()}
    BLACKLIST_USERS = {int(x) for x in os.environ.get("BLACKLIST_USERS", "").split()}
    DEVLOPERS = {int(x) for x in os.environ.get("DEVLOPERS", "").split()}
    OWNER_ID = {int(x) for x in os.environ.get("OWNER_ID", "").split()}
    SUPPORT_USERS = {int(x) for x in os.environ.get("SUPPORT_USERS", "").split()}
    PLUGIN_CHANNEL = int(os.environ.get("DARKWEB_ID", None))
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    if AUTH_TOKEN_DATA != None:
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        with open(f"{TEMP_DOWNLOAD_DIRECTORY}auth_token.txt", "w") as t_file:
            t_file.write(AUTH_TOKEN_DATA)
    DARKWEB_ID = os.environ.get("DARKWEB_ID", None)
    if DARKWEB_ID != None:
        try:
            DARKWEB_ID = int(DARKWEB_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers."
            )

class Development(Var):
    LOGGER = True
