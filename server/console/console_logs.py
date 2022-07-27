from datetime import datetime
from console.style import Style
import os

dasher = f"|"


def info_prefer(string):
    date = datetime.now()
    date = date.strftime("%H:%M:%S")
    txt = f"{string}{Style.WHITE_BG} {date} {Style.ZERO}{dasher}"
    return txt


class ConsoleLogs():

    def START():
        os.system('CLS')
        print(f"{Style.VIOLET_BG} DONE {Style.ZERO} {Style.VIOLET}Compiled successfully{Style.ZERO}\n\n  {Style.BOLD}Running at:{Style.ZERO}\n  {Style.BOLD}- Local:{Style.ZERO} {Style.BLUE}http://localhost:{Style.BOLD}5000{Style.ZERO}{Style.BLUE}/{Style.ZERO}\n  {Style.BOLD}- Network:{Style.ZERO} {Style.BLUE}http://127.0.0.1:{Style.BOLD}5000{Style.ZERO}{Style.BLUE}/{Style.ZERO}\n")

    def SERVER(name):
        print(info_prefer(f"{Style.BLUE_BG} SERVER {Style.ZERO}{dasher}") +
              f"{Style.VIOLET_BG} {name} {Style.ZERO}|")

    def SOCKETS(name):
        print(info_prefer(f"{Style.GREEN_BG} SOCKETS {Style.ZERO}{dasher}") +
              f"{Style.VIOLET_BG} {name} {Style.ZERO}|")

    def ERROR(name):
        print(info_prefer(f"{Style.RED_BG} ERROR {Style.RED_BG}{dasher}") +
              f"{Style.VIOLET_BG} {name} {Style.ZERO}|")

    def PRINT(string):
        tb = "  "
        print(tb + string)

    def END():
        # varid = 1
        print("")
