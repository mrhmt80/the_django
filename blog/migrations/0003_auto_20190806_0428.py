# Generated by Django 2.2.3 on 2019-08-06 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='static/img/blog'),
        ),
    ]
