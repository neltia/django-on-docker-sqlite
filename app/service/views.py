from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def menu1(request):
    return render(request, "service/menu1.html")
