# Generated by Django 3.0.7 on 2020-07-10 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20200709_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_hit',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
