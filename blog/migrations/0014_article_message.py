# Generated by Django 3.2 on 2021-05-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_article_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='message',
            field=models.TextField(default=None),
        ),
    ]
