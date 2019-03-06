from src.models import Company

# class TestClass():
#     @classmethod
#     def setup_class(cls):
#         pass
    
#     @classmethod
#     def teardown_class(cls):
#         pass

#     def setup_method(self, method):
#         pass

#     def teardown_method(self, method):
#         pass

def test_create_company(session):
    company = Company(name='ADT Inc', symbol='adt')
    session.add(company)
    session.commit()

    assert company.id > 0

    companies = company.query.all()

    assert len(companies) == 1
    # assert companies[0] == 'ADT Inc'

def test_create_company_again(session):
    company = Company(name='General Electric Company', symbol='ge')
    session.add(company)
    session.commit()

    assert company.id > 0

    companies = company.query.all()

    assert len(companies) == 1





    

