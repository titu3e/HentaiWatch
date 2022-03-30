import os

#Config - bot.py
API_ID = os.getenv('8626831') or "8626831"
API_HASH = os.getenv('6c9636ea928b50402b7d7c69a6eba45c') or "db23330a6edf4a517ee186b35cedec71"
BOT_TOKEN = os.getenv('2077017001:AAHE9GF1OK2u3jRR9Ns5yZKycsQCR8HW0eY') or "5188200237:AAEZbGn3vCuf0B8PvoAZEImt68niQuodRqA"
PLUGINS = dict(root="plugins")

#Config - plugins/utils.py -> TelegraphUP()
SHORT_NAME = "HW"
AUTHOR_NAME = "Shouko komi"
AUTHOR_URL = "https://t.me/HentaiWatchBot"

#Cofig - plugins/sudoers.py
SUDO_LIST = [1593338093]
MAX_MESSAGE_LENGTH = 4096

# -> sudo_command_telegraph()
INIT_MESSAGE_PHOTO = "https://telegra.ph/file/5efdb99994b1528f77ccf.png"

#Config - plugins/nhentai.py
LOGCHAT = -1001598625668
NHCHANNEL = -1001598625668
LOG_MESSAGE = "{} has been added on {}"

#Config - plugins/inline.py
INLINE_MENU_PHOTO_ICON_1 = "https://te.legra.ph/file/de239bf119e5e52fe2f07.jpg"
