from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('list/', views.game_list, name='list'),
    path('<int:pk>/detail/', views.GameDetailView.as_view(), name='detail'),
    path('create/', views.GameCreateView.as_view(), name='create'),
    path('<int:pk>/update/',views.GameUpdateView.as_view(), name = 'update'),
    path('<int:pk>/create/', views.game_delete, name='delete'),
    path('search/',views.game_search, name = 'search'),
    path('<int:pk>/comment/write/', views.comment_write, name="comment_write"),
    path('<int:pk>/comment_delete/', views.comment_delete, name="comment_delete"),
    path('<int:pk>/like/', views.like, name='like'),
]
