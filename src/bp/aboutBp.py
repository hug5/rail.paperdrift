# from sanic import Blueprint, Request, text
from sanic import Blueprint, Request, text, html

bp = Blueprint("aboutBp", url_prefix="/about")

@bp.get("/")
async def about(request: Request):
    # return text(f"Hello, world!! {request.text}")
    # return html("<b>about page</b>")
    message = (
        request.head + b" \nBegin Body \n" + request.body + b" \nEnd Body\n"
    ).decode("utf-8")
    # print(message)
    return html(message)
    # return html((request.head).decode("utf-8"))
