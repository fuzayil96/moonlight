from django.shortcuts import render

from django.views.generic import ListView, TemplateView
from .models import Article
class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'index-test-added-1-page.html'