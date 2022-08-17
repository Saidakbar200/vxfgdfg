from django.contrib import admin
from myfiles.models import Student,Fan
# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','ism','fam','fan','yosh','sana']

admin.site.register(Student,AdminStudent)

class AdminFan(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Fan,AdminFan)