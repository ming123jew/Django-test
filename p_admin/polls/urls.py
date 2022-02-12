from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # # ex: /polls/
    # path('', views.index, name='index'),
    # path('index2', views.index2, name='index2'),
    # # ex: /polls/5/
    # path('<int:question_id>.html', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results.html', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('vote/<int:question_id>', views.vote, name='vote'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]