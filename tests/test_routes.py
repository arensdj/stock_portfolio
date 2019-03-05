from src import app

def test_home_route():
    """
    Tests '/' route status code
    """
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert b'<h1>Welcome to your future!</h1>' in rv.data

def test_search_route():
    """
    Tests '/search' route status code
    """
    rv = app.test_client().get('/search')
    assert rv.status_code == 200
    assert b'<title>Flask Demo</title>' in rv.data

def test_portfolio_route_get_status(session):
    """
    Tests '/' route status code
    """
    rv = app.test_client().get('/portfolio')
    assert rv.status_code == 200
    assert b'<title>Flask Demo</title>' in rv.data

def test_search_route_post_status(session):
    """
    Tests that /search post route gives correct status
    """
    rv = app.test_client().post('/search', data={'symbol': 'GE'})
    assert rv.status_code == 302

def test_search_route_post_status_again(session):
    """
    Tests that /search post route gives correct status
    """
    rv = app.test_client().post('/search', data={'symbol': 'GE'}, follow_redirects=True)
    assert rv.status_code == 200

    

    

