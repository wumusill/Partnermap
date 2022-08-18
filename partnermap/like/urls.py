from django.contrib import admin
from django.urls import path, include
from like import views
from accounts import views as accounts_views

urlpatterns = [
    path('likes_humanity/<int:partner_id>/', views.likes_humanity, name="likes_humanity"),
    path('likes_society/<int:partner_id>/', views.likes_society, name="likes_society"),
    path('likes_science/<int:partner_id>/', views.likes_science, name="likes_science"),
    path('likes_business/<int:partner_id>/', views.likes_business, name="likes_business"),
    path('likes_engine/<int:partner_id>/', views.likes_engine, name="likes_engine"),
    path('likes_elec/<int:partner_id>/', views.likes_elec, name="likes_elec"),
    path('likes_farm/<int:partner_id>/', views.likes_farm, name="likes_farm"),
    path('likes_teacheer/<int:partner_id>/', views.likes_teacher, name="likes_teacher"),
    path('likes_life/<int:partner_id>/', views.likes_life, name="likes_life"),
    path('likes_vet/<int:partner_id>/', views.likes_vet, name="likes_vet"),
    path('likes_medicine/<int:partner_id>/', views.likes_medicine, name="likes_medicine"),
    path('likes_doctor/<int:partner_id>/', views.likes_doctor, name="likes_doctor"),
    path('likes_mixed/<int:partner_id>/', views.likes_mixed, name="likes_mixed"),
]
