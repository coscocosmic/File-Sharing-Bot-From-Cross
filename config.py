#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN"7115851010:AAEK60i4I6w7iq6dQXI-_SF_e_FrRKE-UaA
")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("24082043"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("eefee55310e47c71549bf63d1195cd90")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("-1002132295486"))

#OWNER ID
OWNER_ID = int(os.environ.get("5817386548"))

#Port
PORT = os.environ.get("8080")

#Database 
DB_URI = os.environ.get("mongodb+srv://cosco:sahilsoni2007@cluster0.oqqb388.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("CoscoCosmic")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("-1002085504544"))

TG_BOT_WORKERS = int(os.environ.get("4"))

#start message
START_MSG = os.environ.get("Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("1047290398").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('True') == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(5817386548)
ADMINS.append(1047290398)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
