from telethon.types import Message, User

from .dto.message_dto import MessageDto
from .dto.user_data_dto import UserDataDto


class MessageBuilder:
    def __init__(self, client):
        self.client = client

    async def build(self, link: str, message: Message, key_word: str,
                    use_replies: bool, use_replied_to: bool) -> MessageDto:

        msg_link = self.generate_msg_link(link, message.id)
        replies = await self.get_replies(message, link, key_word) if use_replies else None
        user_data = await self.get_user_data(message)
        date = self.date_handling(message)
        reply_to = await self.get_replied_to(link, message, key_word) if use_replied_to else None
        return MessageDto(user_data.username, user_data.name, message.message, msg_link, date, replies, message.id,
                          key_word, reply_to)

    async def get_replied_to(self, link: str, message: Message, key_word: str):
        if message.reply_to:
            reply_to = await self.client.get_messages(link, ids=message.reply_to.reply_to_msg_id)
            if reply_to:
                built_reply_to = await self.build(link, reply_to, key_word, False, False)
                return built_reply_to
            else:
                return None
        return None

    @staticmethod
    def date_handling(message: Message):
        date = message.date.date()
        time = message.date.time()
        return f"{date} / {time}"

    async def get_replies(self, message: Message, link: str, key_word: str):
        replies_msgs = []
        replies_is_exists = bool(message.replies)
        if replies_is_exists:
            replies = self.client.iter_messages(link, reply_to=message.id)
            reply: Message
            async for reply in replies:
                built_reply = await self.build(link, reply, key_word, False, False)
                replies_msgs.append(built_reply)
        replies_msgs.reverse()
        return replies_msgs or None

    @staticmethod
    def generate_msg_link(link: str, id: int) -> str:
        msg_link = f"{link}/{id}"
        return msg_link

    @staticmethod
    async def get_user_data(message: Message) -> UserDataDto:
        sender: User = await message.get_sender()
        if sender:
            return UserDataDto(sender.username, sender.first_name)
        else:
            return UserDataDto("sent by admin", "sent by admin")
