from django.shortcuts import render

from .models import Word




def index(request):
    """Представление отображающее список всех слов"""
    context = {}
    context['words'] = Word.objects.all()

    return render(request, 'words/index.html', context)



def sense(request, word_id='1'):
    """Представление для отображения всех значений слова"""
    context = {}
    
    word = Word.objects.get(id=word_id)
    if word:
        context['word'] = word

    return render(request, 'words/sense.html', context)