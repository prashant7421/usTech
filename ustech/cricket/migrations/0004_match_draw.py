# Generated by Django 3.0.5 on 2020-05-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0003_match_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='draw',
            field=models.BooleanField(default=False),
        ),
    ]
