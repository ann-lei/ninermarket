from django.urls import path
from . import views

urlpatterns = [
    path('', views.explorePage, name='explore-page'),
    path('community/', views.communityPage, name='community-page'),
]