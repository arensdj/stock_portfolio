from  ..models import Portfolio

def test_create_portfolio(authenticated_client):
    data = {'name': 'pasta'} #category name
    res = authenticated_client.post('/portfolio', data=data, follow_redirects=True)
    assert res.status_code == 200
    assert b'<title>Search</title>' in res.data

    # but do you want to make sure that category made it to the database?
    # check that category was properly persisted into the database
    # can check that there is one category using ORM
    categories = Category.query.all()
    assert len(categories) == 1

def test_category_count_again(authenticated_client, user):
    data = {'name': 'nuts'} #category name
    res = authenticated_client.post('/postfolio', data=data, follow_redirects=True)
    assert res.status_code == 200
    assert b'<title>Search</title>' in res.data
    categories = Category.query.all()
    assert len(categories) == 1

# test that category is associated with user
def test_category_count_again(authenticated_client):
    data = {'name': 'nuts'} #category name
    res = authenticated_client.post('/postfolio', data=data, follow_redirects=True)
    nuts = Category.query.first()
    assert nuts.user.email == 'default@example.com'
    # 'user' is the backref in the models.py file

    # Categories has many cities
    assert len(nuts.cities) == 0

# sometimes you want to test models directly
