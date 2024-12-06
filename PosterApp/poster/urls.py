from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_poster, name='create_poster'),
    path('<int:pk>/', views.poster_detail, name='poster_detail'),  # Detail view
    path('list/', views.poster_list, name='poster_list'),

]
