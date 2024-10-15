from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser

# API ID dan Hash dari my.telegram.org
api_id = '29571344'
api_hash = '83071db94acd379a1242d3be3febd337'
phone = '+6285329869691'

# Membuat client Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    try:
        # Mengambil entitas user menggunakan username atau user ID
        entity = await client.get_entity('t.me/@Dataerdha')  # Bisa menggunakan @username atau URL
        user_id = entity.id
        access_hash = entity.access_hash

        # Menggunakan InputPeerUser untuk user chat pribadi
        user = InputPeerUser(user_id, access_hash)

        # Membuka file HTML untuk menulis
        with open("telegram_user_messages.html", "w", encoding="utf-8") as file:
            # Menulis header HTML
            file.write("<html><head><title>Telegram User Messages</title></head><body>")
            file.write("<h1>Pesan dari Chat Pribadi</h1>")

            # Mengambil 100 pesan dari user
            async for message in client.iter_messages(user, limit=100):
                if message.text:  # Pastikan pesan bukan None
                    # Menulis setiap pesan ke file HTML
                    file.write(f"<p><b>Pengirim:</b> {message.sender_id}<br>")
                    file.write(f"<b>Pesan:</b> {message.text}<br>")
                    file.write(f"<b>Tanggal:</b> {message.date}</p>")
                    file.write("<hr>")

            # Menulis footer HTML
            file.write("</body></html>")

    except Exception as e:
        print(f"Error: {e}")

# Menjalankan client
with client:
    client.loop.run_until_complete(main())
