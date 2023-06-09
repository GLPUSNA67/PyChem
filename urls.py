from django.urls import path
from . import views

app_name = 'chemistryapp'
urlpatterns = [
    path('landingpage/', views.landingpage, name='landingpage'),
    path('uielements/', views.uielements, name='uielements'),
    path('lpchart/', views.lpchart, name='lpchart'),
    path('lptabpanel/', views.lptabpanel, name='lptabpanel'),
    path('lptable/', views.lptable, name='lptable'),
    path('lpform/', views.lpform, name='lpform'),
    path('lpempty/', views.lpempty, name='lpempty'),
]
