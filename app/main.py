from telethon import TelegramClient

from src import MessageJsonConverter, DbApiHandler
from src.env_reader import EnvReader
from src.message_builder import MessageBuilder
from src.parser import ExcelParser, MessageParser

env_reader = EnvReader(".env")
env_data = env_reader.get_env_data()
client = TelegramClient("name", env_data.id, env_data.hash)


async def main():
    excel_parser = ExcelParser("data.xlsx")
    excel_data = excel_parser.parse()
    message_builder = MessageBuilder(client)
    message_parser = MessageParser(excel_data, client, message_builder)
    messages = await message_parser.get_messages()
    if messages:
        message_json_converter = MessageJsonConverter()
        db_api_handler = DbApiHandler(messages, message_json_converter)
        await db_api_handler.req()


if __name__ == "__main__":
    try:
        with client:
            client.loop.run_until_complete(main())
    except Exception as e:
        print(f"Error: {e}")
