from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User

import config
from api.kakao_rest_api import search_places
from api.models import Place, KakaoPlace
from api.serializers import PlaceSerializer, KakaoPlaceSerializer
from common.utils import FoodMapResponse
import logging

logger = logging.getLogger(__name__)


# Create your views here.

def health(request):
    return HttpResponse("Healthy")


DEFAULT_LAT, DEFAULT_LNG = 37.50059916708842, 127.03215610525639


def marker_list(request):
    places = Place.objects.filter(profile=1)

    center_lat = DEFAULT_LAT
    center_lng = DEFAULT_LNG
    if places:
        cnt = 0
        total_lat = 0
        total_lng = 0
        for place in places:
            cnt += 1
            total_lat += place.latitude
            total_lng += place.longitude
        center_lat = total_lat / cnt
        center_lng = total_lng / cnt

    return render(request, 'api/index.html', {
        'center_lat': center_lat,
        'center_lng': center_lng,
        'places': places,
        'kakao_api_key': config.KAKAO_WEB_API_KEY
    })


def search_place(request, score: str):
    score_dict = {s: score for score, s in Place.SCORE_CHOICE}
    score_num = score_dict[score]
    print(score_num)
    return render(request, 'api/search.html', {
        "profile_id": 1,
        "score": score_num
    })


def update_place_contents(request, place_id: int):
    return render(request, 'api/place_detail.html', {"place_id": place_id})


class UserAPIView(APIView):
    def post(self, request):
        username = ''
        try:
            last_user_id = User.objects.latest('id')
            username = f'user_{last_user_id}'
        except User.DoesNotExist:
            username = 'user_1'
        finally:
            User.objects.create_user(username=username)

        return FoodMapResponse(status_code=status.HTTP_201_CREATED, data={})


class UserPlaceView(ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        param = self.request.query_params
        profile_id = param.get('profile_id')
        score = param.get('score')

        queryset = Place.objects.filter(profile_id=profile_id, score=score)
        return queryset

    def list(self, request, *args, **kwargs):
        response = PlaceSerializer(self.get_queryset(), many=True)
        return FoodMapResponse(status_code=status.HTTP_200_OK, data=response.data)


class SearchPlaceView(APIView):
    def get(self, request):
        query = request.query_params.get('query')
        places = search_places(query)
        serializer = KakaoPlaceSerializer(places, many=True)
        return FoodMapResponse(status_code=status.HTTP_200_OK, data=serializer.data)


class SavePlaceView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        profile_id = data.pop('profile_id')
        score = data.pop('score')

        place = {
            'profile': profile_id,
            'score': score,
            'longitude': data.get('x'),
            'latitude': data.get('y'),
            'name': data.get('place_name')
        }
        with transaction.atomic():
            kakao_place, created = KakaoPlace.objects.get_or_create(**data)

            place['kakao_place'] = kakao_place.id
            place_serializer = PlaceSerializer(data=place)
            if place_serializer.is_valid(raise_exception=True):
                place_serializer.save()

            return FoodMapResponse(status_code=status.HTTP_201_CREATED, data=place_serializer.data)


class PlaceDescriptionView(APIView):
    def put(self, request, place_id: int):
        print(request)
        data = request.data
        print(data)
        contents = data.get('contents')
        Place.objects.filter(id=place_id).update(contents=contents)

        return FoodMapResponse(status_code=status.HTTP_200_OK, data={})