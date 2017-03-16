import random

from django.db import models
from prefs.models import Pref
from classes.models import Class



class Word(models.Model):
    """Модель описывающая слово"""
    word = models.CharField(max_length=64)
    pref = models.ForeignKey(Pref, on_delete=models.CASCADE, blank=True, null=True)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.word



class Sense(models.Model):
    """Значение слова, для одного слова может быть много значений"""
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    sense = models.TextField()

    def __str__(self):
        return self.sense

    def get_all_examples(self):
        """Метод возвращает все примеры для данного значения слова"""
        return Example.objects.filter(sense=self)



class Example(models.Model):
    """Пример значения слова, для одного значения может быть много примеров"""
    sense = models.ForeignKey(Sense, on_delete=models.CASCADE)
    example = models.TextField()

    def __str__(self):
        return self.example



class Task(models.Model):
    """Задания к словам, для одного задания может быть много заданий"""
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    task = models.TextField()

    def __str__(self):
        return self.task


    def get_random_answers(self, count=3):
        random_words = [word.word for word in Word.objects.all().order_by('?')[:count]]
        random_words.remove(self.word.word)
        random_answers = random_words + [self.word.word]
        random.shuffle(random_answers)
        
        return random_answers