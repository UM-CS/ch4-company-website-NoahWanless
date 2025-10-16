from django.urls import path

from .views import home_page_view, AboutPageView, ProductsPageView, MessagesPageView,post_list,posts
from .views import post_detail
from .views import BlogDetailView,BlogCreateView,BlogUpdateView, BlogDeleteView

urlpatterns = [
	path("", home_page_view,name="home"),
    path("about/",AboutPageView.as_view(),name="about"), #makes the class a view
    path("products/",ProductsPageView.as_view(),name="products"),
    path("messages/",MessagesPageView.as_view(),name="messages"),
    path("posts/",post_list.as_view(),name="post_list"),
    path("post_board/",posts.as_view(),name="posts"),
    path("post/new/",BlogCreateView.as_view(),name="post_new"), 
    path("post/<int:pk>/",BlogDetailView.as_view(),name="post_detail"),
    path("post/<int:pk>/edit/",BlogUpdateView.as_view(),name="post_edit"),
    path("post/<int:pk>/delete/",BlogDeleteView.as_view(),name="post_delete")
    #the <int:pk> tells it that when using post_detail to get the view, 
    #pass in pk as the var pk

]
