from src import app
from flask import session


def test_home_route():
    """
    Tests '/' route status code
    """
    rv = app.test_client().get('/')
    assert rv.status_code == 200

def test_home_route_title():
    rv = app.test_client().get('/')
    assert b'<h1>Welcome to the site</h1>' in rv.data

def test_search_route():
    """
    Tests '/search' route status code
    """
    rv = app.test_client().get('/search')
    assert rv.status_code == 200
    assert b'<title>Flask Demo</title>' in rv.data
    # assert b'<h2>Search for companies</h2>' in rv.data

def test_portfolio_route_get_status(session):
    """
    Tests '/' route status code
    """
    rv = app.test_client().get('/portfolio')
    assert rv.status_code == 200
    # assert b'<title>Flask Demo</title>' in rv.data

def test_portfolio_route_get_welcome_message():
    rv = app.test_client().get('/portfolio')
    assert b'<h2>Welcome to the Portfolio</h2>' in rv.data

def test_search_route_post_status(session):
    """
    Tests that /search post route gives correct status
    """
    rv = app.test_client().post('/search', data={'symbol': 'GE'})
    assert rv.status_code == 200
    # assert rv.status_code == 302

def test_search_route_post_status_again(session):
    """
    Tests that /search post route gives correct status
    """
    rv = app.test_client().post('/search', data={'symbol': 'GE'}, follow_redirects=True)
    assert rv.status_code == 200

def test_unknown_route_status(self, client):
    res = client.get('/does_not_exist')
    assert res.status_code == 404
    assert b'<h1>404 - Page Not Found</h1' in res.data
