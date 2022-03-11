from django.urls import path
from .views import BlogPostView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView  # new
urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),  # new
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),  # new
    path('post/<int:pk>/delete', BlogDeleteView.as_view(),
         name='post_delete'),  # new
    path('', BlogPostView.as_view(), name='home'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
]
