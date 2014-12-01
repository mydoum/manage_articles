from django.shortcuts import render
from models import Article

# Create your views here.
def home(request):
    objects = Article.objects.all()
    if request.method == 'GET':
        if 'category' in request.GET:
            if request.GET['category'] == 'AR':
                objects = objects.filter(category='AR')
            elif request.GET['category'] == 'IN':
                objects = objects.filter(category='IN')
            elif request.GET['category'] == 'RE':
                objects = objects.filter(category='RE')
            elif request.GET['category'] == 'DI':
                objects = objects.filter(category='DI')
            else:
                objects = Article.objects.all()
    return render(request, 'index.html', {'objects': objects})

def profile(request):
    return render(request, 'registration/profile.html', {})
