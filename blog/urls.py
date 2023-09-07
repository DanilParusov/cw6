from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [

    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('view/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='blog_view', ),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update', ),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete', ),

]