import string


def valid_uname(login):
    err = None
    result = True
    if not login.isalpha():
        result = False
        err = "Username must consist of only alpha characters"
    elif len(login) not in range(3, 14):
        result = False
        err = "Username length out of bounds [3, 13]"
    return result, err


def valid_password(password):
    err = None
    result = True

    lettcnt = 0
    for letter in string.ascii_letters:
        lettcnt += password.count(letter)

    digitcnt = 0
    for digit in string.digits:
        digitcnt += password.count(digit)

    if lettcnt == 0:
        result = False
        err = "Password must contain a letter"
    elif digitcnt == 0:
        result = False
        err = "Password must contain a digit"
    elif len(password) not in range(3, 21):
        result = False
        err = "Password length out of bounds [3, 20]"
    return result, err


def valid_chatname(name):
    err = None
    result = True
    for c in name:
        if c not in (string.ascii_letters + string.digits + ' '):
            result = False
            err = "Chat name must consist of only letter, digit and space characters"

    if len(name) not in range(3, 21):
        result = False
        err = "Chat name length out of bounds [3, 20]"
    return result, err

