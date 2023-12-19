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
            channel_entity = await self.client.get_entity(link)
            print(f"Channel name: {channel_entity.title}")
            for key_word in self.__csv_data.key_words:
                print(f"Key word: {key_word}")
                messages = self.client.iter_messages(channel_entity, search=key_word)
                current = 0
                message: Message
                async for message in messages:
                    if message.date.date() >= self.__csv_data.date:
                        built_message = await self.message_builder.build(link, message, key_word, True)
                        parsed_messages.append(built_message)
                        current += 1
                        print(f"Completed {current}")
        if len(parsed_messages) == 0:
            print("Nothing to add")
        return parsed_messages
