# Generated by Django 3.2 on 2021-05-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='message',
            field=models.TextField(),
        ),
    ]