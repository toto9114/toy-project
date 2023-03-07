from typing import List
from api.models import KakaoPlace
import config
import ujson as json
import requests

headers = {"Authorization": f'KakaoAK {config.KAKAO_REST_API_KEY}'}


def search_places(query: str) -> List[KakaoPlace]:
    if not query:
        return []

    request_url = f'https://dapi.kakao.com/v2/local/search/keyword.json'
    query_params = {'query': query}
    response = requests.get(headers=headers, url=request_url, params=query_params)

    result = []
    if 200 <= response.status_code < 300:
        _result = json.loads(response.text)
        doc = _result['documents']
        if doc:
            result = []
            for data in doc:
                data.pop('distance')
                result.append(KakaoPlace(**data))

    return result
