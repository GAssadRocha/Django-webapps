# Generated by Django 4.1 on 2023-03-09 04:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Owe_app', '0005_remove_transaction_time_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]