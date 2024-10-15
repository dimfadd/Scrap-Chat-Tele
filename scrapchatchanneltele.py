from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel

# API ID dan Hash dari my.telegram.org
api_id = '29571344'
api_hash = '83071db94acd379a1242d3be3febd337'
phone = '+6285329869691'

# Membuat client Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    try:
        # Mengambil entitas channel menggunakan username atau ID publik
        entity = await client.get_entity('https://t.me/+tj36CSPlZMk5Mjg9')  # Bisa menggunakan @username atau URL
        channel_id = entity.id
        access_hash = entity.access_hash

        # Menggunakan InputPeerChannel
        channel = InputPeerChannel(channel_id, access_hash)

        # Membuka file HTML untuk menulis
        with open("telegram_messages.html", "w", encoding="utf-8") as file:
            # Menulis header HTML
            file.write("<html><head><title>Telegram Messages</title></head><body>")
            file.write("<h1>Pesan dari Channel</h1>")

            # Mengambil 100 pesan dari channel
            async for message in client.iter_messages(channel, limit=100):
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