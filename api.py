import requests
import json
from settings import VALID_EMAIL
from settings import VALID_PASSWORD
from requests_toolbelt.multipart.encoder import MultipartEncoder


class Pets:
    """ API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {
            "password": VALID_PASSWORD,
            "email": VALID_EMAIL
        }
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        my_email = res.json()['email']
        my_status = res.status_code
        return my_token, my_id, my_email, my_status

    def get_list_users(self) -> json:
        '''Запрос к Swagger сайта для получения списка юзеров. По факту приходит наш id'''
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        my_status = res.status_code
        my_id = res.text
        return my_status, my_id

    def create_pet(self) -> json:
        '''Запрос к Swagger сайта для добавления нового питомца'''
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "name": "My new pet",
            "type": "cat",
            "age": 5,
            "gender": "Male",
            "owner_id": my_id,
        }
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return status, pet_id

    def get_pet_id(self) -> json:
        '''Запрос к Swagger сайта на получение информации по id питомца'''
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        id_pet = res.json()['pet']['id']
        name_pet = res.json()['pet']['name']
        type_pet = res.json()['pet']['type']
        owner_id = res.json()['pet']['owner_id']
        owner_name = res.json()['pet']['owner_name']
        return status, id_pet, name_pet, type_pet, owner_id, owner_name

    def get_pet_by_user_id(self) -> json:
        '''Запрос к Swagger сайта на получение  всех питомцев юзера'''
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[1]
        pet_id = Pets().create_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "skip": 0,
            "num": 3,
            "type": "cat",
            "user_id": my_id
        }
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        list_pets = res.json()
        return status, list_pets

    def add_comment(self) -> json:
        '''Запрос к Swagger сайта на добавление комментария питомцу'''
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "pet_id": pet_id,
            "date": "2022-12-04T08:48:12.745Z",
            "message": "new comment",
            "user_id": 192,
            "user_name": "alena@mail.ru"
        }
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        id_comment = res.json()['id']
        return status, id_comment

    def add_like(self) -> json:
        '''Запрос к Swagger сайта на добавление лайка питомцу'''
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": Pets().create_pet()[1]}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def delete_pet(self) -> json:
        '''Запрос к Swagger сайта на удаления питомца'''
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status


Pets().get_token()
Pets().get_list_users()
Pets().create_pet()
Pets().get_pet_id()
Pets().get_pet_by_user_id()
Pets().add_comment()
Pets().add_like()
Pets().delete_pet()
