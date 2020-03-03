import requests
import json
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from socialogin.interactors import FaceBook
from rest_framework import status
from socialogin.helpers import JsonToken


class FacebookLoginView(APIView):
    def get(self, request: Request):
        code = request.query_params.get('code')
        response = requests.get(
            url='https://graph.facebook.com/v6.0/oauth/access_token',
            params={
                "client_id": FaceBook.facebook_api_id,
                "redirect_uri": FaceBook.facebook_api_redirect_uri,
                "client_secret": FaceBook.facebook_api_secret,
                "code": code,
            },
        )



        response = requests.get(
            url='https://graph.facebook.com/me',
            params={
                "access_token": response.json()['access_token'],
                "fields": "email,name"
            },
        )

        payload = response.json()

        token = JsonToken().encode(
            payload={"id":payload['id']}
        )

        return Response(status=status.HTTP_200_OK, data={"token": token})
