from django.urls import path

from .views import Login

from . import views

app_name = 'account'
urlpatterns = [
    path("login/", Login.as_view()),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]