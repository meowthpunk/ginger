from models import Friends, FriendInvites, database
from methods.user.user import getUserIdViaLogin, getUserViaId


def removeFriend(user_frst_login, user_sec_login):

    user_frst_id = getUserIdViaLogin(user_frst_login)
    if user_frst_id == None:
        return "frst_login_error"

    user_sec_id = getUserIdViaLogin(user_sec_login)
    if user_sec_id == None:
        return "sec_login_error"

    obj_frst = database.session.query(Friends).filter(
        Friends.user_frst_id == user_frst_id,
        Friends.user_sec_id == user_sec_id
    ).first()

    obj_sec = database.session.query(Friends).filter(
        Friends.user_frst_id == user_sec_id,
        Friends.user_sec_id == user_frst_id
    ).first()

    try:
        database.session.delete(obj_frst)
        database.session.delete(obj_sec)
        database.session.commit()
    except:
        return "none_obj"

    return "removed"


def getFriends(login):
    user_id = getUserIdViaLogin(login)
    friends = database.session.query(Friends).filter(
        Friends.user_frst_id == user_id
    ).all()
    return [{
        "user": getUserViaId(invite.user_sec_id),
    } for invite in friends]
