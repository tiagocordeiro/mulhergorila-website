from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


def quem_somos(request):
    return render(request, 'quem-somos.html')
