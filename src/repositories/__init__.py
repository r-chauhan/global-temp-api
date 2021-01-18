from flask_sqlalchemy import SQLAlchemy
from .temp_data import TempRepository


db = SQLAlchemy()
__all__ = ['TempRepository']
