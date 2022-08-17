from django.contrib import admin
from django.urls import path, include
from partnerapp import views
from accounts import views as accounts_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    
    path('login/', accounts_views.login, name="login"),
    path('logout/', accounts_views.logout, name="logout"),
    path('join/', accounts_views.join, name="join"),
    
    path('board/', views.board, name="board"),
    path('detail/<int:post_id>', views.detail, name="detail"),

    path('intro/', include('intro.urls')),

    path('postcreate/', views.postcreate, name="postcreate"),
    path('new_comment/<int:post_id>', views.new_comment, name="new_comment"),

    path('preference/', views.preference, name="preference"),
    path('like/<int:partner_id>/', views.likes, name="likes"),
]
