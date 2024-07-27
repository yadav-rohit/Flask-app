from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler
# import config

app = Flask(__name__)

# Configure logging
app.config.from_object('config.Config')
# print('Configuring',config.Config["ACCESS_LOGFILE"])
logfile = app.config["ACCESS_LOGFILE"]
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

loghandler = RotatingFileHandler(logfile, maxBytes=1000000, backupCount=5)
logger.addHandler(loghandler)
logger.removeHandler(default_handler)

import website.views as views