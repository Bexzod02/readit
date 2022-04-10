from django.shortcuts import render, get_object_or_404
from .models import Tag, Article, Category, Comment


def home_view(request):
    articles = Article.objects.order_by('-id')[:10]

    context = {'object_list': articles}
    return render(request, 'articles/index.html', context)


def article_list_view(request):
    articles = Article.objects.order_by('-id')

    context = {'object_list': articles}

    return render(request, 'articles/articles.html', context)


def article_detail_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    last_2_articles = Article.objects.order_by('-id')[:2]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comments = Comment.objects.filter(article__slug=slug)
    context = {
        'object': article,
        'last_2_articles': last_2_articles,
        'categories': categories,
        'tags': tags,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
