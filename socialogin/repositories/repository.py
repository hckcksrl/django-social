import abc
from socialogin.models import User


class Repository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_user(self):
        pass

    @abc.abstractmethod
    def create_user(self,
            username: str,
            access_token: str,
            social: str,
            email: str,
            id: int,
            refresh_token=None
        ):
        pass

    @abc.abstractmethod
    def update_user_token(self):
        pass


class UserRepositorty(Repository):
    def get_user(self):
        pass

    def create_user(self):
        pass

    def update_user_token(self):
        pass


class UserRepository(Repository):
    def get_user(self):
        pass

    def create_user(self,
            username: str,
            access_token: str,
            social: str,
            email: str,
            id: int,
            refresh_token=None
        ):
        user = User(
            username=username,
            access_token=access_token,
            social_site=social,
            social_id=id,
            email=email,
            refresh_token=refresh_token
        )
