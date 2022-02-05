import requests


class DogBreedPredictionAPI:
    def __init__(self):
        self.host = 'https://www.models.yev-bots.com/'

    def predict_breed_transfer(self, img_path=None, image=None, top=2):
        url = self.host + 'breeds-prediction/predict/'
        payload = {}
        files = [
            ('image_to_predict', ('image_to_predict.jpeg', image, 'image/jpeg'))
        ]
        try:
            response = requests.request("POST", url, data=payload, files=files)
            breed = response.json()['breed']
            print(f'got predicted breed: {breed}')
            return breed
        except Exception as ex:
            print('ex: ', ex)
