from models import database, User


def registrateUser(login, password):
    user = database.session.query(User).filter(User.login == login).first()

    if user == None:
        user = User(login, password)
        database.session.add(user)
        database.session.commit()
        return True
    else:
        return False


def loginUser(login, password):

    user = database.session.query(User).filter(
        User.login == login).first()
    if user == None:
        return 404
    else:
        pass_wer = user.passWer(password)

        if pass_wer == False:
            return 402
        else:
            return 100


def getUserViaAuth(login, password):
    try:
        return database.session.query(User).filter(User.login == login, User.password == password).first()
    except:
        return None


def getUserIdViaLogin(login):
    try:
        return database.session.query(User).filter(User.login == login).first().id
    except:
        return None


def getUserViaId(id):
    try:
        return database.session.query(User).filter(User.id == id).first().userInfoFriend()
    except:
        return None


def getUserFriendViaLogin(login):
    try:
        return database.session.query(User).filter(User.login == login).first().userInfoFriend()
    except:
        return None
