from django.shortcuts import render
from models import CreateArticle
from django.http import HttpResponse
from index.models import Article

# Create your views here.
def create(request):
    form = CreateArticle()
    if request.method == "POST":
        form = CreateArticle(request.POST)
        if form.is_valid():
            Article(CreateArticle.name, CreateArticle.description, 'AR')
            return HttpResponse('/OK/')
    return render(request, 'creation/article.html', {'form': form})