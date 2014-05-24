from django.shortcuts import render_to_response
from blog import models


def index(request):
    return render_to_response('blog/index.html', {
        'posts': models.Post.objects.all()
    })