import abc
from socialogin.models import User


class Repository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_user(
            self,
            id: int,
            social: str
    ):
        pass

    @abc.abstractmethod
    def create_user(
            self,
            username: str,
            access_token: str,
            social: str,
            email: str,
            id: int,
            refresh_token=None
        ):
        pass

    @abc.abstractmethod
    def update_user_token(
            self,
            username: str,
            access_token: str,
            social: str,
            email: str,
            id: int,
            refresh_token=None
        ):
        pass


class UserRepository(Repository):
    def get_user(
            self,
            id: int,
            social: str
    ):
        user = User.objects.filter(social_id=id, social_site=social)

        return user

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

        user.save()

        return user

    def update_user_token(
            self,
            username: str,
            access_token: str,
            social: str,
            email: str,
            id: int,
            refresh_token=None
        ):
        user = User.objects.get(social_id=id, social_site=social)

        user.access_token = access_token,

        user.refresh_token = refresh_token

        user.save()

        return user
