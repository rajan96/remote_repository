# Generated by Django 2.1.2 on 2019-12-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0004_coursesdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesdata',
            name='start_date',
            field=models.DateField(max_length=100),
        ),
    ]
