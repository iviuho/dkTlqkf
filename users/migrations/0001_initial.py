# Generated by Django 5.0 on 2024-01-04 14:34

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('login_id', models.CharField(max_length=30, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
