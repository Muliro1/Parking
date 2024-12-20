from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home_view, name="home"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    path('home/', views.home_view, name='home'),
    path('reserve_parking/', views.reserve_parking, name='reserve_parking'),
]