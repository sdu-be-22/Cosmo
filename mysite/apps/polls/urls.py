from django.urls import path

from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, LikeView, AddCommentView, UserSearch, AddLike, send_message


urlpatterns = [
    path('send/', send_message),
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('search/', UserSearch.as_view(), name='profile-search'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
]
