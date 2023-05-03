class User(object):
    def __init__(self, id_, name, phash):
        self.id = id_
        self.name = name
        self.password = phash
        self.chats = []


class Message(object):
    def __init__(self, id_, chat_id_, author, text):
        self.id = id_
        self.chat_id = chat_id_
        self.author = author
        self.text = text


class Chat(object):
    def __init__(self, id_, name, users_):
        self.id = id_
        self.name = name
        self.users = users_
        self.messages = []
