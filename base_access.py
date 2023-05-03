from validators import *
from classes import *
import uuid

users = dict()
chats = dict()
messages = dict()


def hash_func(strg):
    return hash(strg)


def user_exists(login):
    if not users.get(login):
        return False
    return True


def user_password(login):
    user_ = users.get(login)
    if not user_:
        return None
    return user_.password


def check_user(login, password):
    err = None

    res, err = valid_uname(login)
    if not res:
        return -1, err

    res, err = valid_password(password)
    if not res:
        return -1, err

    pswd = user_password(login)
    if not pswd:
        return 0, None
    if pswd == hash_func(password):
        return 1, None
    return -1, "Invalid login or password, try again"


def set_user(login, password):
    users[login] = User(str(uuid.uuid4()), login, hash_func(password))


def user_add_chat(login, chatID):
    users[login].chats.append(chatID)


def user_get_chats(login):
    return users[login].chats


def get_message(ID):
    return messages[ID]


def chat_exists(ID):
    if not chats.get(ID):
        return False
    return True


def get_chat_name(ID):
    return chats[ID].name


def get_chat_messages(ID):
    return list(map(get_message, chats[ID].messages))


def set_chat(name, unames):
    new_chat = Chat(str(uuid.uuid4()), name, unames)
    chats[new_chat.id] = new_chat
    for name in unames:
        user_add_chat(name, new_chat.id)


def add_message_in_chat(chat_id, author, msg_text):
    new_msg = Message(str(uuid.uuid4()), chat_id, author, msg_text)
    messages[new_msg.id] = new_msg
    chats[chat_id].messages.append(new_msg.id)
    if len(chats[chat_id]) > 25:
        chats[chat_id].messages = chats[chat_id].messages[len(chats[chat_id]) - 25 + 1:]
