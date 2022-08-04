from django.urls import path

from . import views

urlpatterns=[
path('', views.index),
path('questions/<question_subject>', views.questions, name='questions-list'),
#path('questions/<slug:question_slug>',views.single_question)
]
