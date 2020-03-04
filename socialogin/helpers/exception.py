from rest_framework.exceptions import APIException


class BaseAPIException(APIException):
    pass


class InvalidTokenException(BaseAPIException):
    status_code = 404
    default_code = 'invalid_token'
    default_detail = 'invalid_token'


class ValidationErrorException(BaseAPIException):
    status_code = 400
    default_code = 'bad request'
    default_detail = 'bad request params'


class InvalidCodeException(BaseAPIException):
    status_code = 404
    default_code = 'invalid_code'
    default_detail = 'invalid_code'