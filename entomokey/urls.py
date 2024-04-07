from django.urls import path
from . import views

app_name = 'entomokey'

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search")
]
urlpatterns += [
    path('login/', views.entomokey_login, name="user_login"),
    path('register/', views.entomokey_register, name="user_register"),
    path('logout/', views.entomokey_logout, name="user_logout"),
]