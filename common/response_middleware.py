import asyncio
import traceback
import sys
from django.utils.decorators import sync_and_async_middleware
from django.utils.deprecation import MiddlewareMixin
from rest_framework.renderers import JSONRenderer

from common.utils import FoodMapResponse
from rest_framework.response import Response

@sync_and_async_middleware
def simple_middleware(get_response):
    # One-time configuration and initialization goes here.
    if asyncio.iscoroutinefunction(get_response):
        async def middleware(request):
            # Do something here!
            response = await get_response(request)
            return response

    else:
        def middleware(request):
            # Do something here!
            response = get_response(request)
            _, _, stacktrace = sys.exc_info()
            if response.status_code >= 400:
                response = FoodMapResponse(status_code=response.status_code, data={}, message=response.reason_phrase)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
            return response

    return middleware
