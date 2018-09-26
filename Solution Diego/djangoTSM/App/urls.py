from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='TSM-home'),
    path('sol1/', views.sol1, name='TSM-Sol1'),
    path('sol2/', views.sol2, name='TSM-Sol2'),
    path('sol3/', views.sol3, name='TSM-Sol3'),

]