# from sanic import Blueprint, Request, text
from sanic import Blueprint, Request, text, html

bp = Blueprint("loginBp", url_prefix="/login")

@bp.post("/")
async def login(request: Request):
    return text("login")
