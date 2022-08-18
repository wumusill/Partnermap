from django.urls import path
from intro import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('humanity/', views.humanity, name='humanity'),
    path('society/', views.society, name='society'),
    path('science/', views.science, name='science'),
    path('business/', views.business, name='business'),
    path('engine/', views.engine, name='engine'),
    path('elec/', views.elec, name='elec'),
    path('farm/', views.farm, name='farm'),
    path('teacher/', views.teacher, name='teacher'),
    path('life/', views.life, name='life'),
    path('vet/', views.vet, name='vet'),
    path('medicine/', views.medicine, name='medicine'),
    path('doctor/', views.doctor, name='doctor'),
    path('mixed/', views.mixed, name='mixed'),
]