# Generated by Django 3.0.5 on 2020-05-01 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testM', '0012_auto_20200501_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='puntuacion_mchatrf',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='testM.Resultado'),
        ),
    ]