from . import views
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.mentor, name='mentor'),
                  path('mentor_chatrooms/<str:myEmail>/<str:user_id>/', views.mentor_chatrooms,
                       name='mentor_chatrooms'),
                  path('mentor_new_message/', views.mentor_new_message, name='mentor_new_message'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
