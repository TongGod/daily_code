# Generated by Django 3.1.3 on 2021-05-03 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_loginstatemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginmodel',
            name='img_head',
            field=models.CharField(default='static/images/default.jpg', max_length=200),
        ),
    ]
