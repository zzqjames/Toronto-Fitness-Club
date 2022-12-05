# Generated by Django 4.1.3 on 2022-12-05 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('coach', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=200)),
                ('capacity', models.PositiveIntegerField()),
                ('start_time', models.DateTimeField(help_text='This is the start time of the first instance of this class.')),
                ('duration', models.DurationField()),
                ('end_time', models.DateTimeField(help_text='Every instance of this class ends before end time.')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studios.studio')),
            ],
        ),
        migrations.CreateModel(
            name='ClassInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('coach', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
                ('space_availability', models.PositiveIntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('is_cancelled', models.BooleanField(default=False)),
                ('the_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class')),
            ],
        ),
        migrations.CreateModel(
            name='UserEnrolledClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('class_instance_name', models.CharField(max_length=200)),
                ('class_instance_start_time', models.DateTimeField()),
                ('class_instance_end_time', models.DateTimeField()),
                ('class_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classinstance')),
            ],
        ),
    ]