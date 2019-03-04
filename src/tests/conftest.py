from src.models import db as _db
from src import app as _app
import pytest
import os

@pytest.fixture()
def app(request):
    """
    Function Testable Flask Application
    """
    _app.config.from_mapping(
        TESTING=True,
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    ctx=














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