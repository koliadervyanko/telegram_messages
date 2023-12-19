class MessageDto:
    def __init__(self, username: str, name: str, message: str, link: str, date: str, replies, message_id: int,
                 key_word: str):
        self.username = username
        self.message = message
        self.name = name
        self.link = link
        self.date = date
        self.replies = replies
        self.messageId = message_id
        self.keyWord = key_word
