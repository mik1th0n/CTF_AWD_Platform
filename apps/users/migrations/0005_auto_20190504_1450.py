# Generated by Django 2.1.7 on 2019-05-04 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_userprofile_user_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_log',
            name='login_time',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=20),
        ),
        migrations.AddField(
            model_name='user_log',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
