class MessageDto:
    def __init__(self, username: str, message: str, name: str, link: str, date):
        self.username = username
        self.message = message
        self.name = name
        self.link = link
        self.date = date
