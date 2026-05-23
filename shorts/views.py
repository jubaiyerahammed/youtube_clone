from django.shortcuts import render
from django.views import View
# Create your views here.

class ShortsView(View):
    def get(self, request):
        return render(request,'shorts/shorts.html')
class ShortsWatchView(View):
    def get(self, request):
        return render(request,'shorts/watch.html')