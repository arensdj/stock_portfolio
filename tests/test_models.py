from src.models import Company, Portfolio

class TestCompanyModel:
    """
    """
    def test_create_company(self, company):
        """
        """
        assert company.id > 0

    def test_company_name(self, company):
        """
        """
        assert company.name == 'ADT Inc.'
        
    def test_company_query(self, company):
        """
        """
        companies = Company.query.all()
        assert len(companies) == 1



class TestPortfolioModel:
    """
    """
    def test_create_portfolio(self, portfolio):
        """
        """
        assert portfolio.id > 0

    def test_portfolio_name(self, portfolio):
        """
        """
        assert portfolio.name is not None


class TestPortfolioCompanyRelationship:
    """
    """
    def test_city_has_portfolio(self):
        tech = Portfolio(name='tech')
        arbor = City(name='Arbor Realty Trust', symbol='ABR', portfolio='low risk')

        assert seattle.portfolio.name == 'tech'

    def test_portfolio_has_symbols(self):
        tech = Portfolio(name='tech')
        adt = Company(name='ADT Inc.', symbol='adt', category=tech)

        assert tech.companies[0].name == 'ADT Inc.'
        # assert rainy.cities[1].name == 'Glasgow'



# def test_create_company(session):
#     company = Company(name='Agco Corp', symbol='agco')
#     session.add(company)
#     session.commit()

#     assert company.id > 0

#     companies = company.query.all()

#     assert len(companies) == 1
#     assert companies[0] == 'ADT Inc'

# def test_create_company_again(session):
#     company = Company(name='AAR Corp', symbol='air')
#     session.add(company)
#     session.commit()

#     assert company.id > 0

#     companies = company.query.all()

#     assert len(companies) == 1





    

