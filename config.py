import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bug-n4m3s-4r3-stup1d'
