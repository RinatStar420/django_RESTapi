from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    # Что хочу видеть в нашей модели
    # list_display - какие поля модели будут видны в списке
    list_display = ('id', 'title', 'description', 'date', 'done')
    list_display_links = ('id', 'title')
    # search_fields - по каким полям модели можно произодить поиск
    search_fields = ('id', 'title', 'description')
    # list_editable - озночает разрешение модификации в самом списке
    list_editable = ('done',)
    # параметры фильтра
    list_filter = ('done',)


admin.site.register(Todo, TodoAdmin)


