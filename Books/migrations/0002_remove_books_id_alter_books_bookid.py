# Generated by Django 4.2.4 on 2023-08-13 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='id',
        ),
        migrations.AlterField(
            model_name='books',
            name='bookid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
