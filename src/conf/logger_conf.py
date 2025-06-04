
# // 2025-05-30 Fri 13:55
# This is imported by serv.py
# Uses below configuation setting for logger;

# Logger alert levels:
  # debug
  # info
  # warning
  # error
  # critical
  # If you set to debut, then anything above debug is caught;
  # If you set to error, then only error and above are caught;



# Notes:
  # These config comes from the default sanic logger;
  # The trouble is that I'm gonna forget everything if I don't write
   # almost everything down! But don't feel like doing that!
  # I think I used a combination of the default sanic logger config
   # settings, suggestions by AI, and settings I had used in Flask;
  # You can either use the default Sanic, but that doesn't write to file;
  # Or you can import Sanic settings and modify it; but that seems to
   # be even more trouble than just writing a clean config like this;


#-----------------------------------------------------------


LOG_CONFIG = {
  'version': 1,
  'disable_existing_loggers': False,

  # Sanic omits the top level root logger
  # Or maybe it writes it in behidn the scenes in its module
  # "root": {
  #     "level": "DEBUG",
  #     "handlers": [
  #         "console",
  #         "debug_log_file"
  #     ]
  # },

  'loggers': {
      'sanic.root': {
          'level': 'INFO',
          'handlers': ['console', 'debug_log_file']
      },
      'sanic.error': {
          'level': 'DEBUG',
          'handlers': ['error_console', 'error_log_file', 'debug_log_file'],
          'propagate': False,  # Whether to propagate to root logger
          # 'qualname': 'sanic.error'
      },
      'sanic.access': {
          'level': 'DEBUG',
          'handlers': ['access_console', 'debug_log_file'],
          'propagate': False,
          # 'qualname': 'sanic.access'
      },
      'sanic.server': {
          'level': 'DEBUG',
          'handlers': ['console', 'debug_log_file'],
          'propagate': False,
          # 'qualname': 'sanic.server'
      },
      'sanic.websockets': {
          'level': 'INFO',
          'handlers': ['console', 'debug_log_file'],
          'propagate': False,
          # 'qualname': 'sanic.websockets'
      }
  },
  'handlers': {
      'console': {
          'class': 'logging.StreamHandler',
          'formatter': 'generic',
          # 'stream': "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>"
          'stream': 'ext://sys.stdout',
      },
      'error_console': {
          'class': 'logging.StreamHandler',
          'formatter': 'generic',
          # 'stream': "<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>"
          'stream': 'ext://sys.stderr',
      },
      'access_console': {
          'class': 'logging.StreamHandler',
          'formatter': 'access',
          # 'stream': "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>"
          'stream': 'ext://sys.stdout',
      },

      'debug_log_file': {
          # 'class': 'logging.handlers.TimedRotatingFileHandler',
          "class": "logging.FileHandler",
          # 'level': 'INFO',
          'formatter': 'generic',
          'filename': 'etc/log/sanic_debug.log',
          # 'when': 'midnight',
          # 'interval': 1,
          # 'backupCount': 7,
      },
      'error_log_file': {
          "class": "logging.FileHandler",
          'formatter': 'generic',
          'filename': 'etc/log/sanic_error.log',
      },


  },

  # This is the default sanic formatter
  'formatters': {
      'generic': {'class': 'sanic.logging.formatter.AutoFormatter'},
      'access': {'class': 'sanic.logging.formatter.AutoAccessFormatter'}
  }

  # 'formatters': {
  #     'generic': {
  #         'format': '[%(asctime)s] [%(levelname)s] [%(process)d] %(message)s',
  #         'datefmt': '%Y-%m-%d %H:%M:%S %z',
  #     },
  # },
  #
  # Belowis the formatter I used in flask:
  # 'formatter1': {
  #   "format": "{levelname} : {message} | {module}:{lineno} | {asctime}",
  #   "style": "{"
  #   # For this style {, must denote the style;
  # },
  # 'formatter2': {
  #   # 'format': '%(levelname)s : %(message)s | %(module)s:%(lineno)s | %(asctime)s',
  #   'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
  #   # "style": "%"
  #   # For this % format, style appears to be optional
  # }

}
  