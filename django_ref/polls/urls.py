from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<str:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<str:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<str:question_id>/vote/', views.vote, name='vote')
]