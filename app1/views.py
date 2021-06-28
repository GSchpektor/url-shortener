from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
import secrets
import json
from django.views.decorators.csrf import csrf_exempt
from .models import ShortUrl


@csrf_exempt
def make_short_url(request):
    response = request.body
    # converting from bytes to dict
    url = json.loads(response)
    print(url['url'])
    # create short url
    code = secrets.token_urlsafe(8)
    # checking if the code exists
    while ShortUrl.objects.filter(short_url=code).exists():
        code = secrets.token_urlsafe(8)
    ShortUrl.objects.create(url=url['url'], short_url=code)
    return JsonResponse({'status': 200, 'short_url': f'http://127.0.0.1:8000/s/{code}'})


def redirect_to_url(request, short_url):
    # retrieve the object
    obj = get_object_or_404(ShortUrl, short_url=short_url)
    # increase the counter
    obj.counter += 1
    obj.save()
    return HttpResponseRedirect(obj.url)
