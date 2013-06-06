from django.contrib import admin 
from models import *


class StudentsAdmin(admin.ModelAdmin):
	
	list_display = ('fio', 'birthday', 'student_card', 'group',)

admin.site.register(Students, StudentsAdmin)


class StudentsInline(admin.TabularInline):
	model = Students
	extra = 1


class GroupAdmin(admin.ModelAdmin):
	
	list_display = ('name',)
	inlines = [StudentsInline,]

admin.site.register(Group, GroupAdmin)