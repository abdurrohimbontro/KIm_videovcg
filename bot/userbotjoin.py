# Copyright (C) 2021 Veez Music Project

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from helpers.filters import command
from helpers.decorators import authorized_users_only, errors
from bot.videoplayer import app as USER
from config import Veez


@Client.on_message(command(["vjoin", f"vjoin@{Veez.BOT_USERNAME}"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def entergroup(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>💡 jadikan saya sebagai admin terlebih dahulu untuk melakukan itu !</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "assistant"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "🤖: saya bergabung di sini untuk streaming video di obrolan video/obrolan suara")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>✅ asisten berhasil masuk ke grup ini</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔴 KESALAHAN FLOODWAIT 🔴\n\n pengguna {user.first_name} tidak dapat bergabung dengan grup Anda karena banyaknya permintaan bergabung untuk userbot! pastikan asisten tidak dilarang di grup ini.."
        )
        return
    await message.reply_text(
        "<b>✅ asisten bot berhasil bergabung dengan obrolan Anda</b>",
    )


@Client.on_message(command(["vleave", f"vleave@{Veez.BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def leavegroup(client, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "<b>❌ asisten tidak dapat keluar dari grup karena menunggu banjir.\n\n» anda dapat mengeluarkanya secara manual</b>"
        )



@Client.on_message(command(["leaveall", f"leaveall@{Veez.BOT_USERNAME}"]))
async def outall(client, message):
    if message.from_user.id not in Veez.SUDO_USERS:
        return

    left=0
    failed=0
    lol = await message.reply("🔁 asisten meninggalkan semua obrolan")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(f"🔁 asisten pergi...\n⏳ Left: {left} chats.\n\n❌ Failed: {failed} chats.")
        except:
            failed += 1
            await lol.edit(f"🔁 asisten pergi...\n⏳ Left: {left} chats.\n\n❌ Failed: {failed} chats.")
        await asyncio.sleep(0.7)
    await client.send_message(message.chat.id, f"✅ Left {left} chats.\n\n❌ Failed {failed} chats.")
