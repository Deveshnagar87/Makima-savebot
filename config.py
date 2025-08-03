# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29841528"))
API_HASH = getenv("API_HASH", "74bf5a13efb31cb167ede30c3d2a824f")
BOT_TOKEN = getenv("BOT_TOKEN", "8249003232:AAH4k2G18-GY96w41DcpsQ88IfivGwVSho8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7364404381").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://nagardeveshjpr:vDBSHxlkeAfVAWs8@cluster0.slvhm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002752207790")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002626193023"))
