# Generated by Django 3.0.5 on 2020-04-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testM', '0010_auto_20200424_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='question_id',
            field=models.IntegerField(default=0),
        ),
    ]