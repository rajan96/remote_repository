# Generated by Django 2.1.2 on 2019-12-12 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(max_length=50)),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
    ]
