from ..models import User  #relative path to models.py file


class TestUserModel:
    """
    """
    def test_user_create(self, user):
        assert users.id > 0

    def test_user_email(self, user):
        assert user.email == 'default@example.com'

    def test_user_check_password(self, user):
        # from src.models import User  # this import just for this test
        assert User.check_password_hash(user, 'secret')

    def test_password_check(self, user):
        assert User.check_password_hash(user, 'secret')