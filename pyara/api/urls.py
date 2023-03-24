from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('questions/',
         views.QuestionListView.as_view(),
         name='question_list'),

    path('questions/<pk>/',
         views.QuestionDetailView.as_view(),
         name='question_detail'),
]