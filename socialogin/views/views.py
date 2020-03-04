from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from socialogin.helpers import ValidationErrorException
from socialogin.interactors import FaceBookLoginInteractor, KakaoLoginInteractor
from socialogin.serializers import CodeSerializer


class FacebookLoginView(APIView):
    def get(self, request: Request):
        serializer = CodeSerializer(data=request.query_params)
        if not serializer.is_valid():
            raise ValidationErrorException

        token = FaceBookLoginInteractor().execute(**serializer.data)

        return Response(status=status.HTTP_200_OK, data={"token": token})


class KakaoLoginView(APIView):
    def get(self, request:Request):
        serializer = CodeSerializer(data=request.query_params)
        if not serializer.is_valid():
            raise ValidationErrorException

        token = KakaoLoginInteractor().execute(**serializer.data)

        return Response(status=status.HTTP_200_OK, data={"token": token})
