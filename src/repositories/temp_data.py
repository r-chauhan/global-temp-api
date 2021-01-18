from sqlalchemy.exc import IntegrityError
import sqlalchemy as sa
from sqlalchemy.sql.expression import literal_column
from exceptions import ResourceExists
from flask import jsonify
from models import TempData, db


class TempRepository:
    @staticmethod
    def get(year: str) -> dict:
        """ Query a row by date format: YYYY/MM/DD """
        temp: dict = {}
        query = TempData.query.filter(TempData.dt >= year).cte("query")

        MAX_AVG = sa.func.max(
            sa.func.coalesce(query.c.AverageTemperature, literal_column("0"))
        )

        temp = (
            sa.select(
                [
                    query.c.id,
                    query.c.dt,
                    MAX_AVG.label("maxAverage"),
                    query.c.AverageTemperatureUncertainty,
                    query.c.City,
                    query.c.Country,
                    query.c.Latitude,
                    query.c.Longitude,
                ]
            )
            .group_by(
                query.c.id,
                query.c.dt,
                query.c.AverageTemperatureUncertainty,
                query.c.City,
                query.c.Country,
                query.c.Latitude,
                query.c.Longitude,
            )
            .order_by(MAX_AVG.desc())
            .select_from(query)
            .limit(literal_column("1"))
        )

        result = db.session.execute(temp).fetchall()

        response = [
            {
                "id": str(row.id),
                "avgTemp": str(row.maxAverage),
                "avgTempUncertainty": str(row.AverageTemperatureUncertainty),
                "date": str(row.dt),
                "city": str(row.City),
                "country": str(row.Country),
                "latitude": str(row.Latitude),
                "longitude": str(row.Longitude),
            }
            for row in result
        ]
        return response

    @staticmethod
    def create(
        avg_temp: float, avg_temp_uncertainty: float, city: str, country: str, lat: str, lon: str
    ) -> dict:
        """ Create row """
        result: dict = {}
        try:
            temp = TempData(
                AverageTemperature=avg_temp,
                AverageTemperatureUncertainty=avg_temp_uncertainty,
                City=city,
                Country=country,
                Latitude=lat,
                Longitude=lon,
            )
            temp.save()
            result = {
                "id": str(temp.id),
                "avgTemp": str(temp.AverageTemperature),
                "avgTempUncertainty": str(temp.AverageTemperatureUncertainty),
                "dt": str(temp.dt),
                "city": str(temp.City),
                "country": str(temp.Country),
                "latitude": str(temp.Latitude),
                "longitude": str(temp.Longitude)
            }
        except IntegrityError:
            TempData.rollback()
            raise ResourceExists("row already exists")

        return result

    def update(id: int, avg_temp: float) -> dict:
        """ Update row """
        result: dict = {}
        try:
            temp = TempData(id=id, AverageTemperature=avg_temp)
            temp.update()
            result = {
                "id": str(temp.id),
                "avgTemp": str(temp.AverageTemperature),
                "avgTempUncertainty": str(temp.AverageTemperatureUncertainty),
                "dt": str(temp.dt),
                "city": str(temp.City),
                "country": str(temp.Country),
                "latitude": str(temp.Latitude),
                "longitude": str(temp.Longitude)
            }
        except IntegrityError:
            TempData.rollback()
            # raise ResourceExists("row unaltered")

        return result