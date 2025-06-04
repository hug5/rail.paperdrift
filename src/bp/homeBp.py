# from sanic import Blueprint, Request, text
# from sanic import Blueprint, text
from sanic import Blueprint, Request, text, HTTPResponse, log
from sanic_ext import render

bp = Blueprint("homeBp", url_prefix="/")
# app.config.TEMPLATING_PATH_TO_TEMPLATES = "src/templates"

@bp.get("/")
async def home(request: Request) -> HTTPResponse:
    # return text(f"Hello, world!! {request.text}")
    # return text("Hello, world!!")

    log.logger.info('----- Home')

    return await render(
        # "homeHtml.jinja", context={"seq": ["three", "four"]}, status=400
        "homeHtml.jinja",
        context={"seq": ["one", "two", "three", "four"]},
        status=200,
        # return render(request, "hello.html", context={"name": "Sanic"})
        # headers: dict = None,
        headers={"what": "is", "that": "this"}
        # content_type: str = "text/html; charset=utf-8",
        # template_source: str = None, # template source code
        # app: Sanic = None

        # template_name
    )

