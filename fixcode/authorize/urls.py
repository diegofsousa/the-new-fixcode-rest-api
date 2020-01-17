from django.conf.urls import url

from django.urls import path, include

from .views import FirstAccessView, SecondAccessView

app_name = 'authorize'

urlpatterns = [
    path('first-access/', FirstAccessView.as_view(), name='first_access'),
    path('second-access/', SecondAccessView.as_view(), name='second_access'),
]