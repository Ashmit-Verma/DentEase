from . import views
from django.urls import path,include

urlpatterns = [
    path('login/',views.Login,name='login')
]