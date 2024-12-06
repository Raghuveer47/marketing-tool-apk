from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_poster, name='create_poster'),  # Root URL for creating posters
    path('<int:pk>/', views.poster_detail, name='poster_detail'),  # Detail view
    path('list/', views.poster_list, name='poster_list'),  # List of posters
      path('delete/<int:pk>/', views.delete_poster, name='delete_poster'),
]
