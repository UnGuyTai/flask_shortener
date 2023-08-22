import os


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
    SECRET_KEY = "SECRET_KEY"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
