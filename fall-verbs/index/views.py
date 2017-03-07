from django.shortcuts import render




def index(request):
    """Представление для главной страницы"""
    return render(request, 'index/index.html', {})