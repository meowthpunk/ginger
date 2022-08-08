from models import Questions, database
import random
import threading
import time
from sockets import socket

# pizda = database.session.query(Questions).all()

# print(len(pizda))


def getQuest():
    questions = database.session.query(Questions).all()
    return questions[random.randint(0, len(questions)-1)]


def setQuestsZero():
    questions = database.session.query(Questions).filter(
        Questions.isActive == True).all()
    for quest in questions:
        quest.delActive()

# for i in range(1000):
#     print(getQuest())


def ping_in_intervals():
    threading.Timer(30.0, ping_in_intervals).start()
    print("start-quest")
    setQuestsZero()
    quest = getQuest()
    quest.setActive()
    info = quest.getQuest()
    socket.emit("rand_quest", {"data": info}, namespace="/auth")
    time.sleep(20)
    print("stop-quest")
    socket.emit("rand_quest_answ", {"data": "data"}, namespace="/auth")
    print(f"Высираю ответ: {info['answers'][info['correct']]}")


# ping_in_intervals()

# setQuestsZero()


# quest = getQuest()
# info = quest.getQuest()

# print(info)
# print(info["answers"][4])
# getQuest
