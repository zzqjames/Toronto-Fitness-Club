# Generated by Django 4.1.2 on 2022-11-19 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_membershipplan_customuser_sub_edate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payer',
            field=models.CharField(max_length=255, null=True, verbose_name="payer's username"),
        ),
    ]