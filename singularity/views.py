from django.shortcuts import render
from blog.models import Story

def singularity(request):
    return render(request, 'singularity.html')

def fluff(request):
    stories = Story.objects.all()
    if request.user.is_authenticated:
        return render(request, 'fluff.html', {'stories': stories})

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
        story = Story.objects.get(pk=id)
        return render(request, 'story.html', {'story': story})
    
