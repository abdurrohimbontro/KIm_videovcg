# ===========
# running bot
# ===========
import logging
import time
import sys
import asyncio
import glob
import importlib
from pathlib import Path
from pyrogram import Client, idle
from config import Veez 
from bot.videoplayer import app
from bot.videoplayer import call_py
from helpers.loggings import LOG
 
    
bot = Client(
    ":memory:",
    Veez.API_ID,
    Veez.API_HASH,
    bot_token=Veez.BOT_TOKEN,
    plugins=dict(root="bot"),
)

StartTime = time.time()

loop = asyncio.get_event_loop()

_path = f"bot/*.py"
files = glob.glob(_path)

def load_plugins(plugin_name):
    path = Path(f"bot/{plugin_name}.py")
    name = "bot.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(load)
    sys.modules[f"bot." + plugin_name] = load
    print("Imported => " + plugin_name)

async def start():
    print('\n')
    print('------------------- Initalizing Veez ---------------------')
    if bot:
        await bot.start()
    await app.start()
    await call_py.start()
    print('----------------------- SELESAI ------------------------')
    print('--------------------- MENGIMPOR ---------------------')
    for name in files:
        with open(name) as a:
            path_ = Path(a.name)
            plugin_name = path_.stem
            load_plugins(plugin_name.replace(".py", ""))
    print('----------------------- MEMULAU KIM VIDEO BOT ------------------------')
    print('             masuk sebagai pengguna =>> {}'.format((await app.get_me()).first_name))
    if bot:
        print('             dan bot =>> {}'.format((await bot.get_me()).first_name))
    print('-----------------------------------------------------')
    await idle()
if __name__ == '__main__':
    is_bot = bool(Veez.BOT_TOKEN)
    loop.run_until_complete(start())


# bot.start()
# print("[STATUS]:✅ »» STAF BOT MEMULAI ««")
# app.start()
# print("[STATUS]:✅ »» STAF USERBOT MEMULAI ««")
# call_py.start()
# print("[STATUS]:✅ »» PYTGCALSS CLIENT STARTED ««")
# idle()
# print("[STATUS]:❌ »» BOT BERHENTI ««")
