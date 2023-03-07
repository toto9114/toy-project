# Generated by Django 4.1.7 on 2023-02-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_place_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='score',
            field=models.IntegerField(choices=[(1, 'BAD'), (5, 'GOOD')], db_column='SCORE', default=5),
        ),
    ]