from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register),
    path('token/', views.token),
    path('token/refresh/', views.refresh_token),
    path('token/revoke/', views.revoke_token),
    path('all/', views.ListUsers.as_view(), name=None),
    path('create/', views.CreateUser.as_view(), name=None),
]