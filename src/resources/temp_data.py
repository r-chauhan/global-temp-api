from flask import request, jsonify
from flask_restful import Resource

from repositories import TempRepository


class TempData(Resource):
    def get(self, year: str):
        try:
            temp = TempRepository.get(year)
            return temp, 200
        except Exception as e:
            return ("Not found", 404)


class TempAdd(Resource):
    def post(self):
        """
        Create row
        """
        request_json = request.get_json(silent=True)
        avg_temp: float = request_json["avg_temp"]
        avg_temp_uncertainty: float = request_json.get("avg_temp_uncertainty")
        city: str = request_json["city"]
        country: str = request_json.get("country")
        lat: str = request_json["lat"]
        lon: str = request_json.get("lon")
        try:
            temp = TempRepository.create(
                avg_temp, avg_temp_uncertainty, city, country, lat, lon
            )
            return temp, 200
        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response


class TempUpdate(Resource):
    def patch(self):
        """
        Update row based on id
        """
        request_json = request.get_json(silent=True)
        id: str = request_json["id"]
        avg_temp: str = request_json.get("avg_temp", "")
        try:
            temp = TempRepository.update(id, avg_temp)
            return temp, 200
        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response
