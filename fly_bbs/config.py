# coding=utf-8

import os
from flask_uploads import ALL


class Dev:
    MONGO_URI = "mongodb://127.0.0.1:27017/pyfly"
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PROT = 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'YOUNGAIT@163.com'
    MAIL_PASSWORD = '99liu12feng31'
    MAIL_DEBUG = True
    MAIL_SUBJECT_PREFIX = '[YoungAI]-'
    WTF_CSRF_ENABLED = False
    UPLOADED_PHOTOS_ALLOW = ALL
    UPLOADED_PHOTOS_DEST = os.path.join(os.getcwd(), 'uploads')
    UPLOADED_FILES_DEST = os.path.join(os.getcwd(), 'uploads')
    WHOOSH_PATH = os.path.join(os.getcwd(), 'whoosh_indexes')

    # USE_CACHE = True
    # CACHE_TYPE = 'redis'
    # CACHE_REDIS_HOST = '127.0.0.1'
    # CACHE_REDIS_PORT = 6379
    # CACHE_REDIS_PASSWORD = ''
    # CACHE_REDIS_DB = '0'


class Pud:
    pass

config = {
    "Dev": Dev,
    "Pud": Pud
}