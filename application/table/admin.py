from django.contrib import admin

from .models import Field, Path


class FieldAdmin(admin.ModelAdmin):
    pass


class PathAdmin(admin.ModelAdmin):
    pass


admin.site.register(Field, FieldAdmin)
admin.site.register(Path, PathAdmin)