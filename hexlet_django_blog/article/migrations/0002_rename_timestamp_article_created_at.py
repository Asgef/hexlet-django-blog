# Generated by Django 5.0.4 on 2024-04-15 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='timestamp',
            new_name='created_at',
        ),
    ]
