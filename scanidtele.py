from telethon.sync import TelegramClient

# API ID dan Hash dari my.telegram.org
api_id = '29571344'
api_hash = '83071db94acd379a1242d3be3febd337'
phone = '+6285329869691'

# Membuat client Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    # Mengambil semua dialog (chat, grup, dan channel)
    dialogs = await client.get_dialogs()

    # Mencetak nama dan username (jika ada) untuk setiap grup/channel
    for dialog in dialogs:
        if dialog.is_group or dialog.is_channel:
            username = getattr(dialog.entity, 'username', None)  # Mengambil username jika ada, None jika tidak ada
            print(f"Nama: {dialog.name}, Username: {username}")

with client:
    client.loop.run_until_complete(main())
