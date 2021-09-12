# Generated by Django 3.2 on 2021-08-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('question_text', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('language', models.CharField(max_length=200)),
                ('stars', models.IntegerField()),
            ],
        ),
    ]
