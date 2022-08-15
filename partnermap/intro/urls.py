from django.urls import path
from intro import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('humanity/', views.humanity, name='humanity'),
    path('business/', views.business, name='business'),
]