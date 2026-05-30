from django.views import View
from django.shortcuts import render
from home.models import TagTitels
from contents.models import VideoContent

class HomeView(View):
    def get(self, request):
        thumnails = ['Recent Videos', 'Playlist', 'Subcription']
        categories = TagTitels.objects.all()
        videos = VideoContent.objects.all().order_by('-created_at')

        return render(request, 'home/home.html', {
            'thumnails': thumnails,
            'categories': categories,
            'videos': videos
        })


class HomeRecommandView(View):
    def get(self, request):
        return render(request,'home/recommand.html')