# Generated by Django 4.1.2 on 2022-11-17 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_card_pmt_option_remove_payment_payer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='holder',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Card holder'),
        ),
    ]