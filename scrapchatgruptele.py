from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChat

# API ID dan Hash dari my.telegram.org
api_id = '29571344'
api_hash = '83071db94acd379a1242d3be3febd337'
phone = '+6285329869691'

# Membuat client Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    try:
        # Mengambil entitas grup menggunakan username atau ID grup
        entity = await client.get_entity('https://t.me/+tj36CSPlZMk5Mjg9')  # Bisa menggunakan @username atau URL
        group_id = entity.id

        # Menggunakan InputPeerChat untuk grup
        group = InputPeerChat(group_id)

        # Membuka file HTML untuk menulis
        with open("telegram_group_messages.html", "w", encoding="utf-8") as file:
            # Menulis header HTML
            file.write("<html><head><title>Telegram Group Messages</title></head><body>")
            file.write("<h1>Pesan dari Grup</h1>")

            # Mengambil 100 pesan dari grup
            async for message in client.iter_messages(group, limit=100):
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
