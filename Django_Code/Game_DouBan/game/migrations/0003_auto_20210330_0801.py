# Generated by Django 3.1.3 on 2021-03-30 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20210329_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameinfo',
            name='n_ratings',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='platforms',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='rating',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
