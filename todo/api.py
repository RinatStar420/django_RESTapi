from .models import Todo
from rest_framework import  viewsets, permissions
from .serializers import TodoSerializers

class TodoViewSet(viewsets.ModelViewSet):
    # мои объекты тодо в БД
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializers