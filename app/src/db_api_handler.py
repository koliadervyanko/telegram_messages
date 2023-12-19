import requests

from .dto.message_dto import MessageDto
from .message_json_converter import MessageJsonConverter


class DbApiHandler:
    def __init__(self, messages, message_json_converter: MessageJsonConverter):
        self.messages = messages
        self.message_json_converter = message_json_converter

    async def req(self):
        for message in self.messages:
            await self.save_data(message)

    async def save_data(self, message: MessageDto):
        try:
            jsoned_message = self.message_json_converter.convert(message)
            res = requests.post("http://localhost:4200/messages", json=jsoned_message)
            if res.ok:
                print(f"Added successfully | {res.status_code}")
            else:
                print(f"Error adding | {res.status_code} | {message.link}")
                # print(res.text)


        except Exception as e:
            print(f"Error: {e}")
