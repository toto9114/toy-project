from rest_framework import serializers
from api.models import Place, KakaoPlace


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class KakaoPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KakaoPlace
        fields = '__all__'
