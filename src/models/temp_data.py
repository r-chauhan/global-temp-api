"""Database model"""
from . import db
from .base import BaseModel
from sqlalchemy import Column, Numeric, String, BigInteger, DateTime

import datetime


class TempData(db.Model, BaseModel):
    __tablename__ = "Global_Land_Temperatures_By_City"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    dt = Column(
        DateTime,
        doc="Record date, formatted like 'YYYY-DD-MM'",
        default=datetime.datetime.utcnow,
    )
    AverageTemperature = Column(Numeric(asdecimal=True))
    AverageTemperatureUncertainty = Column(Numeric(asdecimal=True))
    City = Column(String, doc="City")
    Country = Column(String, doc="Country")
    Latitude = Column(String, doc="Latitude")
    Longitude = Column(String, doc="Longitude")
