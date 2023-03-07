from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='USER_ID')
    name = models.CharField(max_length=256, db_column='NAME')
    created_time = models.DateTimeField(auto_now_add=True, db_column='CREA_DT')
    updated_time = models.DateTimeField(auto_now=True, db_column='UPDT_DT')

    class Meta:
        db_table = 'profile'


class Place(models.Model):
    BAD_SCORE = 1
    GOOD_SCORE = 5
    SCORE_CHOICE = (
        (BAD_SCORE, 'bad'),
        (GOOD_SCORE, 'good')
    )

    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='places', null=True,
                                db_column='PROFILE_ID')
    name = models.CharField(max_length=256, db_column='NAME')
    kakao_place = models.ForeignKey('KakaoPlace', on_delete=models.SET_NULL, null=True, db_column='KAKAO_ADDR_ID')
    contents = models.TextField(db_column='CONT', null=True, blank=True)
    latitude = models.FloatField(db_column='LAT', null=True)
    longitude = models.FloatField(db_column='LNG', null=True)
    score = models.IntegerField(choices=SCORE_CHOICE, default=GOOD_SCORE, db_column='SCORE')
    created_time = models.DateTimeField(auto_now_add=True, db_column='CREA_DT')
    updated_time = models.DateTimeField(auto_now=True, db_column='UPDT_DT')

    class Meta:
        db_table = 'place'


class KakaoPlace(models.Model):
    id = models.CharField(max_length=256, db_column='ADDR_ID', primary_key=True)
    address_name = models.TextField(db_column='ADDR_NAME')
    road_address_name = models.TextField(db_column='ROAD_ADDR_NAME')
    category_group_code = models.CharField(max_length=50, db_column='CTGR_GRP_CODE')
    category_group_name = models.CharField(max_length=50, db_column='CTGR_GRP_NAME')
    category_name = models.CharField(max_length=256, db_column='CTGR_NAME')
    place_name = models.CharField(max_length=256, db_column='NAME')
    place_url = models.TextField(db_column='URL')
    phone = models.CharField(max_length=50, db_column='PHONE')
    x = models.FloatField(db_column='X')
    y = models.FloatField(db_column='Y')

    class Meta:
        db_table = 'kakao_place'
