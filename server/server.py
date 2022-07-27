from console.console_logs import ConsoleLogs
from sockets import socket
from backend import server


if __name__ == "__main__":
    ConsoleLogs.START()
    socket.run(server)
