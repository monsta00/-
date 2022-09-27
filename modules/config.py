import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "19193443"))
API_HASH = getenv("API_HASH", "4e2f2d90bdc549ebebd1d01ac1e8292b")
BOT_TOKEN = getenv("BOT_TOKEN", "5499998318:AAFS2maq5oF2OEvf62lX6PMVQiPXlyxIywY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "1ApWapzMBu6Vd0p6Oflg31L38GKEOJ40xlIaDqdXIAVlHdzt4pT7OdrKCAWWjbrm8U75B7Xk_KrRuNmgqhDyFzLNo7t2x0vAyl2lWuLELw-mzHwRkxrRkro_Lyzcc2_t4HIunhI-9oT7zPPkjrLqOF4Ng-D1c4pmCGfXJl9poevyylWwDbKCMen_kmGTulxa1C7E7_h8Er8ilBYdRdOZWwMyOzcEa-wd3QMf7kRW5g0jpSLdAyhAkrStjwjwZU-vdnoQ1UK5KvNkpLpM4tlo79yj49U5gnygdDI40vEdhNW4E-1IxKbZ6bIX6YMIreSxfn1dbysEoy3q0mHYAsjuhLgWd6-rKy9Y=")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
