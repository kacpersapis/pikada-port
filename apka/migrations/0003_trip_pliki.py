# Generated by Django 3.1 on 2020-08-17 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apka', '0002_auto_20200816_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='pliki',
            field=models.FileField(blank=True, null=True, upload_to='pliki'),
        ),
    ]
