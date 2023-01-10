from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index-view'),
    path('questions/<question_subject>', views.questions, name='questions-list'),
    path('answer/<question_id>', views.answers, name='answers-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
