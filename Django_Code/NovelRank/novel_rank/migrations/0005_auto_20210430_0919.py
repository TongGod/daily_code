# Generated by Django 3.1.3 on 2021-04-30 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novel_rank', '0004_chuangshimodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chuangshimodel',
            old_name='click',
            new_name='collection',
        ),
    ]
