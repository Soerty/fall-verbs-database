from django.db import models

class Class(models.Model):
    """Модель описывающая приставку"""
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name
