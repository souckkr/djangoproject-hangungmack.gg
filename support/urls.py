from django.urls import path
from . import views
# Create your tests here.
app_name = 'support'

urlpatterns = [
    path('list', views.PostListView.as_view(), name='list'),
    path('<int:pk>/detail/', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.post_delete, name='delete'),
]