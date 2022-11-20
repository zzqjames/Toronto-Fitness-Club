# Generated by Django 4.1.3 on 2022-11-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='address',
            field=models.TextField(help_text='Please seperate street name, city, and province by comma.And no space after comma', max_length=500, verbose_name='Studio Address'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='amenitiesquantity',
            field=models.TextField(help_text="Please correspond to each amenity's type. Seperate each integer by comma and no space after comma", max_length=500, verbose_name='Amenities Quantity'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='amenitiestype',
            field=models.TextField(help_text="Please enter amenity's type.Seperate each integer by comma and no space after comma", max_length=500, verbose_name='Amenities Type'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='geolocation',
            field=models.TextField(help_text='Please seperate longitude and latitude by comma and no space after comma. Eg. 121.1111,90.28', max_length=500, verbose_name='longitude, latitude'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='imagelist',
            field=models.TextField(blank=True, help_text='Please seperate each image by comma and no space after comma', null=True, verbose_name='Link of Images'),
        ),
    ]