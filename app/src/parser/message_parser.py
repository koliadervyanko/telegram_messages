from telethon.types import Message

from src.dto.csv_data_dto import CsvDataDto
from src.message_builder import MessageBuilder


class MessageParser:
    def __init__(self, csv_data: CsvDataDto, client, message_builder: MessageBuilder):
        self.__csv_data = csv_data
        self.client = client
        self.message_builder = message_builder

    async def parse(self):
        try:
            messages = await self.get_messages()
            return messages
        except Exception as e:
            print(e)

    async def get_messages(self):
        parsed_messages = []
        for link in self.__csv_data.links:
            for key_word in self.__csv_data.key_words:
                messages = self.client.iter_messages(link, search=key_word, reverse=True)
                current = 0
                message: Message
                async for message in messages:
                    built_message = await self.message_builder.build(link, message)
                    parsed_messages.append(built_message)
                    current += 1
                    print(f"Completed {current}")
        return parsed_messages
