from django.shortcuts import render
# from django.http import HttpResponse

# Fake Posts

posts = [
	{
		'author': 'auth1',
		'title': 'Blog Post 1',
		'content': 'First post conent',
		'date_posted': 'February 7, 2024'
	},
	{
		'author': 'auth2',
		'title': 'Blog Post 2',
		'content': 'Second post conent',
		'date_posted': 'February 8, 2024'
	},
]



# Create your views here.
def home(request):
	context = { 
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})