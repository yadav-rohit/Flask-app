import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    # --Domain Settings --------------------------------#
    HTTPS_PORT = 8443
    HTTP_PORT = 8000
    INTERFACE = '0.0.0.0'
    SSL_CERTIFICATE = 'ssl/local.crt'
    SSL_KEYFILE = 'ssl/local.key'
    # --Domain Settings --------------------------------#

    # --Application Settings --------------------------------#
    SECRET_KEY = '$uP36S3c63T'
    DEBUG = True
    ACCESS_LOGFILE = 'logs/access_log'
    ERROR_LOGFILE = 'logs/error_log'
    UPLOADS_FILE = 'uploads'
    DEFAULT_FOLDER = 'static/default'
