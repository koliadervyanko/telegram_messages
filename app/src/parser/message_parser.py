from telethon.types import Message

from src.dto.excel_data_dto import ExcelDataDto
from src.message_builder import MessageBuilder


class MessageParser:
    def __init__(self, excel_data: ExcelDataDto, client, message_builder: MessageBuilder):
        self.__excel_data = excel_data
        self.client = client
        self.message_builder = message_builder

    async def parse(self):
        try:
            messages = await self.get_messages()
            print("All message parsed successfully")
            return messages
        except Exception as e:
            print(f"Error parsing messages: {e}")

    async def get_messages(self):
        parsed_messages = []
        for link in self.__excel_data.links:
            channel_entity = await self.client.get_entity(link)
            print(f"Channel name: {channel_entity.title}")
            for key_word in self.__excel_data.key_words:
                print(f"Key word: {key_word}")
                messages = self.client.iter_messages(channel_entity, search=key_word)
                current = 0
                message: Message
                print(f"Date: {self.__excel_data.date}")
                async for message in messages:
                    if message.date.date() >= self.__excel_data.date:
                        built_message = await self.message_builder.build(link, message, key_word, True, True)
                        parsed_messages.append(built_message)
                        current += 1
                        print(f"Completed {current}")
        if len(parsed_messages) == 0:
            print("Nothing to add")
        return parsed_messages
