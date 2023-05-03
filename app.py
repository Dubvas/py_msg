from flask import Flask, send_from_directory, jsonify, make_response, request, session, redirect,\
    render_template
from markupsafe import escape
# from pymongo import MongoClient
# from pymongo.collection import Collection
from base_access import *


app = Flask(__name__)
app.secret_key = b'bibaibobadvadolboeba228133769420575757179'


@app.route("/static/<path:filename>")
def file(filename):
    return send_from_directory("static", filename)

@app.route("/")
def index():
    if not session.get('username'):
        return redirect("/login")

    chat_ids = user_get_chats(session['username'])
    ln = len(chat_ids)
    chat_names = list(map(get_chat_name, chat_ids))
    result = make_response((render_template("index.html", testt=session['username'],
                                            ln=ln, chatIDs=chat_ids, chatNames=chat_names), 200))

    return result

@app.route("/login", methods=["GET", "POST"])
def login_pd():
    if session.get('username'):
        return redirect("/")

    err = None

    if request.method == 'GET':
        result = make_response((render_template("login_page.html", error=""), 200))
        return result

    res, err = check_user(request.form.get('username', ""), request.form.get('password', ""))
    if res == 0:
        set_user(request.form.get('username'), request.form.get('password'))
    if res >= 0:
        session['username'] = request.form.get('username')
        return redirect("/")

    return make_response((render_template("login_page.html", error=err), 400))

@app.route("/logout")
def logout():
    session.pop('username')
    return redirect("/login")


@app.route("/make_chat", methods=["GET", "POST"])
def make_chat_pd():
    if not session.get('username'):
        return redirect("/login")

    err = None

    if request.method == 'GET':
        result = make_response((render_template("make_page.html"), 200))
        return result

    cname = request.form.get('chat_name', "")
    res, err = valid_chatname(cname)
    if not res:
        return make_response((render_template("make_page.html", error=err), 400))

    unames = request.form.get('users')

    if not unames:
        err = "At least one user should be there"
        return make_response((render_template("make_page.html", error=err), 400))

    unames = unames.split('\n')
    unames[:] = [x for x in unames if x]
    unames[:] = [x if x[-1] != '\r' else x[:-1] for x in unames]
    unames = list(dict.fromkeys(unames))
    if session.get('username') in unames:
        unames.remove(session.get('username'))

    if len(unames) == 0:
        err = "At least one user should be there"
        return make_response((render_template("make_page.html", error=err), 400))

    unames.append(session.get('username'))
    print(unames)
    for name in unames:
        if not user_exists(name):
            err = "Wrong username! " + str(escape(name))
            return make_response((render_template("make_page.html", error=err), 400))

    set_chat(cname, unames)

    return redirect("/")

@app.get("/chat/<string:chat_id>")
def chat_pg(chat_id):
    if not session.get('username'):
        return redirect("/login")

    msgs = get_chat_messages(chat_id)
    return render_template("chat_page.html", chatName=get_chat_name(chat_id),
                           ln=len(msgs), messages=msgs, chatID=chat_id)

@app.post("/send_msg")
def send_msg():
    if not session.get('username'):
        return make_response(("ERROR", 403))
    r_data = request.get_json(force=True)
    author = session['username']
    chat_id = r_data.get('chat_id')
    msg_text = r_data.get('user_message')

    if not chat_id:
        return make_response(("ERROR", 400))
    if not chat_exists(chat_id):
        return make_response(("ERROR", 404))

    if chat_id not in user_get_chats(author):
        return make_response(("ERROR", 403))

    if len(msg_text) > 256:
        msg_text = msg_text[:256]

    add_message_in_chat(chat_id, author, msg_text)

    return make_response(("GOOD", 200))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
