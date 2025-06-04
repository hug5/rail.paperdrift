from sanic import Blueprint, Request, text, HTTPResponse, log
# from sanic import Blueprint, text
from sanic_ext import render


bp = Blueprint("productBp", url_prefix="/product")
# group = Blueprint.group(book_bp, version=2)
# bp.config.TEMPLATING_PATH_TO_TEMPLATES = "src/templates"
# app.config.TEMPLATING_PATH_TO_TEMPLATES = "src/templates"


# @app.get("/")
# @app.post("/")

@bp.route("")
async def product(request: Request) -> HTTPResponse :
    # return text("product!!")
    log.logger.info('----- product')

    return await render(
        # "homeHtml.jinja", context={"seq": ["three", "four"]}, status=400
        "productHtml.jinja",
        context={"seq": ["three", "four"]},
        status=200
        # return render(request, "hello.html", context={"name": "Sanic"})
        # headers: dict = None,
        # content_type: str = "text/html; charset=utf-8",
        # template_source: str = None, # template source code
        # app: Sanic = None

        # template_name
    )

# @bp.before_server_start
# async def setup_db(app, loop):
#     app.ctx.db = await setup_my_db()



@bp.route("/search")
async def search(request: Request) -> HTTPResponse :
    log.logger.info('----- product/search')

    qry1 = request.query_string  # raw query string
    qry2 = request.query_args    # parsed query string as a list of tuples
    qry3 = request.args          # query string as special dictionary
    return text(f"product search!! : \n{qry1}\n{qry2}\n{qry3}")

@bp.route("/sku/<number:int>")
async def no(request: Request, number: int) -> HTTPResponse :
    return text(f"product sku: {number}")
