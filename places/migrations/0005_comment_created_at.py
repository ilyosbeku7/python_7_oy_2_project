# Generated by Django 5.0.3 on 2024-03-30 09:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_comment_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
