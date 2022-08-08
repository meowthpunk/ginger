from console.console_logs import ConsoleLogs
from console.style import Style
from flask import Blueprint

server_views = Blueprint('book_routes', __name__)


@server_views.route("/")
def home():
    ConsoleLogs.SERVER('HOME')
    ConsoleLogs.PRINT(f"Connected {Style.GREEN}succes{Style.ZERO}")
    ConsoleLogs.END()
    return {"ok": True, "wasd": 4}
