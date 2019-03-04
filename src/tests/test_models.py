from src.models import Company

class testClass():
    @classmethod
    def setup_class(cls):
        pass
    
    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_create_company(self, session):
        company = Company(name='Blackrock', symbol='BLK')
        session.add(company)
        session.commit()

        assert company.id > 0

        companies = company.query.all()

        assert len(companies) == 1

    def test_create_company_again(self, session):
        company = Company(name='Blackrock', symbol='BLK')
        session.add(company)
        session.commit()

        assert company.id > 0

        companies = company.query.all()

        assert len(companies) == 1




    

