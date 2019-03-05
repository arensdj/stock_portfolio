from src.models import db as _db
from src import app as _app
import pytest
import os

@pytest.fixture()
def app(request):
    """
    Function Testable Flask Application
    Instantiates an app, sets up the app, then tears it down.
    """
    _app.config.from_mapping(
        TESTING=True,
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    ctx = _app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return _app

@pytest.fixture()
def db(app, request):
    """
    Function Test Database
    """
    def teardown():
        # drop all database tables
        _db.drop_all()

        # sets the database app to input value app
        _db.app = app
        _db.create_all()

        request.addfinalizer(teardown)
        
        # returns the database
        return _db

@pytest.fixture()
def session(_db, request):
    """
    Create a new database session for testing purposes
    """
    # import pdb; pdb.set_trace()
    connection = _db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = _db.create_scoped_session(options=option)

    _db.session = session

    def teardown():
        # at the end of the current test function, undo all of the changes
        transaction.rollback()
        connection.close()
        session.remove()

        request.addfinalizer(teardown)
        return session





















# from multiprocessing import Process
# from src import server
# import pytest


# # @pytest.fixture(scope='session', autouse=True)
# @pytest.fixture(scope='session', autouse=True) # but is it 'function' ?
# def server_setup():
#     instance = server.create_server()

#     process = Process(target=instance.serve_forever)
#     process.daemon = True
#     process.start()