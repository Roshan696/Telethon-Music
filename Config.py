import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN",6047327945 )
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOGgBu1RC9ibemuq3yo7RPhmxt5g7KnhE08dq_ExBiCJlUfrnSYEgRFy4vfHwdNV0nszn3S-UdI6v0jmi8xIArvy5--XiCK78pQqpXkFCxtDGLgQ84f4N-PHv4Qb0v1_6WQ2e9wSJaajTFatKWBnY8JYGBM71DKeotnhFSGz78Wa2ZdYW-2HrHiE8FkcHkQz86BTOaczV5NbPrFCtRNL2wG1mHuDs8eiWPoUZ03PetdMaOe_SmLNfo4DUTSX1YrFhUPZo5k68zPH2ZToLwYTITNXOZ18UDpAvuBzO3t2WvcTSVpSQZvJfdAlTM_4KG_4IqB0u29xoJff6x699zy33bOYKQy4=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
