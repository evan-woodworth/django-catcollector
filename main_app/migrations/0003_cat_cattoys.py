# Generated by Django 3.2.4 on 2021-06-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210624_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='cattoys',
            field=models.ManyToManyField(to='main_app.CatToy'),
        ),
    ]
