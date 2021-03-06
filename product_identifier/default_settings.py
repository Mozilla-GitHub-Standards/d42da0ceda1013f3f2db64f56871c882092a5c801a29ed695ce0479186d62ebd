import os


class DefaultConfig(object):
    DEBUG = True
    APPLICATION_ROOT = None
    JSONIFY_PRETTYPRINT_REGULAR = True

    ENVIRONMENT = "dev"

    SAME_DOMAIN = True

    SECRET_KEY = "moz-product-identifier-development-key"

    TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

    SQLALCHEMY_DATABASE_URI = "postgres://localhost/moz_productid"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 10

    MASTER_HANDLER_POOL_SIZE = 5

    PHANTOM_PATH = "/usr/local/bin/phantomjs"
    PHANTOM_POOL_SIZE = 5
    PHANTOM_WIDTH = 1366
    PHANTOM_HEIGHT = 768

    IMG_WIDTH = 200

    S3_BUCKET = "moz-product-id"
    S3_KEY_PREFIX = "imgs"

    REDIS = {
        "host": "localhost",
        "port": 6379,
        "db": 0,
        "password": None,
        "socket_timeout": 5,
    }
