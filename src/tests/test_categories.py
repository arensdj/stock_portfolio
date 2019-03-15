class TestCategoryModel:
    """
    """
    def test_create_portfolio(self, portfolio):
        assert portfolio.id > 0

    def test_portfolio_name(self, portfolio):
        assert portfolio.name is not None


