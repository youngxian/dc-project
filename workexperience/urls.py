from django.urls import path
from .views import WorkExperienceFormView

urlpatterns = [
    path('personal', WorkExperienceFormView.as_view(), name='onboading')
]
