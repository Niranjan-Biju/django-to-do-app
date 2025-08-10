# Register your models here.
from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)  # show only own tasks

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user  # assign user on creation
        super().save_model(request, obj, form, change)

admin.site.register(Task, TaskAdmin)
