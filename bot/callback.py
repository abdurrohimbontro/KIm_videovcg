from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Veez


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ BAGAIMANA CARA MENGGUNAKAN BOT INI:

1.) pertama, masukkan saya ke grup kamu
2.) Jadikan saya admin ,dan beri ijin untuk menambahkan admin baru
3.) Masukkan  @{Veez.ASSISTANT_NAME } ke grup kamu
4.) Nyalakan obrolan suara setelah itu start untuk streaming video.
5.) type /vplay (reply to video) untu6 memulai.
6.) type /vstop untuk mengakhiri video streaming.

📝 **Catatan: perintah stream & stop hanya dapat dilakukan oleh admin dalam grup !**

⚡ __Maintained by KIM officiak__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🔙 Kembali", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"✨ **Halo, saya bot streaming video grup telegram.**\n\n💭 **Saya dibuat untuk streaming video dalam grup  "
        f"video chat dengan mudah..**\n\n❔ **To find out how to use me, Untuk mengetahui cara menggunakan saya, silakan tekan tombol bantuan di bawah** 👇🏻",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "➕ TAMBAKAN SAYA KE GRUP ➕", url=f"https://t.me/{Veez.BOT_USERNAME}?startgroup=true")
            ], [
                InlineKeyboardButton(
                    "❔ BAGAIMANA CARA MENGGUNAKAN SAYA", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "🌐 syarat & ketentuan", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "💬 Grup", url="https://t.me/Crazy_people345"),
                InlineKeyboardButton(
                    "📣 Channel", url="https://t.me/Curhatanmassa")
            ], [
                InlineKeyboardButton(
                    "👩🏻‍💻 Bantuan", url="https://t.me/warga_pati")
            ], [
                InlineKeyboardButton(
                    "📑 Semua perintah", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🌐 **informasi bot !**

🤖 __Bot ini dibuat untuk melakukan streaming video dalam obrolan video grup telegram menggunakan beberapa metode dari WebRTC.__

📳 __Didukung oleh PyTg memanggil API klien Async untuk Panggilan Grup Telegram, dan Pyrogram API MTProto telegram
Pustaka dan Kerangka Klien dalam Python Murni untuk Pengguna dan Bot.__

✍️ __Terima kasih kepada para pengembang yang telah berpartisipasi dalam pengembangan bot ini, daftar devs dapat dilihat di bawah ini:__
___Bot ini dilisensikan di bawah Lisensi GNU-GPL 3.0____""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🔙 Kembali", callback_data="cbstart")
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📑 semua perintah:

» /vplay (balas ke video atau yt/url langsung) - untuk streaming video
» /vstop - hentikan streaming video
» /song (nama lagu) - download lagu dari YT
» /vsong (nama video) - unduh video dari YT
» /lyrics (nama lagu) - penghapus lirik
» /vjoin - undang asisten bergabung ke grup Anda
» /vleave - perintahkan asisten keluar dari grup Anda

CMD MENYENANGKAN:

» /asupan - cek sendiri
» /chika - cek sendiri
» /wibu - cek sendiri
» /truth - periksa sendiri
» /dare - periksa sendiri

CMD TAMBAHAN:

» /tts (membalas teks) - teks ke ucapan
» /alive - periksa status hidup bot
» /ping - periksa status bot ping
» /uptime - periksa status uptime bot
» /sysinfo - periksa informasi sistem bot

HANYA SUDO:

» /rmd - hapus semua file yang diunduh
» /rmw - hapus semua file mentah yang diunduh
» /leaveall - perintahkan asisten keluar dari semua grup

✍️__Dikelola oleh KIM official___""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🔙 Kembali", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
