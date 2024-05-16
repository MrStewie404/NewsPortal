from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, SearchList, PostCreate, page

urlpatterns = [
   path('news/', PostsList.as_view()),
   path('page/', page),
   path('news/search/', SearchList.as_view()),
   path('news/search/<int:pk>', PostDetail.as_view()),
   path('news/<int:pk>', PostDetail.as_view()),


   path('news/create/', PostCreate.as_view()),

   # path('/news/<int:pk>/edit/', PostDetail.as_view()),
   # path('/news/<int:pk>/delete/', PostDetail.as_view()),
   # path('/articles/create/', PostDetail.as_view()),
   # path('/articles/<int:pk>/edit/', PostDetail.as_view()),
   # path('/articles/<int:pk>/delete/', PostDetail.as_view()),

   



]