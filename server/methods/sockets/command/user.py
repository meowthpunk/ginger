from console.style import Style
from console.console_logs import ConsoleLogs, socketDecorator
from methods.user.user import *
from methods.user.friendInvites import *
from methods.user.friends import *
from flask_socketio import emit
# from sockets import socket


@socketDecorator('AUTORIZATE')
def autorisateSocket(login, password, socket):
    user = getUserViaAuth(login, password)

    user_friend_invites = getFriendInvites(login)
    user_not_accepted_friend_invites = getNotAcceptedFriendInvites(login)
    user_friends = getFriends(login)
    friendlist = {
        "user_friend_invites": user_friend_invites,
        "user_not_accepted_friend_invites": user_not_accepted_friend_invites,
        "user_friends": user_friends,
    }

    user_info = {
        "user": user.userInfo(),
        "friendlist": friendlist,
    }

    emit("autorizate", user_info)

    ConsoleLogs.PRINT(f"User friends:")
    ConsoleLogs.PRINT(f"- invites: {user_friend_invites}")
    ConsoleLogs.PRINT(f"- not accepted: {user_not_accepted_friend_invites}")
    ConsoleLogs.PRINT(f"- friends: {user_friends}")
    ConsoleLogs.PRINT(f"Connectet user: {Style.BLUE}{login}{Style.ZERO}")


@socketDecorator('REGISTRATION')
def registrationSocket(login, password):
    result = registrateUser(login, password)
    match result:
        case True:
            emit("try_to_registrate", {"succes": 101})
            ConsoleLogs.PRINT(f"Try to registrate: Succes - 101")
        case False:
            emit("try_to_registrate", {"succes": 401})
            ConsoleLogs.PRINT(f"Try to registrate: Aproval - 401")


@socketDecorator('LOGIN')
def loginSocket(login, password):
    result = loginUser(login, password)
    match result:
        case 404:
            emit("try_to_login", {"succes": 404})
            ConsoleLogs.PRINT(f"Try to login: Aproval - 404")
        case 402:
            emit("try_to_login", {"succes": 402})
            ConsoleLogs.PRINT(f"Try to login: Aproval - 402")
        case 100:
            emit("try_to_login", {"succes": 100})
            ConsoleLogs.PRINT(f"Try to login: Succes - 100")


@socketDecorator('SEND MESS TO CHAT')
def sendMessSocket(socket, data):
    ConsoleLogs.PRINT(data)
    socket.emit("send_message_to_all_chat", data, namespace='/auth')


@socketDecorator('SEND FRIENDS INVITE')
def sendFriendInvite(data, socket):
    charge = createFriendInvite(data["user"], data["friend_invite"])
    ConsoleLogs.PRINT(charge)
    socket.emit("send_friend_invite", {
        "user": data["friend_invite"],
        "friend_invite": {
            "user": getUserFriendViaLogin(data["user"])
        }
    }, namespace='/auth')

    emit("send_friend_invite_answ", {
        "friend_invite": {
            "user": getUserFriendViaLogin(data["friend_invite"])
        }
    }, namespace='/auth')


@socketDecorator('ACCEPT FRIENDS INVITE')
def acceptFriendInviteSocket(data, socket):
    charge = acceptFriendInvite(
        data["user_frst_login"], data["user_sec_login"])
    ConsoleLogs.PRINT(charge)
    ConsoleLogs.PRINT(data["user_sec_login"])
    socket.emit("accept_friend_invite", {
        "user": data["user_sec_login"],
        "friend": {
            "user": getUserFriendViaLogin(data["user_frst_login"])
        }
    }, namespace='/auth')

    emit("accept_friend_invite_answ", {
        "friend": {
            "user": getUserFriendViaLogin(data["user_sec_login"])
        }
    }, namespace='/auth')


@socketDecorator('DECLINE FRIENDS INVITE')
def declineFriendInviteSocket(data, socket):
    charge = declineFriendInvite(
        data["user_sec_login"], data["user_frst_login"])
    ConsoleLogs.PRINT(charge)
    socket.emit("decline_friend_invite", {
        "user": data["user_sec_login"],
        "login": data["user_frst_login"]
    }, namespace='/auth')

    emit("decline_friend_invite_answ", {
        "login": data["user_sec_login"]
    }, namespace='/auth')


@socketDecorator('REMOVE FRIEND')
def removeFriendSocket(data, socket):
    charge = removeFriend(data["user_frst_login"], data["user_sec_login"])
    ConsoleLogs.PRINT(charge)
    socket.emit("remove_friend_invite", {
        "user_frst_login": data["user_sec_login"],
        "user_sec_login": data["user_frst_login"]
    }, namespace='/auth')
    emit("remove_friend_invite_answ", {
        "login": data["user_sec_login"],
    }, namespace='/auth')
