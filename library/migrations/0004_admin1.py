# Generated by Django 4.2.4 on 2023-08-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_student_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin1',
            fields=[
                ('rollnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]