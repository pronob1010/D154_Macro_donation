# Generated by Django 3.2.5 on 2021-07-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='about',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
