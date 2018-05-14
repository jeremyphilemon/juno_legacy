from django.shortcuts import render


def singularity(request):
    return render(request, 'singularity.html')
