from telethon.types import Message

from .dto.csv_data_dto import CsvDataDto
from .message_builder import MessageBuilder


class MessageParser:
    def __init__(self, csv_data: CsvDataDto, client, message_builder: MessageBuilder):
        self.__csv_data = csv_data
        self.client = client
        self.message_builder = message_builder

    async def parse(self):
        await self.get_messages()

    async def get_messages(self):
        for link in self.__csv_data.links:
            for key_word in self.__csv_data.key_words:
                messages = self.client.iter_messages(link, search=key_word)
                message: Message
                async for message in messages:
                    built_message = self.message_builder.build(message)
                    break
