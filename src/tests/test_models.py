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
    def test_company_has_portfolio(self):
        tech = Portfolio(name='tech')
        arbor = Company(name='Arbor Realty Trust', symbol='ABR', portfolio='low risk')

        assert seattle.portfolio.name == 'tech'

    def test_portfolio_has_symbols(self):
        tech = Portfolio(name='tech')
        adt = Company(name='ADT Inc.', symbol='adt', category=tech)

        assert tech.companies[0].name == 'ADT Inc.'
        # assert rainy.cities[1].name == 'Glasgow'

class TestUserModel:
    """
    """
    def test_user_create(self, user):
        """
        """
        assert users.id > 0

    def test_user_email(self, user):
        """
        """
        assert user.email == 'default@domain.com'

    def test_user_check_password(self, user):
        """
        """
        from src.models import User
        assert User.check_password_hash(user, 'password')
        

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





    

