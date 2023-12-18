from telethon import TelegramClient

from src import CsvParser, MessageParser
from src.env_reader import EnvReader
from src.message_builder import MessageBuilder

env_reader = EnvReader(".env")
env_data = env_reader.get_env_data()
client = TelegramClient("name", env_data.id, env_data.hash)


async def main():
    csv_parser = CsvParser("data.csv")
    csv_data = csv_parser.parse()
    message_builder = MessageBuilder(client)
    message_parser = MessageParser(csv_data, client, message_builder)
    messages = await message_parser.get_messages()


if __name__ == "__main__":
    try:
        with client:
            client.loop.run_until_complete(main())
    except Exception as e:
        print(f"Error in main: {e}")
