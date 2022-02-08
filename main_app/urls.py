from unicodedata import name
from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('freaks/', views.FreakList.as_view(), name = "freak_list"),
    path('freaks/new/',views.FreakCreate.as_view(), name="freak_create"),
    path('freak/<int:pk>/', views.FreakDetail.as_view, name="freak_detail")
]