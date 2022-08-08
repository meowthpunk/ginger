from console.console_logs import ConsoleLogs
from sockets import socket
from config import server
from models import database
from test import ping_in_intervals


# def ping_in_intervals():
#     threading.Timer(1.0, ping_in_intervals).start()
#     print("send ping")
#     socket.emit("rand_quest", {"data": "data"}, namespace="/auth")


host = "192.168.0.101"
port = 5000

if __name__ == "__main__":
    ping_in_intervals()
    ConsoleLogs.START(host, port)
    database.create_all()
    socket.run(server, host, port)
