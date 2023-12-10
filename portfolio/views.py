from django.shortcuts import render
from .models import Profile

# Create your views here.
def home(req):
	profile=Profile.objects.all()
	return render(req,'portfolio/home.html',{'profile':profile})