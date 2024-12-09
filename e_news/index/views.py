from django.shortcuts import render
from .models import NewsCategory, News
# Create your views here.
def home_page(request):
    categories = NewsCategory.objects.all()
    news = News.objects.all()

    context = {'categories': categories, 'news': news}

    return render(request, 'home.html', context)
