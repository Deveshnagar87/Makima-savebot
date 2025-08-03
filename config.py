# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28151444"))
API_HASH = getenv("API_HASH", "85ef94c1c03dd427c4acb85bf66e4f6d")
BOT_TOKEN = getenv("BOT_TOKEN", "8249003232:AAH4k2G18-GY96w41DcpsQ88IfivGwVSho8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7336436880").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://nagardeveshjpr:vDBSHxlkeAfVAWs8@cluster0.slvhm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002752207790")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002626193023"))
