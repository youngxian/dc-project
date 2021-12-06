from django.urls import path
from .views import HomeView, WorkExprienceView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('work/exprience', WorkExprienceView.as_view(), name='work_exprience')
]
