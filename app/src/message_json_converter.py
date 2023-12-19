import json

from src.dto import MessageDto


class MessageJsonConverter:
    def to_dict(self, replies):
        if replies:
            return [self.convert(reply) for reply in replies]
        else:
            return None

    def convert(self, message: MessageDto):
        if message.replies:
            message.replies = self.to_dict(message.replies)

        jsoned = json.dumps(message.__dict__, indent=1, ensure_ascii=False)
        return json.loads(jsoned)
