# Generated by Django 4.2.4 on 2023-08-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentlibrary', '0006_alter_studentlibrary_issue_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlibrary',
            name='issue_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='studentlibrary',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentlibrary',
            name='time_period',
            field=models.DateField(),
        ),
    ]
