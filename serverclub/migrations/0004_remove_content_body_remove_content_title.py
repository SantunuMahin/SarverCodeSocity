# Generated by Django 5.1.2 on 2024-10-14 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serverclub', '0003_content_alter_post_author_alter_post_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='body',
        ),
        migrations.RemoveField(
            model_name='content',
            name='title',
        ),
    ]
