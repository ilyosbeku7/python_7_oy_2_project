# Generated by Django 5.0.3 on 2024-03-29 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='izohlar', to='places.place'),
        ),
    ]
