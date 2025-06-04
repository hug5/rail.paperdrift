# from sanic import Blueprint, Request, text, HTTPResponse, log
from sanic import Blueprint, log
# from asyncmy import create_pool
from src.dbo import dbc

# from sanic_ext import render

# bp = Blueprint("middlewareBp", url_prefix="/")
bp = Blueprint("middlewareBp", url_prefix=None)





@bp.before_server_start
async def before_server_start(app, loop):

    log.logger.info('----- before server start')
    # app.ctx.db = "my db"


# @bp.listener("before_server_start")
@bp.before_server_start
async def init_pool(app, loop):
    ##
      # app.ctx.db_pool = await create_pool(
      #     host="localhost",
      #     port=3306,
      #     user="user",
      #     password="pass",
      #     db="db",
      #     minsize=1,
      #     maxsize=5,
      #     pool_recycle=60,
      #     # number of seconds after which connection is recycled, helps to deal with stale connections in pool, default value is -1, means recycling logic is disabled.

      #     # echo=True,
      #     # loop=loop
      # )

    dbo = dbc.Dbc()
    app.ctx.db_pool = await dbo.doPool_init()

    log.logger.info('----- init_pool')
    log.logger.info(f"----- {app.ctx.db_pool}")



# async def run(request: Request):
#     pool = request.app.ctx.db_pool
#     async with pool.acquire() as conn:
#       async with conn.cursor() as cursor:
#           await cursor.execute("SELECT 1")
#           ret = await cursor.fetchone()
#           assert ret == (1,)

#     pool.close()
#     await pool.wait_closed()



@bp.after_server_start
async def after_server_start(app, loop):

    # REmember that this will not show up in the console logs;
    # Will show up in the file logs only!
    log.logger.info('----- after server start')


# shutdown hook
@bp.listener("after_server_stop")
async def close_pool(app, loop):
    app.ctx.db_pool.close()
    await app.ctx.db_pool.wait_closed()






