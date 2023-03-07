from rest_framework.response import Response


class FoodMapResponse(Response):
    def __init__(self, status_code, data, message='ok', code=None):
        if not code:
            code = '%s%s' % (str(status_code), '0000')
        response = {
            'code': str(code),
            'message': message,
            'payload': data
        }
        super().__init__(status=status_code, data=response)
