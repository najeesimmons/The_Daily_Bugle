from unicodedata import name
from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('freaks/', views.FreakList.as_view(), name = "freak_list"),
    path('freaks/new/',views.FreakCreate.as_view(), name="freak_create"),
    path('freaks/<int:pk>/', views.FreakDetail.as_view(), name="freak_detail"),
    path('freaks/<int:pk>/update', views.FreakUpdate.as_view(), name="freak_update"),
    path('freaks/<int:pk>/delete', views.FreakDelete.as_view(), name="freak_delete"),
]