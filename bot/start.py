from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from config import Veez
from helpers.decorators import sudo_users_only
from helpers.filters import command

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{Veez.BOT_USERNAME}"]))
async def start(_, m: Message):
    if m.chat.type == "private":
        await m.reply_text(
            f"āØ **Halo, saya KIM VODEO BOT .**\n\nš­ **Saya dibuat untuk streaming video dalam grup "
            f"video chat dengan mudah.**\n\nā **Untuk mengetahui cara menggunakan saya, silakan tekan tombol bantuan di bawah** šš»",
            reply_markup=InlineKeyboardMarkup( 
                [[
                    InlineKeyboardButton(
                        "ā TAMBAHKAN SAYA KE GRUP ā", url=f"https://t.me/{Veez.BOT_USERNAME}?startgroup=true")
                ], [
                    InlineKeyboardButton(
                        "ā BAGAIMANA CARA MENGGUNAKAN SAYA", callback_data="cbguide")
                ], [
                    InlineKeyboardButton(
                        "š syarat & ketentuan", callback_data="cbinfo")
                ], [
                    InlineKeyboardButton(
                        "š¬ Grup", url="https://t.me/crazy_people345"),
                    InlineKeyboardButton(
                        "š£ Channel", url="https://t.me/Curhatanmassa")
                ], [
                    InlineKeyboardButton(
                        "š©š»āš» bantuan", url="https://t.me/warga_pati")
                ], [
                    InlineKeyboardButton(
                        "š SEMUA PERINTAH", callback_data="cblist")
                ]]
            ))
    else:
        await m.reply_text("**āØ KIM VIDEO BOT sedang online āØ**",
                           reply_markup=InlineKeyboardMarkup(
                               [[
                                   InlineKeyboardButton(
                                       "ā BAGAIMANA CARA MENGGUNAKAN BOT INI", callback_data="cbguide")
                               ], [
                                   InlineKeyboardButton(
                                       "šŖļø KEMBALI", switch_inline_query='')
                               ], [
                                   InlineKeyboardButton(
                                       "š SEMUA PERINTAH", callback_data="cblist")
                               ]]
                           )
                           )


@Client.on_message(command(["alive", f"alive@{Veez.BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def alive(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"""ā **KIM VIDEO BOT sedang berjalan**\n<b>š  **waktu aktif:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "āØ Grup", url=f"https://t.me/Crazy_people345"
                    ),
                    InlineKeyboardButton(
                        "š£ Channel", url=f"https://t.me/Curhatanmassa"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{Veez.BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(_, m: Message):
    sturt = time()
    m_reply = await m.reply_text("pinging...")
    delta_ping = time() - sturt
    await m_reply.edit_text(
        "š `PUNK!!`\n"
        f"ā” `{delta_ping * 1000:.3f} ms`\n"
        f"š¾ `KIM VIDEO BOT`"
    )


@Client.on_message(command(["uptime", f"uptime@{Veez.BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "š¤ Status bot š¤\n\n"
        f"ā¢ **waktu aktif:** `{uptime}`\n"
        f"ā¢ **waktu mulai:** `{START_TIME_ISO}`"
    )
