# import mariadb
from sanic import log
from asyncmy import create_pool

# from jug.lib.f import F
# from jug.lib.gLib import G


class Dbc():

    def __init__(self):
        # self.db
        # self.pool = None
        pass


    def commit_transaction(self):
        # self.db.commit()
        pass


    def doDisconnect(self):
        pass

        # # if self.db:
        # #     self.db.close
        #     # self.db = False
        # # F.uwsgi_log("Disconnecting")
        # logger.info('Disconnecting')

        # if self.pool is not None:
        #     self.pool.close()
        #     self.pool = None
        #     # F.uwsgi_log("Disconnected")
        #     # logger.info('Disconnected')
        # # When to close connection??


    def getConfig(self):
        pass
        # return {
        #     "un"                 : G.db["un"],
        #     "pw"                 : G.db["pw"],
        #     "host"               : G.db["host"],
        #     "port"               : G.db["port"],
        #     "database"           : G.db["database"],
        #     "autocommit"         : True,
        #     "pool_name"          : "pool_1",
        #     "pool_size"          : 64,        # The max should be 64
        #     "pool_reset_connect" : False,
        #     "pool_valid_int"     : 500,       # 500 is default
        # }

        # # return config_dict

    async def doPool_init(self):

        try:
            # # app.ctx.db_pool = await create_pool(

            return await create_pool(
                host="localhost",
                port=3306,
                user="user",
                password="pass",
                db="db",
                minsize=1,
                maxsize=5,
                pool_recycle=60,
                # number of seconds after which connection is
                 # recycled, helps to deal with stale connections
                 # in pool, default value is -1, means recycling
                 # logic is disabled.
                # echo=True,
                # loop=loop
            )

            # return {
            #     "host" : "localhost",
            #     "port" : 3306,
            #     "user" : "user",
            #     "password" : "pass",
            # }

        except Exception as e:
            # <class 'asyncmy.errors.OperationalError'>
            log.logger.error(f"----- {e} : {type(e)}")
            # print(e.args)

        finally:
            log.logger.info('----- doPool_init')


    def doQuery(self, query):
        pass
        # # https://mariadb.com/docs/server/connect/programming-languages/python/example/
        # # F.uwsgi_log("Begin Query")
        # logger.info('Begin Query + get pool connection')


        # # F.uwsgi_log("get pool connection")
        # logger.info('get pool connection')
        # # Create connection pool;
        # # self.doConnect()

        # # logger.info("here 1")
        # try:
        #     # self.pool.connect()
        #     # logger.info("here 2")

        #     # self.pool.add_connection()
        #     pool_connect = self.pool.get_connection() ###


        # except mariadb.PoolError as e:
        #     # logger.info(f"Error opening connection from pool: {e}")
        #     logger.exception(f"Error opening connection from pool: {e}")
        #     self.pool.add_connection()
        #     pool_connect = self.pool.get_connection() ###

        #     # self.doDisconnect()
        #     # self.doConnect()
        #     # self.pool.add_connection()
        #     # pool_connect = self.pool.get_connection()

        # except Exception as e:
        #     # logger.error(f"Error {e}")
        #     logger.exception(f"dbc Error: {e}")



        #     self.doDisconnect()
        #     self.doConnect()
        #     self.pool.add_connection()
        #     pool_connect = self.pool.get_connection()


        # # logger.info("here 3")
        # # instantiate the cursor
        # # curs = self.db.cursor()
        # curs = pool_connect.cursor()

        # # pool_connect.begin()

        # # https://mariadb-corporation.github.io/mariadb-connector-python/cursor.html
        # # curs.prepared = True
        #   # Not sure if you really need this?

        # # result = curs.execute(query)
        # # The result itself doesn't seem to be iterable; have to put into list??
        # # I guess it doesn't really return anything??

        # logger.info("run query")

        # # Run the query;
        # # query  = "SELECT ARTICLENO, HEADLINE, BLURB FROM ARTICLES"
        # curs.execute(query)

        # # pool_connect.commit()
        # # pool_connect.rollback()

        # ##
        #   resultList = []

        #   # Prepare result:

        #   # Method 1
        #   for (ARTICLENO, HEADLINE, BLURB) in cur:
        #       resultList.append(f"{first_name} {last_name} <{email}>")

        #       This should put everything in a list as a single string;
        #       Could also use this method to create a dictionary; with the field name as the index;

        #   # Method 2
        #   for row in curs:
        #       # arr.append(f"{row}")  # This would probably be like above;
        #       resultList.append(row)
        #       # This should create multidimensional list;
        #       # Each field is a separate list item;

        #   # for (first_name, last_name) in cur:
        #   #     print(f"First Name: {first_name}, Last Name: {last_name}")


        # cc = self.pool.connection_count
        # ps = self.pool.pool_size
        # logger.info(f"connection count: {cc}, pool size: {ps}")

        # pool_connect.close()

        # ###
        #   # # cc = self.pool.connection_count
        #   # # ps = self.pool.pool_size
        #   # # F.uwsgi_log(f"connection count2: {cc}")
        #   # # F.uwsgi_log(f"pool size2: {ps}")

        #   # # for x in range(10000000):
        #   # #     y = "hello"

        #   # logger.info(f"resultList: {resultList}")
        #   # # self.doDisconnect()
        #   # return resultList

        # return curs


    async def doQuery(self, request, query):

        query = "SELECT * FROM mytable"
        # query = "UPDATE accounts SET balance = balance - 100 WHERE user_id = 1"
        # query = "INSERT INTO users (name) VALUES ('Alice')")
        try:
            async with request.app.ctx.db_pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await conn.begin() # Start transaction
                    try:
                        await cursor.execute(query)
                        # await cursor.execute(query)
                          # Could execute multiple queries
                        result = await cursor.fetchall()
                        # return response.json({"data": result})
                        await conn.commit()  # If all went well, commit changes
                        return result
                        # return json({"result": result})

                    except Exception:
                        await conn.rollback()
                          # If anything fails, rollback changes
                        raise
                          # Optionally re-raise for upstream handling
                    finally:
                        pass
                        # conn.close() # not needed

        except asyncmy.OperationalError as e:
        # except OperationalError as e:
            pass
            # Rather than using a connection validation hook, can also catch errors:
            # Validation hooks are nice to have, but not necessary for most sane apps
        except Exception as e:
            pass




    def doConnect_old(self):
        pass
        # '''
        #   I am still not convinced about this whole pool things;
        #   I don't see the benefits in this; even if there is a marginal
        #   benefit, it's going to be very very tiny, I suspect; and not
        #   worth the trouble we're seeing here;

        # '''

        # pool_conf = self.getConfig()

        # logger.info("Connecting")

        # try:
        #     # logger.info("begin try connect")

        #     self.pool = mariadb.ConnectionPool(
        #         pool_name = pool_conf["pool_name"],
        #         pool_size = pool_conf["pool_size"],
        #         pool_reset_connection = pool_conf["pool_reset_connect"],
        #         pool_validation_interval = pool_conf["pool_valid_int"]
        #     )
        #     self.pool.set_config(
        #         user = pool_conf["un"],
        #         password = pool_conf["pw"],
        #         # host = host,
        #         port = pool_conf["port"],
        #         database = pool_conf["database"],
        #         # protocol = "SOCKET",
        #         autocommit = pool_conf["autocommit"],
        #     )

        #     # Create an initial connection pool slot
        #     # If we free up after every query, should be able to reuset his repeatedly and never exceed connection_count=1
        #     # Might need more if there are simultaneous connections?
        #     self.pool.add_connection()

        #     # logger.info("end try connect")
        #     logger.info("Connected")

        # except mariadb.Error as e:
        #     # print(f"Error connecting to mariadb: {e}")
        #     # return e
        #     logger.exception(f"dbc Error: {e}")
        # finally:
        #     pass


