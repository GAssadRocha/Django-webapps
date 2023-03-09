# Generated by Django 4.1 on 2023-03-09 03:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Owe_app', '0003_alter_transaction_payee_user_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='value',
            field=models.DecimalField(decimal_places=2, default=django.utils.timezone.now, max_digits=8),
            preserve_default=False,
        ),
    ]
