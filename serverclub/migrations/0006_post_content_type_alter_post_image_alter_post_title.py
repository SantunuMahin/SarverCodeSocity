# Generated by Django 5.1.2 on 2024-10-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverclub', '0005_delete_content_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_type',
            field=models.CharField(choices=[('BL', 'Blog'), ('NW', 'News'), ('RV', 'Review')], default='BL', max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
