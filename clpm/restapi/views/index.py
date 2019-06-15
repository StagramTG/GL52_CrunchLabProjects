from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def login(request):
    context = {}
    return render(request, 'login.html', context)


def validatelogin(request):
    context = {}
    return render(request, 'index.html', context)


@ensure_csrf_cookie
def main(request):
    context = {}
    return render(request, 'index.html', context)