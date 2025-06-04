# from sanic.response import text, html
from sanic import Sanic, Request, text, html, log

# from sanic.log import logger, error_logger, LOGGING_CONFIG_DEFAULTS
  # avoid using: access_logger, server_logger, websockets_logger
  # Okay using: logger (root), error_logger
from src.conf.logger_conf import LOG_CONFIG
  # Import log configuration

# Blueprint
from src.bp.homeBp import bp as homeBp
from src.bp.productBp import bp as productBp
from src.bp.aboutBp import bp as aboutBp
from src.bp.loginBp import bp as loginBp
from src.bp.middlewareBp import bp as middlewareBp
from src.conf.static_routes import static_routes

# How can I make imports not dependent on from where the application is called??

# homeCtl
# homeRte

##
  # class Startup():

  #     def __init__(self):
  #         # app = Sanic("MyHelloWorldApp")
  #         # self.app = Sanic(__name__)
  #         # self.app = Sanic(__file__)
  #         pass

  #     def doInit(self):
  #         self.app = Sanic("NewSanicServer")
  #         # self.app.blueprint(bp_home, bp_product, bp_about)
  #         self.app.blueprint(bp_home)
  #         self.app.blueprint(bp_product)
  #         self.app.blueprint(bp_about)

  #         # @self.app.get("/")
  #         # async def home(request: Request):
  #         #     # return text(f"Hello, world!! {request.text}")
  #         #     return text("Hello, world!!")

  #         # @self.app.post("/about/")
  #         # async def about(request: Request):
  #         #     # return text(f"Hello, world!! {request.text}")
  #         #     # return html("<b>about page</b>")
  #         #     message = (
  #         #         request.head + b" \nBegin Body \n" + request.body + b" \nEnd Body\n"
  #         #     ).decode("utf-8")
  #         #     # print(message)
  #         #     return html(message)
  #         #     # return html((request.head).decode("utf-8"))

  #         return self.app

  # app = Startup().doInit()



# I think this runs with the blueprint files;
# init is a bad name!

# def doServ():



# Extend default logging config to add file handler
# LOG_CONFIG = log.LOGGING_CONFIG_DEFAULTS.copy()  # Copy default config
# LOG_CONFIG['handlers']['file'] = {
#     'class': 'logging.handlers.TimedRotatingFileHandler',
#     'level': 'INFO',
#     'formatter': 'generic',  # Reuse Sanic's default formatter
#     'filename': 'etc/log/sanic.log',
#     'when': 'midnight',
#     'interval': 1,
#     'backupCount': 7,
# }
print("---------------------------------------------------")
print(LOG_CONFIG)
print("---------------------------------------------------")
# LOG_CONFIG['version'] = 1
# LOG_CONFIG['loggers']['sanic.root']['handlers'].append('file')
# LOG_CONFIG['loggers']['sanic.access']['handlers'].append('file')




app = Sanic(
    "NewSanicServer",
    strict_slashes = True,
    # configure_logging=True,
    log_config=LOG_CONFIG
)


# Just modify the default
# from sanic.log import LOGGING_CONFIG_DEFAULTS
# LOGGING_CONFIG_DEFAULTS['formatters']['generic']['class'] = 'sanic.logging.formatter.ProdFormatter'
# LOGGING_CONFIG_DEFAULTS['formatters']['access']['class'] = 'sanic.logging.formatter.ProdAccessFormatter'
# app = Sanic('NewSanicServer', log_config=LOGGING_CONFIG_DEFAULTS)

# Create your own logging config
# app = Sanic('NewSanicServer', log_config=LOGGING_CONFIG)




# print(app.logger)
# Output: <Logger sanic.MyApp (DEBUG)>


# app.config.REQUEST_TIMEOUT = 60  # Request timeout in seconds
# app.config.RESPONSE_TIMEOUT = 60  # Response timeout
app.config.KEEP_ALIVE = True  # Enable HTTP keep-alive
app.config.KEEP_ALIVE_TIMEOUT = 5  # Keep-alive timeout (seconds)
# app.config.ACCESS_LOG = True  # Enable access logs
# app.config.GRACEFUL_SHUTDOWN_TIMEOUT = 15.0  # Shutdown timeout
# app.config.REQUEST_MAX_SIZE = 100_000_000  # Max request size (bytes)
# app.config.REQUEST_BUFFER_QUEUE_SIZE = 100  # Request buffer queue
# app.config.FALLBACK_ERROR_FORMAT = "json"  # Default error format

# app.config.load(path="settings.py")  # or .env, or .json

# app.config.NAME = "NewSanicServer"
# app.config.STRICT_SLASHES = True
# For multiple directories:
# app.ext.config.templating_path_to_templates = ["base_templates", "user_templates"]
# app.config.TEMPLATING_PATH_TO_TEMPLATES = ["src/html", "src/html2"]
app.config.TEMPLATING_PATH_TO_TEMPLATES = "src/html"
# app.static("static", "/path/to/static/files", name="static")
# app.config.ROOT_DIR = "src/www/static"  ?? fake?
# https://sanic.dev/en/plugins/sanic-ext/logger.html#logging
app.config.LOGGING = True  # True=Enable background logger extension; default False;
app.config.LOGGING_QUEUE_MAX_SIZE = 4096 # this is default
app.config.LOG_LEVEL = "DEBUG"


# Extend(app)

# To use this idiom, must import Config
# https://sanic.dev/en/plugins/sanic-ext/configuration.html#background-logger
# from sanic_ext import Config
# app.extend(config=Config(
#     TEMPLATING_PATH_TO_TEMPLATES = "src/html",
#     LOGGING = True,
#     LOGGING_QUEUE_MAX_SIZE = 4096, # this is default
#     LOG_LEVEL = "INFO"
# ))





# app.blueprint(bp_home, bp_product, bp_about)
app.blueprint(homeBp)
app.blueprint(productBp)
app.blueprint(aboutBp)
app.blueprint(loginBp)
app.blueprint(middlewareBp)

# logger = logging.getLogger('sanic.root')
# error_logger = logging.getLogger('sanic.error')
  # Note that we don't explicitly do a 'getLogger';
  # So presumably, sanic is doing this behind the scenes for us;
  # log.logger should be mapped to sanic.root;
  # log.error_logger should be mapped to sanic.error;
  # And etc for others;


log.logger.info('////// doServ')
log.logger.info('------ doServ')
log.error_logger.error('xxxxxxxxx This is the error logger message')
log.logger.error('------ my error')


# Avoid using these directly:
# server_logger.info('This is the server logger message')
# access_logger.info('xxxxxxxxx This is the access logger message')
# websockets_logger.info('xxxxxxx This is the websockets logger message')


# Set up static routes
static_routes(app)

log.logger.info('====== Application ready!')




#---------------------------------------------------------


# query string
# http https://api.github.com/search/repositories q==httpie per_page==1
# form post
# http -f POST pie.dev/post hello=World

# json
# http PUT pie.dev/put name=John email=john@example.org


#---------------------------------------------------------

# For development mode:
#
# From inside rail.paperdrift folder, but outside src dir:
# $ sanic src.serv -w2 --dev
# $ sanic src.serv -w2 --port 8000 --dev
# $ sanic src.serv --port 8000 --dev --workers 2
# $ sanic src.serv -p 8000 -dw 2

# If terminal gets stuck on ctrl-c, then do:
#
# $ reset

# Production:
#
# $ sanic src.serv --no-access-log
  # you want no debug, no access log for production
  # https://sanic.dev/en/guide/best-practices/logging.html#logging


#---------------------------------------------------------

# https://httpie.io/docs/cli/request-url
# app.run(port=8000, debug=True)


# http POST 127.0.0.1:8000/about/ food:bar
  # with header?
# http POST 127.0.0.1:8000/about/ food=bar
  # post with body;
# http 127.0.0.1:8000/about/ food=bar
  # post is optional when there is body;

# http https://api.github.com/search/repositories q==httpie per_page==1
  # Parameter string
  # This is equivalent to:
  # GET /search/repositories?q=httpie&per_page=1 HTTP/1.1