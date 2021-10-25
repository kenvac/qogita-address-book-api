from django.urls import path, include
from djoser import views as djoser_views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('login', djoser_views.TokenCreateView.as_view(), name='login'),
    path('logout', djoser_views.TokenDestroyView.as_view(), name='logout'),
]
