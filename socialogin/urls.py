from django.urls import path
from socialogin.views import FacebookLoginView


urlpatterns = [
    path('fb_login', FacebookLoginView.as_view()),
]