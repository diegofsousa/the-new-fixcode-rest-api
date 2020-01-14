from django.conf.urls import url

from django.urls import path, include

from .views import FirstAccessView

app_name = 'authorize'

urlpatterns = [
    path('first-access/', FirstAccessView.as_view(), name='single_user_profile'),
]