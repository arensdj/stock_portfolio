from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime as dt
from flask_migrate import Migrate
from . import app


# instatiated and stored db and migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    symbol = db.Column(db.String(16), index=True, unique=True)

    # date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Company {}-{}>'.format(self.name, self.symbol)
