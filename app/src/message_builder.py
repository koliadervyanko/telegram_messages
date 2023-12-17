from telethon.types import Message


class MessageBuilder:
    @staticmethod
    def build(message: Message):
        print(message)
