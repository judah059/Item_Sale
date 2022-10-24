import datetime


def get_datetime(request):
    return {'datetime': datetime.datetime.now()}
