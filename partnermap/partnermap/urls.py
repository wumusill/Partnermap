from django.contrib import admin
from django.urls import path, include
from partnerapp import views
from intro import views as intro_views
from accounts import views as accounts_views

urlpatterns = [
    path("rndlghdtla", admin.site.urls),
    path('', views.home , name='home'),
    
    path('login/', accounts_views.login, name="login"),
    path('logout/', accounts_views.logout, name="logout"),
    path('join/', accounts_views.join, name="join"),
    
    path('board/', views.board, name="board"),
    path('detail/<int:post_id>', views.detail, name="detail"),
    path('detail/<int:post_id>/delete/', views.detail_delete, name="detail_delete"),

    path('intro/', include('intro.urls')),
    path('like/', include('like.urls')),

    path('postcreate/', views.postcreate, name="postcreate"),
    path('new_comment/<int:post_id>', views.new_comment, name="new_comment"),
]
