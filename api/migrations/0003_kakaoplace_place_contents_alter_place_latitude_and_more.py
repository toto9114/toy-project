# Generated by Django 4.1.7 on 2023-02-23 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_place_table_alter_profile_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='KakaoPlace',
            fields=[
                ('address_id', models.CharField(db_column='ADDR_ID', max_length=256, primary_key=True, serialize=False)),
                ('address_name', models.TextField(db_column='ADDR_NAME')),
                ('road_address_name', models.TextField(db_column='ROAD_ADDR_NAME')),
                ('category_group_code', models.CharField(db_column='CTGR_GRP_CODE', max_length=50)),
                ('category_group_name', models.CharField(db_column='CTGR_GRP_NAME', max_length=50)),
                ('category_name', models.CharField(db_column='CTGR_NAME', max_length=256)),
                ('place_name', models.CharField(db_column='NAME', max_length=256)),
                ('place_url', models.TextField(db_column='URL')),
                ('phone', models.CharField(db_column='PHONE', max_length=50)),
                ('x', models.FloatField(db_column='X')),
                ('y', models.FloatField(db_column='Y')),
            ],
            options={
                'db_table': 'kakao_place',
            },
        ),
        migrations.AddField(
            model_name='place',
            name='contents',
            field=models.TextField(blank=True, db_column='CONT', null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(db_column='LAT', null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(db_column='LNG', null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='profile',
            field=models.ForeignKey(db_column='PROFILE_ID', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='places', to='api.profile'),
        ),
        migrations.AddField(
            model_name='place',
            name='kakao_address',
            field=models.ForeignKey(db_column='KAKAO_ADDR_ID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.kakaoplace'),
        ),
    ]
