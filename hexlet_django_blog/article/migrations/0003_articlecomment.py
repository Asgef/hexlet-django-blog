# Generated by Django 5.0.4 on 2024-04-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_rename_timestamp_article_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, verbose_name='content')),
            ],
        ),
    ]
