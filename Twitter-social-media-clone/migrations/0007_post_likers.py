# Generated by Django 3.2.2 on 2021-07-08 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
    ]