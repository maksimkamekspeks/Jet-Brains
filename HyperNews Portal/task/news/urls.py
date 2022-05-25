from django.urls import path, re_path
from .views import MainPageView, ArticlePageView, CreateArticle, redirect_m

urlpatterns = [
    path('news/', MainPageView.as_view()),
    path('', redirect_m),
    re_path('news/create/', CreateArticle.as_view()),
    re_path('news/(?P<number_of_link>[^/]*)/?', ArticlePageView.as_view()),
]
# (?P<candy_name>[^/]*)/?
# <int:number_of_article>
