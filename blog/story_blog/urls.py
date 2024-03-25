from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # path('', views.home, name='home_page'),
    path('', PostListView.as_view(), name='home_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about_page'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user_post'),
]
