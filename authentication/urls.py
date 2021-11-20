from django.urls import path
from .views import LoginHomeView, RegisterView, StageOneView, StageTwoView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', LoginHomeView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('<slug:slug>/1/', StageOneView.as_view(), name="stage_one"),
    path('<slug:slug>/2/', StageTwoView.as_view(), name="stage_two"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
