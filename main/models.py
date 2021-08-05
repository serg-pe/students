from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class StudentGroup(models.Model):
    number = models.CharField(max_length=5, blank=False, verbose_name='Номер группы')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        return self.number


class Student(models.Model):
    avatar = models.ImageField(blank=True, verbose_name='Фото')
    surname = models.CharField(max_length=50,  blank=False, verbose_name='Фамилия')
    name = models.CharField(max_length=40,  blank=False, verbose_name='Имя')
    patronymic = models.CharField(max_length=40,  blank=True, verbose_name='Отчество')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    groups = models.ManyToManyField(StudentGroup, verbose_name='Группы', related_name='students')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Сутденты'

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.patronymic}'


class Teacher(models.Model):
    surname = models.CharField(max_length=50,  blank=False, verbose_name='Фамилия')
    name = models.CharField(max_length=40,  blank=False, verbose_name='Имя')
    patronymic = models.CharField(max_length=40,  blank=True, verbose_name='Отчество')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    groups = models.ManyToManyField(StudentGroup, verbose_name='Группы', related_name='teachers')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
