from django.urls import path

from . import views

urlpatterns=[
path('', views.index),
path('questions/', views.questions),
path('questions/<slug:question_slug>',views.single_question)
]
