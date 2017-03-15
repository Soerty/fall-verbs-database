from django.db import models

class Pref(models.Model):
    """Модель описывающая приставку"""
    pref = models.CharField(max_length=10)

    def __str__(self):
        return self.pref