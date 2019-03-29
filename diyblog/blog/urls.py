from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),

    path('blogs/', views.BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<int:pk>/comment', views.add_comment, name='blog-comment'),
    path('blog/<int:pk>/comment/<int:comment_pk>/reply/', views.reply_comment, name='reply-comment'),
    path('blog/create', views.BlogCreateView.as_view(), name='blog-create'),
    path('blog/blog/<int:pk>', views.like, name='like'),
   # path('blog/<int:pk>/update/')

    path("bloggers/", views.BloggerListView.as_view(), name='blogger-list'),
    path("blogger/<int:pk>", views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('blogger/create', views.BloggerCreateView.as_view(), name='blogger-create'),



]