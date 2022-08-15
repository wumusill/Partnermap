from django.contrib import admin
from django.urls import path
from partnerapp import views
from accounts import views as accounts_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    
    path('humanity/', views.humanity, name='humanity'),
    path('business/', views.business, name='business'),
    
    path('login/', accounts_views.login, name="login"),
    path('logout/', accounts_views.logout, name="logout"),
    path('join/', accounts_views.join, name="join"),
    
    path('board/', views.board, name="board"),
    path('intro/', views.intro, name="intro"),
    path('write/', views.write, name="write"),
    
]
