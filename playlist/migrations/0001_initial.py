# Generated by Django 2.0.5 on 2018-06-27 14:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=500)),
                ('art', models.CharField(max_length=500)),
                ('archived', models.NullBooleanField(default=False)),
            ],
        ),
    ]