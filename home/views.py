from django.views import View
from django.shortcuts import render

from home.models import TagTitels
from contents.models import VideoContent, News
from shorts.models import Short


class HomeView(View):

    def get(self, request):

        # ==========================================
        # 1. CATEGORY
        # ==========================================

        categories = TagTitels.objects.all()


        # ==========================================
        # 2. RECENT VIDEOS
        # নতুন ভিডিও আগে
        # ==========================================

        recent_videos = (
            VideoContent.objects
            .select_related('channel')
            .order_by('-created_at')[:12]
        )


        # ==========================================
        # 3. TRENDING VIDEOS
        # বেশি views + নতুন ভিডিও
        # ==========================================

        trending_videos = (
            VideoContent.objects
            .select_related('channel')
            .order_by('-views', '-created_at')[:12]
        )


        # ==========================================
        # 4. POPULAR VIDEOS
        # শুধুমাত্র views অনুযায়ী
        # ==========================================

        popular_videos = (
            VideoContent.objects
            .select_related('channel')
            .order_by('-views')[:12]
        )


        # ==========================================
        # 5. SHORTS
        # নতুন Shorts আগে
        # ==========================================

        shorts = (
            Short.objects
            .order_by('-created_at')[:12]
        )


        # ==========================================
        # 6. TOP NEWS
        # নতুন News আগে
        # ==========================================

        news = (
            News.objects
            .order_by('-created_at')[:12]
        )


        # ==========================================
        # 7. PREMIUM VIDEOS
        # ==========================================

        premium_videos = (
            VideoContent.objects
            .select_related('channel')
            .filter(is_premium=True)
            .order_by('-created_at')[:12]
        )


        # ==========================================
        # 8. FREE VIDEOS
        # ==========================================

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