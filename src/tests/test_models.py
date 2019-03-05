from src.models import Company

class TestClass():
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
        company = Company(name='Badger Meter', symbol='BMI')
        session.add(company)
        session.commit()

        assert company.id > 0

        companies = company.query.all()

        assert len(companies) == 1
        assert companies[0] == 'Badger Meter'

    def test_create_company_again(self, session):
        company = Company(name='Badger Meter', symbol='BMI')
        session.add(company)
        session.commit()

        assert company.id > 0

        companies = company.query.all()

        assert len(companies) == 1

    def test_tc2(self):
        pass




    

