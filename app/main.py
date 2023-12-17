from telethon import TelegramClient

from config import id, hash
from src.csv_parser import CsvParser
from src.message_builder import MessageBuilder
from src.message_parser import MessageParser

client = TelegramClient("name", id, hash)


async def main():
    csv_parser = CsvParser("data.csv")
    csv_data = csv_parser.parse()
    message_builder = MessageBuilder()
    message_parser = MessageParser(csv_data, client, message_builder)
    await message_parser.get_messages()


if __name__ == "__main__":
    try:
        with client:
            client.loop.run_until_complete(main())
    except Exception as e:
        print(f"Error in main: {e}")
