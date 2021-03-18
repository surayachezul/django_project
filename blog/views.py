from django.shortcuts import render

posts = [
    {
        'author' : 'Suraya',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'March 18, 2021'
    },
    {
        'author' : 'Ali',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'March 19, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})