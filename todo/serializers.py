# Сериалайзер - чтобы сериализоать наши модели в json предсталение

from rest_framework import serializers
from .models import Todo

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        # говорю что модель это мой Тодо
        model = Todo
        # указыаю что надо сериализовать всё
        fields = '__all__'