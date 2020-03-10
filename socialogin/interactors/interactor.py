import requests

from socialogin.helpers import JsonToken, InvalidCodeException, InvalidTokenException
from .social import FaceBook, Kakao
from socialogin.repositories import UserRepository


class LoginInteractor:
    def __init__(self):
        self.repository = UserRepository()


class FaceBookLoginInteractor(LoginInteractor):
    def execute(self, code: str):
        response = requests.get(
            url='https://graph.facebook.com/v6.0/oauth/access_token',
            params={
                "client_id": FaceBook.facebook_api_id,
                "redirect_uri": FaceBook.facebook_api_redirect_uri,
                "client_secret": FaceBook.facebook_api_secret,
                "code": code,
            },
        ).json()

        error = response.get("error", None)

        if error:
            raise InvalidCodeException

        access_token = response.get('access_token')

        response = requests.get(
            url='https://graph.facebook.com/me',
            params={
                "access_token": access_token,
                "fields": "email,name"
            },
        ).json()

        user = self.repository.get_user(id=response.get('id'), social='facebook')

        if user:
            self.repository.update_user_token(
                access_token=access_token,
                id=response.get('id'),
                email=response.get('email'),
                social='facebook',
                username=response.get('name')
            )
        else:
            self.repository.create_user(
                access_token=access_token,
                id=response.get('id'),
                email=response.get('email'),
                social='facebook',
                username=response.get('name')
            )


        token = JsonToken().encode(
            payload={"id": response['id']}
        )

        return token


class KakaoLoginInteractor(LoginInteractor):
    def execute(self, code: str):
        response = requests.post(
            url="https://kauth.kakao.com/oauth/token",
            data={
                "grant_type": "authorization_code",
                "client_id": Kakao.kakao_api_id,
                "redirect_uri": Kakao.kakao_api_redirect_uri,
                "code": code
            }
        ).json()

        error = response.get("error", None)

        if error:
            raise InvalidCodeException

        access_token = response.get('access_token')

        header = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(
            url="https://kapi.kakao.com/v2/user/me",
            headers=header
        ).json()

        user = self.repository.get_user(id=response.get('id'), social='kakao')

        if user:
            self.repository.update_user_token(
                access_token=access_token,
                id=response.get('id'),
                email=response.get('kakao_account').get('email'),
                social='kakao',
                username=response.get('properties').get('nickname')
            )
        else:
            self.repository.create_user(
                access_token=access_token,
                id=response.get('id'),
                email=response.get('kakao_account').get('email'),
                social='kakao',
                username=response.get('properties').get('nickname')
            )

        token = JsonToken().encode(
            payload={"id": response.get('id')}
        )

        return token

