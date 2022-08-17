from django.contrib import admin
from django.urls import path, include
from like import views
from accounts import views as accounts_views

urlpatterns = [
    path('likes_humanity/<int:partner_id>/', views.likes_humanity, name="likes_humanity"),
    path('likes_business/<int:partner_id>/', views.likes_business, name="likes_business"),
]
