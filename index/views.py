from django.shortcuts import render
from django.http import HttpResponse
from models import Articles

# Create your views here.
def index(request):
    objects = Articles.objects.all()
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
                objects = Articles.objects.all()
    return render(request, 'index.html', {'objects': objects})
