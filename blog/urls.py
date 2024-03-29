from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('events/', views.PostList.as_view(), name='post_list'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('category/<str:cats>/', views.CategoryView, name='category_view'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('edit/<slug:slug>/', views.UpdatePost.as_view(), name='update_post'),
    path(
        'delete/<slug:slug>/', views.DeletePost.as_view(), name='delete_post'),
]
