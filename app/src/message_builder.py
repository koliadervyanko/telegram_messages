from telethon.types import Message, User

from .dto.message_dto import MessageDto
from .dto.user_data_dto import UserDataDto


class MessageBuilder:
    def __init__(self, client):
        self.client = client

    async def build(self, link: str, message: Message, key_word: str) -> MessageDto:
        msg_link = self.generate_msg_link(link, message)
        replies = await self.get_replies(message, link, key_word)
        user_data = await self.get_user_data(message)
        date = self.date_handling(message)

        return MessageDto(user_data.username, user_data.name, message.message, msg_link, date, replies, message.id,
                          key_word)

    @staticmethod
    def date_handling(message: Message):
        date = message.date.date()
        time = message.date.time()
        return f"{date} / {time}"

    async def get_replies(self, message: Message, link: str, key_word: str):
        replies_msgs = []
        replies_is_exists = bool(message.replies)
        print(message.replies)
        if replies_is_exists:
            replies = self.client.iter_messages(link, reply_to=message.id)
            reply: Message
            async for reply in replies:
                built_reply = await self.build(link, reply, key_word)
                replies_msgs.append(built_reply)
        return None if replies_msgs == [] else replies_msgs

    @staticmethod
    def generate_msg_link(link: str, message: Message) -> str:
        msg_link = f"{link}/{message.id}"
        return msg_link

    @staticmethod
    async def get_user_data(message: Message) -> UserDataDto:
        sender: User = await message.get_sender()
        if sender:
            return UserDataDto(sender.username, sender.first_name)
        else:
            return UserDataDto("sent by admin", "sent by admin")
