from django.contrib import admin

# Register your models here.

from .models import Grades, Student


class GradesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    list_filter = ['gname']
    search_fields = ['pk']
    list_per_page = 5

    fieldsets = [
        ('num', {'fields': ['ggirlnum', 'gboynum']}),
        ('base', {'fields':['gname','gdate','isDelete']})
    ]


admin.site.register(Grades, GradesAdmin)
admin.site.register(Student)
