import os

from django import forms
from django.conf import settings


class AdminBulkStudentsForm(forms.Form):
    students_csv = forms.FileField(required=True, label='CSV файл')
    students_avatars = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Загрузить фото')
