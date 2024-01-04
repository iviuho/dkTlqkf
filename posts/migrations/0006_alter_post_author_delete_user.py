# Generated by Django 5.0 on 2024-01-04 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_user_password'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.user'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
