from console.style import Style
from console.console_logs import ConsoleLogs, socketDecorator


@socketDecorator("DISCONNECT")
def disconnectSocket():
    ConsoleLogs.PRINT(f"Client {Style.RED}disconnected{Style.ZERO}")


@socketDecorator("CONNECT")
def connectSocket():
    ConsoleLogs.PRINT(f"Client {Style.GREEN}connected{Style.ZERO}")


# @socketDecorator("DISCONNECT")
# def disconnectSocket():
#     ConsoleLogs.PRINT(f"Client {Style.RED}disconnected{Style.ZERO}")


# @socketDecorator("CONNECT")
# def connectSocket():
#     ConsoleLogs.PRINT(f"Client {Style.GREEN}connected{Style.ZERO}")

@socketDecorator("CONNECT TO ABC")
def connectedToABC():
    ConsoleLogs.PRINT("CONNECT TO |username|")
