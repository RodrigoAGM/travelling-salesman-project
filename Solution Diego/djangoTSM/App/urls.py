from django.urls import path
from App.views import home, sol1, sol2, sol3, sol4, sol5, sol6

from . import views

urlpatterns = [
    path('', home, name='TSM-home'),
    path('sol1/', sol1, name='TSM-Sol1'),
    path('sol2/', sol2, name='TSM-Sol2'),
    path('sol3/', sol3, name='TSM-Sol3'),
    path('sol4/', sol4, name='TSM-Sol4'),   
    path('sol5/', sol5, name='TSM-Sol5'),   
    path('sol6/', sol6, name='TSM-Sol6'),   
]