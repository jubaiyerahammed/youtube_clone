from django.views import View
from django.shortcuts import render

from home.models import TagTitels
from contents.models import VideoContent, News
from shorts.models import Short


class HomeView(View):

    def get(self, request):
        categories = TagTitels.objects.all()
        recent_videos = (
            VideoContent.objects
            .select_related('channel')
            .order_by('-created_at')[:12]
        )

        trending_videos = (
            VideoContent.objects
            .select_related('channel')
            .order_by('-views', '-created_at')[:12]
        )

        popular_videos = (
            VideoContent.objects
            .select_related('channel')
            .order_by('-views')[:12]
        )

        shorts = (
            Short.objects
            .order_by('-created_at')[:12]
        )

        news = (
            News.objects
            .order_by('-created_at')[:12]
        )

        premium_videos = (
            VideoContent.objects
            .select_related('channel')
            .filter(is_premium=True)
            .order_by('-created_at')[:12]
        )

        free_videos = (
            VideoContent.objects
            .select_related('channel')
            .filter(is_premium=False)
            .order_by('-created_at')[:12]
        )


        # ==========================================
        # 9. SUBSCRIPTION VIDEOS
        # ==========================================
        #
        # এখনো User -> Channel subscription
        # relationship তৈরি হয়নি।
        #
        # তাই আপাতত recent videos ব্যবহার করছি।
        #
        # Login + Subscription system তৈরি হলে
        # এই QuerySet পরিবর্তন হবে।
        #

        subscription_videos = (
            VideoContent.objects
            .select_related('channel')
            .order_by('-created_at')[:12]
        )


        # ==========================================
        # 10. SEND DATA TO TEMPLATE
        # ==========================================

        return render(
            request,
            'home/home.html',
            {
                'categories': categories,

                'recent_videos': recent_videos,

                'trending_videos': trending_videos,

                'popular_videos': popular_videos,

                'shorts': shorts,

                'news': news,

                'premium_videos': premium_videos,

                'free_videos': free_videos,

                'subscription_videos': subscription_videos,
            }
        )
    


class HomeRecommandView(View):
    def get(self, request):
        return render(request,'home/recommand.html')