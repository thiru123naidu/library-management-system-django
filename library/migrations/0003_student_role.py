# Generated by Django 4.2.4 on 2023-08-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_name_student_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='role',
            field=models.CharField(default='student', max_length=10),
        ),
    ]