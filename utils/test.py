import asyncio
import json
import time
from concurrent.futures import ThreadPoolExecutor

import aiohttp
import requests

start_time = time.time()
#
# headers = {
#     'Cookie': 'csrftoken=cbvkkl8cPM1I17BlHmPol6voRq9fg7kYt228Q7JECvlhD173gHrfRmUevsxn8ihy'
# }
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         for index in range(100, 1000):
#             payload = {
#                 'image_to_predict':
#                     open(
#                         f'/Users/ymolodtsov/Documents/Development/personal/huskies/media/images/german_shepherd/german_shepherd-{index}.jpeg',
#                         'rb'
#                     )
#             }
#             url = "https://models.yev-bots.com/breeds-prediction/predict/"
#             async with session.post(url, headers=headers, data=payload) as resp:
#                 response = await resp.json()
#                 with open('results_without_celery_4_workers.json', 'a') as f:
#                     f.write(f'{index} ---------------------------------------------------\n')
#                     f.write(json.dumps(response))
#                     f.write('\n\n')
#
#
# asyncio.run(main())
# print("--- %s seconds ---" % (time.time() - start_time))

url = "https://models.yev-bots.com/breeds-prediction/predict/"

payload = {}
headers = {
    'Cookie': 'csrftoken=cbvkkl8cPM1I17BlHmPol6voRq9fg7kYt228Q7JECvlhD173gHrfRmUevsxn8ihy'
}


def send_response(index):
    files = [
        ('image_to_predict', ('german_shepherd-98.jpeg', open(
            f'/Users/ymolodtsov/Documents/Development/personal/huskies/media/images/german_shepherd/german_shepherd-{index}.jpeg', 'rb'),
                              'image/jpeg'))
    ]
    response = requests.request("POST", url, headers=headers, data=payload, files=files).json()
    with open('threaded_test_min.json', 'a') as f:
        f.write(f'{index} ---------------------------------------------------\n')
        f.write(json.dumps(response))
        f.write('\n\n')


with ThreadPoolExecutor(max_workers=8) as exe:
    for i in range(100, 300):
        print(i)
        exe.submit(send_response, i)
