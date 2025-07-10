from telethon import TelegramClient
from io import BytesIO
import asyncio

# ✅ Your credentials here
api_id = 28243499      # <-- replace with your API ID (integer)
api_hash = "74b82239bae847195fdcd651d351dd7a"  # <-- replace with your API HASH

# ✅ Your channel settings here
SOURCE_CHANNEL = -1002862844062  # <-- source channel ID (NO quotes if integer)
DEST_CHANNEL = -1002519079821     # <-- destination channel ID

client = TelegramClient("session_name", api_id, api_hash)

async def main():
    print("🚀 Forwarding video lectures...")

    total_sent = 0
    async for msg in client.iter_messages(SOURCE_CHANNEL, limit=1000):
        if msg.video:
            print(f"🎞 Downloading message {msg.id}")
            bio = BytesIO()
            bio.name = "video.mp4"

            await client.download_media(msg, file=bio)
            bio.seek(0)

            await client.send_file(DEST_CHANNEL, file=bio, caption=msg.text or "Lecture 🎓")
            total_sent += 1
            print(f"✅ Sent video ID: {msg.id}")

    print(f"\n🎉 Done! Total videos forwarded: {total_sent}")

with client:
    client.loop.run_until_complete(main())
