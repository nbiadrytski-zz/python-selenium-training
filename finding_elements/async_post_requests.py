import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests
import random
import string

'''Make POST request in multi threads.
Number of requests made = range value in make_requests func'''

base_url = "http://seamless-media-dev.mtvnservices.com/api/submit"
headers = {'Content-Type': 'application/json', 'Accept': 'application/seamless.app.resource-1.2+json'}
ad_url = "https://s3.amazonaws.com/mtvnet-seamless/qa-artifacts/seamless_docs/seamless_media_sources/patch_ad_uat2.xml"


def generate_id():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    return x


def generate_payload():
    payload = '{"id":2134,"topAdId":"2134","creativeId":"2134",\
    "uuid":' + generate_id() + ',"url":"' + ad_url + '","bitrate":748,"width":1280,"height":720}'
    return payload


def make_post_request():
    r = requests.post(base_url, data=generate_payload(), headers=headers)
    print(r.status_code)


executor = ThreadPoolExecutor(max_workers=5)  # number of threads
loop = asyncio.get_event_loop()


async def make_requests():
    futures = [loop.run_in_executor(executor, make_post_request) for _ in range(16)]  # url will be called 16 times
    await asyncio.wait(futures)


loop.run_until_complete(make_requests())
