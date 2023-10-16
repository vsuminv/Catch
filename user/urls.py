#user/urls.py
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login'),
    path('join_mentee/', views.join_mentee, name='join_mentee'),
    path('join_mentor/', views.join_mentor, name='join_mentor'),
    path('join_select/', views.join_select, name='join_select'),
    path('logout/', views.logout, name='logout'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage/certify', views.certify, name='certify'),
    path('find_id/', views.find_id, name='find_id'),
    path('IdCheck/', views.IdCheck, name='IdCheck'),
    path('withdrawal/', views.withdrawal, name='withdrawal')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)