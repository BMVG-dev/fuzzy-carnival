from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('<int:question_id>/', views.detail_page, name='detail_page'),
    path('<int:question_id>/results_page', views.results_page, name='results_page'),
    path('<int:question_id>/vote_page', views.vote_page, name='vote_page'),

]
