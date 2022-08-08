from flask_sqlalchemy import SQLAlchemy
from config import server

database = SQLAlchemy(server)


class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    login = database.Column(database.String(255), unique=True)
    password = database.Column(database.String(255))
    gems = database.Column(database.Integer, default=0)
    expirience = database.Column(database.Integer, default=0)
    avatar = database.Column(
        database.String, default="https://img.freepik.com/premium-vector/gamer-mascot-geek-boy-esports-logo-avatar-with-headphones-glasses-cartoon-character_8169-228.jpg")
    # order_ingredient_product = database.relationship(
    #     'OrderProductsIngredients', backref='orderingredientproduct')

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def loginPass(self):
        return {
            "login": self.login,
            "password": self.password,
        }

    def passWer(self, password):
        return self.password == password

    def userInfo(self):
        return {
            "login": self.login,
            "gems": self.gems,
            "expirience": self.expirience,
            "avatar": self.avatar,
        }

    def userInfoFriend(self):
        return {
            "login": self.login,
            "avatar": self.avatar,
        }


class FriendInvites(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_frst_id = database.Column(database.Integer)
    user_sec_id = database.Column(database.Integer)

    def __init__(self, user_frst_id, user_sec_id):
        self.user_frst_id = user_frst_id
        self.user_sec_id = user_sec_id

    def acceptInvite(self):
        database.session.delete(self)
        database.session.commit()


class Friends(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_frst_id = database.Column(database.Integer)
    user_sec_id = database.Column(database.Integer)

    def __init__(self, user_frst_id, user_sec_id):
        self.user_frst_id = user_frst_id
        self.user_sec_id = user_sec_id

    def acceptInvite(self):
        database.session.delete(self)
        database.session.commit()


class Questions(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    quest = database.Column(database.String)
    answer1 = database.Column(database.String)
    answer2 = database.Column(database.String)
    answer3 = database.Column(database.String)
    answer4 = database.Column(database.String)
    correct_answer = database.Column(database.Integer)
    isActive = database.Column(database.Boolean, default=False)

    def __init__(self, quest, answer1, answer2, answer3, answer4, correct_answer):
        self.quest = quest
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer

    def setActive(self):
        self.isActive = True
        database.session.commit()

    def delActive(self):
        self.isActive = False
        database.session.commit()

    def getQuest(self):
        return {
            "quest": self.quest,
            "answers": {
                1: self.answer1,
                2: self.answer2,
                3: self.answer3,
                4: self.answer4,
            },
            "correct": self.correct_answer
        }
