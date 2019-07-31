from django.shortcuts import render
from blog.models import Story
from django.contrib.auth.models import User

def singularity(request):
    return render(request, 'singularity.html')

def fluff(request):
    if request.user.is_authenticated:
        stories = Story.objects.all()
        return render(request, 'fluff.html', {'stories': stories})
    else:
        return render(request, '404.html')

def story(request, id):
    if request.method == 'POST' and request.POST:
        edited_story = request.POST['content']
        print(request.user.username)
        if request.user.is_authenticated:
            requested_story = Story.objects.get(pk=id)
            requested_story.story = edited_story
            requested_story.save()
            story = Story.objects.get(pk=id)
            return render(request, 'story.html', {'story': story})
    else:
        if request.user.is_authenticated:
            story = Story.objects.get(pk=id)
            return render(request, 'story.html', {'story': story})
        else:
            return render(request, '404.html')
    
