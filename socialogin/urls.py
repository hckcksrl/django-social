from django.urls import path
from socialogin.views import FacebookLoginView, KakaoLoginView


urlpatterns = [
    path('fb_login', FacebookLoginView.as_view()),
    path('kakao_login', KakaoLoginView.as_view())
]