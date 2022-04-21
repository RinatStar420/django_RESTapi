from django.db import models

# Create your models here.
# Создание модели  которая будет  хранится в БД

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    # флаг выполнена тодошка или нет
    done = models.BooleanField(default=False)

    # строковое представление по названию
    def __str__(self):
        return self.title