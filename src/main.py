from flask_restful import Api
from resources import HealthCheck, UserList, User, TempData, TempAdd, TempUpdate
from models import User as UserModel, db
from flask_migrate import Migrate
from app import create_app


app = create_app()
migrate = Migrate(app, db)


# API
api = Api(app)
api.add_resource(HealthCheck, "/healthcheck")
api.add_resource(TempData, "/api/avg_temp_since_date/<string:year>")
api.add_resource(TempAdd, "/api/add_temp")

# CLI for migrations
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=UserModel)
