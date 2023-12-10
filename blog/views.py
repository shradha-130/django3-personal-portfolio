from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(req):
	# blog=Blog.objects.order_by('date')[:5]// ordered by desc and last 5 records
	blog=Blog.objects.all()
	return render(req,'blog/all_blogs.html',{'blog':blog})

def blog_detail(req,blog_id):
	blog=get_object_or_404(Blog,pk=blog_id)
	return render(req,'blog/blog_detail.html',{'blog':blog})
 