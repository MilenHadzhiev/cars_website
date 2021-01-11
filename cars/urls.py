from django.urls import path

from cars.views import homepage

urlpatterns = [
    path('', homepage, name='homepage')
]