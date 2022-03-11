from django.urls import path
from .views import BlogPostView, BlogDetailView  # new
urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),  # new
    path('', BlogPostView.as_view(), name='home'),
]
