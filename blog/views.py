from django.shortcuts import render


def fluff(request):
    return render(request, 'home.html')
