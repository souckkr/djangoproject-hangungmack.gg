from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('list/', views.PostListView.as_view(), name="list"),
    path("<int:pk>/detail/", views.PostDetailView.as_view(), name="detail"),
    path("create/", views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.post_delete, name='delete'),
    path('search/',views.SearchPost.as_view(), name ='search'),
    path('<int:pk>/comment/write/', views.comment_write, name="comment_write"),
    path('<int:pk>/comment_delete/', views.comment_delete, name="comment_delete"),
    path('<int:pk>/like/', views.like, name='like'), 
    ]
