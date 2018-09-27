from django.urls import path
from App.views import home, sol1, sol2, sol3, sol4

from . import views

urlpatterns = [
    path('', home, name='TSM-home'),
    path('sol1/', sol1, name='TSM-Sol1'),
    path('sol2/', sol2, name='TSM-Sol2'),
    path('sol3/', sol3, name='TSM-Sol3'),
    path('sol4/', sol4, name='TSM-Sol4'),   

]