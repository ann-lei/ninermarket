from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def explorePage(request):
    return HttpResponse('Explore Page')

def communityPage(request):
    return HttpResponse('Community Page')

