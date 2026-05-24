from django.urls import path
from .views import HomeView, HomeRecommandView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('recommand/', HomeRecommandView.as_view(), name='home_recommand'),

]
