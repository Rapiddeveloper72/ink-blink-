# Generated by Django 4.2.1 on 2023-05-19 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogs',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]
