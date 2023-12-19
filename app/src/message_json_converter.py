import json

from src.dto import MessageDto


class MessageJsonConverter:
    def to_dict(self, replies):
        if replies:
            return [self.convert(reply) for reply in replies]
        else:
            return None

    def reply_to(self, reply_to: MessageDto):
        reply_to.repliedTo = self.convert(reply_to)
        return reply_to.repliedTo

    def convert(self, message: MessageDto):
        if message.replies:
            message.replies = self.to_dict(message.replies)
        if message.repliedTo:
            message.repliedTo = self.reply_to(message.repliedTo)
        jsoned = json.dumps(message.__dict__, indent=1, ensure_ascii=False)
        return json.loads(jsoned)
