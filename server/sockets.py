from flask_socketio import SocketIO
from config import server
from methods.sockets import *


socket = SocketIO(server, cors_allowed_origins="*")
hui = 1


# -------- SOCKETS: DEFAULT -------- #


@socket.event
def connect():
    connectSocket()


@socket.event
def disconnect():
    disconnectSocket()


# -------- SOCKETS: LOGIN -------- #


@socket.event(namespace="/login")
def connect():
    connectSocket()


@socket.event(namespace="/login")
def disconnect():
    disconnectSocket()


@socket.event(namespace="/login")
def login(login, password):
    loginSocket(login, password)


@socket.event(namespace="/login")
def registration(login, password):
    registrationSocket(login, password)


# -------- SOCKETS: AUTH -------- #


@socket.event(namespace="/auth")
def connect():
    connectSocket()


@socket.event(namespace="/auth")
def disconnect():
    disconnectSocket()


@socket.event(namespace="/auth")
def autorizate(login, password):
    autorisateSocket(login, password, socket)
    # print(type(login))
    socket.emit("pohuy", {"pidor": "pidor"}, namespace="/HUESOS")


@socket.event(namespace="/auth")
def send_mess_to_all_chat(data):
    sendMessSocket(socket, data)


@socket.event(namespace="/auth")
def send_friend_invite(data):
    sendFriendInvite(data, socket)


@socket.event(namespace="/auth")
def accept_friend_invite(data):
    acceptFriendInviteSocket(data, socket)


@socket.event(namespace="/auth")
def decline_friend_invite(data):
    declineFriendInviteSocket(data, socket)


@socket.event(namespace="/auth")
def remove_friend(data):
    removeFriendSocket(data, socket)
