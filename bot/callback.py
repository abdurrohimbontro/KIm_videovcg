from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Veez


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ā BAGAIMANA CARA MENGGUNAKAN BOT INI:

1.) pertama, masukkan saya ke grup kamu
2.) Jadikan saya admin ,dan beri ijin untuk menambahkan admin baru
3.) Masukkan  @{Veez.ASSISTANT_NAME } ke grup kamu
4.) Nyalakan obrolan suara setelah itu start untuk streaming video.
5.) type /vplay (reply to video) untu6 memulai.
6.) type /vstop untuk mengakhiri video streaming.

š **Catatan: perintah stream & stop hanya dapat dilakukan oleh admin dalam grup !**

ā” __Maintained by KIM officiak__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š Kembali", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"āØ **Halo, saya bot streaming video grup telegram.**\n\nš­ **Saya dibuat untuk streaming video dalam grup  "
        f"video chat dengan mudah..**\n\nā **To find out how to use me, Untuk mengetahui cara menggunakan saya, silakan tekan tombol bantuan di bawah** šš»",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "ā TAMBAKAN SAYA KE GRUP ā", url=f"https://t.me/{Veez.BOT_USERNAME}?startgroup=true")
            ], [
                InlineKeyboardButton(
                    "ā BAGAIMANA CARA MENGGUNAKAN SAYA", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "š syarat & ketentuan", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "š¬ Grup", url="https://t.me/Crazy_people345"),
                InlineKeyboardButton(
                    "š£ Channel", url="https://t.me/Curhatanmassa")
            ], [
                InlineKeyboardButton(
                    "š©š»āš» Bantuan", url="https://t.me/warga_pati")
            ], [
                InlineKeyboardButton(
                    "š Semua perintah", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""š **informasi bot !**

š¤ __Bot ini dibuat untuk melakukan streaming video dalam obrolan video grup telegram menggunakan beberapa metode dari WebRTC.__

š³ __Didukung oleh PyTg memanggil API klien Async untuk Panggilan Grup Telegram, dan Pyrogram API MTProto telegram
Pustaka dan Kerangka Klien dalam Python Murni untuk Pengguna dan Bot.__

āļø __Terima kasih kepada para pengembang yang telah berpartisipasi dalam pengembangan bot ini, daftar devs dapat dilihat di bawah ini:__
___Bot ini dilisensikan di bawah Lisensi GNU-GPL 3.0____""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š Kembali", callback_data="cbstart")
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""š semua perintah:

Ā» /vplay (balas ke video atau yt/url langsung) - untuk streaming video
Ā» /vstop - hentikan streaming video
Ā» /song (nama lagu) - download lagu dari YT
Ā» /vsong (nama video) - unduh video dari YT
Ā» /lyrics (nama lagu) - penghapus lirik
Ā» /vjoin - undang asisten bergabung ke grup Anda
Ā» /vleave - perintahkan asisten keluar dari grup Anda

CMD MENYENANGKAN:

Ā» /asupan - cek sendiri
Ā» /chika - cek sendiri
Ā» /wibu - cek sendiri
Ā» /truth - periksa sendiri
Ā» /dare - periksa sendiri

CMD TAMBAHAN:

Ā» /tts (membalas teks) - teks ke ucapan
Ā» /alive - periksa status hidup bot
Ā» /ping - periksa status bot ping
Ā» /uptime - periksa status uptime bot
Ā» /sysinfo - periksa informasi sistem bot

HANYA SUDO:

Ā» /rmd - hapus semua file yang diunduh
Ā» /rmw - hapus semua file mentah yang diunduh
Ā» /leaveall - perintahkan asisten keluar dari semua grup

āļø__Dikelola oleh KIM official___""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "š Kembali", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
