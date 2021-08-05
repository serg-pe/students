from django.shortcuts import render
from django.contrib import admin

from .models import Student, StudentGroup, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    change_list_template = 'main/admin/admin_students_list.html'
    list_filter = ('groups__number', 'name')

    list_display = ('avatar', 'surname', 'name', 'patronymic')


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('number',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic')
