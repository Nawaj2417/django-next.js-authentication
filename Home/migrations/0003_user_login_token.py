# Generated by Django 4.2.5 on 2023-09-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_user_is_authorized'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_token',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
