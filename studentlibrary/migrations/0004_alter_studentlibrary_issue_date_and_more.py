# Generated by Django 4.2.4 on 2023-08-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentlibrary', '0003_alter_studentlibrary_penalty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlibrary',
            name='issue_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='studentlibrary',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentlibrary',
            name='time_period',
            field=models.DateTimeField(),
        ),
    ]
