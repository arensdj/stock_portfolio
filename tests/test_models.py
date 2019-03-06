from src.models import Company

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





    

