from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path("",views.home,name="home"),
   path("contact/",views.contact,name="contact"),
    path('admin/', admin.site.urls),
     path('login/',views.dentistLogin,name='dentistLogin'),
    path('profile/',views.dentistProfile,name='dentistProfile'),
    path('register/',views.dentistRegister,name="dentistRegister"),
]