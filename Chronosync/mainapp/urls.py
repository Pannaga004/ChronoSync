from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('discover/', views.discover, name='discover'),
    path('crs_ai/', views.crs_ai, name='crs_ai'),
    path('crs_raw/', views.crs_raw, name='crs_raw'),
    path('features/', views.features, name='features'), 
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('chronopoints/', views.chronopoints_view, name='chronopoints'),  
    path('dashboard/', views.dashboard_view, name='dashboard'),
]