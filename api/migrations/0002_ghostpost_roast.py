# Generated by Django 3.0.8 on 2020-07-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghostpost',
            name='roast',
            field=models.BooleanField(default=True),
        ),
    ]