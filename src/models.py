from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from datetime import datetime as dt
from flask_migrate import Migrate
from . import app


# instatiated and stored db and migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.ForeignKey('portfolios.id'), nullable=False)
    name = db.Column(db.String(256), index=True, unique=True)
    symbol = db.Column(db.String(256), index=True, unique=True)

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Company {}-{}>'.format(self.name, self.symbol)

class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(256), index=True, unique=True)

    companies = db.relationship('Company', backref='portfolio', lazy=True)

    dated_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Portfolio {}>'.format(self.name)

class User(db.Model):
    """
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    email = db.Column(db.String(256), index=True, nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    portfolios = db.relationship('Portfolio', backref='user', lazy=True)
    # this establishes a category to have a 'user' connection with the categories table
    # this is a one to many.  user is one to many

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def __init__(self, email, raw_pass): # password is raw password
        self.email = email
        self.password = sha256_crypt.hash(raw_pass)

    @classmethod
    def check_password_hash(cls, user, password):
        """
        """
        if user is not None:
            if sha256_crypt.verify(password, user.password):
                return True
            
        return False
