from django.views import View
from django.shortcuts import render
from home.models import TagTitels
from contents.models import VideoContent
from shorts.models import Short

class HomeView(View):
    def get(self, request):
        thumnails = ['Recent Videos', 'Playlist', 'Subcription']
        categories = TagTitels.objects.all()
        videos = VideoContent.objects.all().order_by('-created_at')
        shorts = Short.objects.all()


        return render(request, 'home/home.html', {
            'thumnails': thumnails,
            'categories': categories,
            'videos': videos,
            'shorts':shorts
        })
    


class HomeRecommandView(View):
    def get(self, request):
        return render(request,'home/recommand.html')