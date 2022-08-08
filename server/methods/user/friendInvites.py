from models import Friends, FriendInvites, database
from methods.user.user import getUserIdViaLogin, getUserViaId


def createFriendInvite(user_frst_login, user_sec_login):

    if user_frst_login == user_sec_login:
        return "cant_send_to_yourself"

    user_frst_id = getUserIdViaLogin(user_frst_login)
    if user_frst_id == None:
        return "frst_login_error"

    user_sec_id = getUserIdViaLogin(user_sec_login)
    if user_sec_id == None:
        return "sec_login_error"

    isFriends = database.session.query(Friends).filter(
        Friends.user_frst_id == user_frst_id,
        Friends.user_sec_id == user_sec_id
    ).first() != None

    if isFriends == True:
        return "already_friends"

    isAlreadyIvnite = database.session.query(FriendInvites).filter(
        FriendInvites.user_frst_id == user_sec_id,
        FriendInvites.user_sec_id == user_frst_id
    ).first() != None

    if isAlreadyIvnite == True:
        acceptFriendInvite(user_frst_login, user_sec_login)
        return "already_invite_accepted"

    find = database.session.query(FriendInvites).filter(
        FriendInvites.user_frst_id == user_frst_id,
        FriendInvites.user_sec_id == user_sec_id
    ).first()

    if find == None:
        obj = FriendInvites(user_frst_id, user_sec_id)
        database.session.add(obj)
        database.session.commit()
        return obj
    return "invite_already_existed"


def acceptFriendInvite(user_frst_login, user_sec_login):

    user_frst_id = getUserIdViaLogin(user_frst_login)
    if user_frst_id == None:
        return "frst_login_error"

    user_sec_id = getUserIdViaLogin(user_sec_login)
    if user_sec_id == None:
        return "sec_login_error"

    obj = database.session.query(FriendInvites).filter(
        FriendInvites.user_frst_id == user_sec_id,
        FriendInvites.user_sec_id == user_frst_id
    ).first()

    if obj == None:
        return "none_obj"

    friend_frst = Friends(user_frst_id, user_sec_id)
    friend_sec = Friends(user_sec_id, user_frst_id)

    database.session.add(friend_frst)
    database.session.add(friend_sec)
    database.session.commit()

    obj.acceptInvite()
    return "accepted"


def declineFriendInvite(user_frst_login, user_sec_login):
    user_frst_id = getUserIdViaLogin(user_frst_login)
    if user_frst_id == None:
        return "frst_login_error"

    user_sec_id = getUserIdViaLogin(user_sec_login)
    if user_sec_id == None:
        return "sec_login_error"

    obj = database.session.query(FriendInvites).filter(
        FriendInvites.user_frst_id == user_frst_id,
        FriendInvites.user_sec_id == user_sec_id
    ).first()

    if obj == None:
        return "none_obj"

    obj.acceptInvite()
    return "declined"


def getFriendInvites(login):
    user_id = getUserIdViaLogin(login)
    friendInvites = database.session.query(FriendInvites).filter(
        FriendInvites.user_frst_id == user_id
    ).all()
    return [{
        "user": getUserViaId(invite.user_sec_id),
    } for invite in friendInvites]


def getNotAcceptedFriendInvites(login):
    user_id = getUserIdViaLogin(login)
    friendInvites = database.session.query(FriendInvites).filter(
        FriendInvites.user_sec_id == user_id
    ).all()
    return [{
        "user": getUserViaId(invite.user_frst_id),
    } for invite in friendInvites]
