from django.shortcuts import render
from django.views import View
# Create your views here.
from home.models import TagTitels



class HomeView(View):
    def get(self, request):
        thumnails = ['Recent Videos', 'Playlist', 'Subcription']
        categories = TagTitels.objects.all() 
        return render(request, 'home/home.html', {'thumnails': thumnails, 'categories': categories})

class HomeRecommandView(View):
    def get(self, request):
        return render(request,'home/recommand.html')