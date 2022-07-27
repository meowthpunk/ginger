from flask_socketio import SocketIO
from backend import server
from console.console_logs import ConsoleLogs
from console.style import Style


socket = SocketIO(server, cors_allowed_origins="*")


@socket.event
def template():
    ConsoleLogs.SOCKETS('TEMPLATE')
    ConsoleLogs.PRINT(f"Template event catched")
    ConsoleLogs.END()
    # Template event catched\n
    # socket.emit("test_listen")


@socket.event
def connect():
    ConsoleLogs.SOCKETS('CONNECT')
    ConsoleLogs.PRINT(f"Client {Style.GREEN}connected{Style.ZERO}")
    ConsoleLogs.END()


@socket.event
def disconnect():
    ConsoleLogs.SOCKETS('DISCONNECT')
    ConsoleLogs.PRINT(f"Client {Style.RED}disconnected{Style.ZERO}")
    ConsoleLogs.END()
