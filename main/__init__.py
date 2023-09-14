#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 15523035
API_HASH = "33a37e968712427c2e7971cb03f341b3"
BOT_TOKEN = "6326888965:AAH95RvB9G9tjK0G-exAR2dCVeJEwcBrRIs"
SESSION = "AQAr3fELR4UZoo_v3GCLc2f-caj8aQhy_8N6ek92tn0DNE3Biek0AkXpe4lxxOMowWpTPnd4JTcpp_aVRmMiDPwTps3cw_vZC7QnG9q3u09Ppp1t66l5kszK-ymrxOnCrb-j4wJH2Y6rhLBL_QCfv9-Lsv2mJ_tkQ5sewJ2trkz-R5rzmBej3qYge-ETLk8qF_OVQaXLWJPODNal2_gH2MhowU2SheI2v5-o1SHLlQq2ykcfx3S9_6-t5Xe-xWaEun4qWmY0ZVAzwsEo4ezc6L33typiT5sMtCr6hwG6fsmBOwzw5x1kw3s9INgSNVZmBQpautlgKEV2_92pq2ky5bFcAAAAAThlsXMA"
FORCESUB = "savecontenttx"
AUTH = 5138169653

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
