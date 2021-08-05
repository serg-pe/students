# Generated by Django 3.2.6 on 2021-08-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentgroup',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='groups',
        ),
        migrations.AddField(
            model_name='teacher',
            name='groups',
            field=models.ManyToManyField(to='main.StudentGroup', verbose_name='Группы'),
        ),
    ]