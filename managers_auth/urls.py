from django.urls import path
from django.http import HttpResponse
from .views import ManagerLogin


def my_view(request):
    return HttpResponse('Success')


urlpatterns = [
    path('test/', my_view),
    path('login', ManagerLogin.as_view(), name='manager_login')
]
