from django.shortcuts import render

from .models import Word
from .models import Task
from .models import Sense
from .models import Example




def index(request):
    """Представление отображающее список всех слов"""
    context = {}
    context['words'] = Word.objects.all()

    return render(request, 'words/index.html', context)



def senses(request, word_id='1'):
    """Представление для отображения всех значений слова"""
    context = {}
    
    word = Word.objects.get(id=word_id)
    context['word'] = word
    context['senses'] = Sense.objects.filter(word=word.id)

    return render(request, 'words/sense.html', context)



def tasks(request, word_id='1'):
    """Представления отображающее задания для слова"""
    context = {}

    word = Word.objects.get(id=word_id)
    tasks = Task.objects.filter(word=word.id)
    random_answers = [task.get_random_answers() for task in tasks]

    all_tasks = []
    for task, answers in zip(tasks, random_answers):
        left_part, right_part = task.task.replace('\r\n', '</br>').split('...')
        all_tasks.append([left_part, answers, right_part])

    context['word'] = word
    context['tasks'] = all_tasks

    return render(request, 'words/task.html', context)