# Generated by Django 3.1.1 on 2020-09-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='lat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='lng',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
