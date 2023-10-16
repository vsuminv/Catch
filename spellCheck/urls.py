from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('spellCheck/', views.spellCheck, name='spellCheck'),
    path('textSave/', views.textSave, name='textSave'),
    path('saveSpellCheckResult/', views.saveSpellCheckResult, name='saveSpellCheckResult')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)