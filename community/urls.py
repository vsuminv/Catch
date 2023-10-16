from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', views.list, name='list'),
    path('new_writing/<int:communityid>', views.new_writing, name='new_writing'),
    path('community_post/<int:communityid>/<int:board_id>', views.community_post, name='community_post'),
    path('community_delete/<int:communityid>/<int:board_id>', views.community_delete, name='community_delete'),
    path('new_comment/<int:communityid>/<int:board_id>', views.new_comment, name='new_comment'),
    path('community_update/<int:communityid>/<int:board_id>', views.community_update, name='community_update'),
    path('comment_update/<int:communityid>/<int:board_id>/<int:reply_id>', views.comment_update, name='comment_update'),
    path('comment_delete/<str:communityid>/<int:board_id>/<int:reply_id>', views.comment_delete, name='comment_delete'),
    path('my_post',views.mypost, name='mypost'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)