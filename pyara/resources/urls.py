from django.urls import path

from . import views

urlpatterns=[
path('', views.index),
path('questions/<question_subject>', views.questions, name='questions-list'),
path('answer/<question_id>', views.answers, name='answers-list'),
#path('questions/<slug:question_slug>',views.single_question)
]
