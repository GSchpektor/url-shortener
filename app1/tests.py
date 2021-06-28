from django.conf import settings
from django.http import HttpResponseRedirect
import requests
import json

settings.configure()


def test_redirect():
    post_url = "http://localhost:8000/create"
    headers = {"Content-Type": "application/json"}
    data = {'url': "https://ravkavonline.co.il"}
    response = requests.post(post_url, data=json.dumps(data), headers=headers)
    response = json.loads(response.content)
    short_url = response['short_url']
    print(short_url)
    return HttpResponseRedirect(short_url)


def test_fake_short_url():
    post_url = "http://localhost:8000/create"
    headers = {"Content-Type": "application/json"}
    data = {'url': "https://ravkavonline.co.il"}
    response = requests.post(post_url, data=json.dumps(data), headers=headers)
    response = json.loads(response.content)
    short_url = response['short_url'] + 'abcd'
    print(short_url)
    return HttpResponseRedirect(short_url)

