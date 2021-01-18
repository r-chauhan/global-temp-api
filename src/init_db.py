import pandas as pd
from models import temp_data
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from utils import get_env_variable


DEFAULT_DB_URI = get_env_variable("DEFAULT_DB_URI")


class TempsDB:
    def __init__(self, uri=DEFAULT_DB_URI):
        self.engine = create_engine(uri, encoding="utf-8", echo=True)

        self.Session = sessionmaker(bind=self.engine)

    def make_session(self):
        return self.Session()


db = TempsDB()


def load_data(filename, Model):
    print(f"Loading: {Model}")
    session = db.make_session()

    chunk_size = 500
    for chunk in pd.read_csv(filename, chunksize=chunk_size, iterator=True):
        chunk.to_sql(
            Model.__tablename__,
            db.engine,
            if_exists="append",
            schema="public",
            index=False,
            method="multi",
        )

    session.commit()


if __name__ == "__main__":
    load_data("./src/data/GlobalLandTemperaturesByCity.csv", temp_data.TempData)
