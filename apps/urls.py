from django.urls import path
from .views import ArticleListView, AboutPageView

urlpatterns = [
    path('', ArticleListView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name = 'about'),
]