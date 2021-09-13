# Copyright (C) 2021 By VeezMusicProject
# module by @tofikdn

import requests
from pyrogram import Client

from config import Veez
from helpers.filters import command


@Client.on_message(command(["asupan", f"asupan@{Veez.BOT_USERNAME}"]))
async def asupan(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception as ex:
        await message.reply_text("gagal mendapatkan asupan dari server...")
        print(ex)


@Client.on_message(command(["wibu", f"wibu@{Veez.BOT_USERNAME}"]))
async def wibu(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception as ex:
        print(ex)
        await message.reply_text("gagal mendapatkan wibu dari server...")


@Client.on_message(command(["chika", f"chika@{Veez.BOT_USERNAME}"]))
async def chika(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception as ex:
        print(ex)
        await message.reply_text("gagal mendapatkan Chika dari server...")


@Client.on_message(command(["truth", f"truth@{Veez.BOT_USERNAME}"]))
async def truth(_, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth-en").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception as ex:
        print(ex)
        await message.reply_text("ada yang salah...")


@Client.on_message(command(["dare", f"dare@{Veez.BOT_USERNAME}"]))
async def dare(_, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare-en").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception as ex:
        print(ex)
        await message.reply_text("ada yang salah...")


@Client.on_message(command(["lyric", f"lyric@{Veez.BOT_USERNAME}"]))
async def lirik(_, message):
    rep = await message.reply_text("🔎 **mencari lirik lagu...**")
    try:
        if len(message.command) < 2:
            await message.reply_text("**berikan nama lirik lagunya juga !**")
            return
        query = message.text.split(None, 1)[1]
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception as ex:
        print(ex)
        await rep.edit("**Lirik tidak ditemhkan.** Tolong berikan saya nama lagu yang valid !")
