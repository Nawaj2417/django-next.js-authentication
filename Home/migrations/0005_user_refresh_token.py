# Generated by Django 4.2.5 on 2023-10-27 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_user_username_reset_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
