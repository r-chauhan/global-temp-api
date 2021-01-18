# flake8: noqa
# TODO: check if there is a better way
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .base import BaseModel
from .temp_data import TempData

__all__ = ['BaseModel', 'TempData']
