import os.path
import pytest
from api import Pets

pt = Pets()


def test_get_token():
    status = pt.get_token()[3]
    token = pt.get_token()[0]
    assert status == 200
    assert token


def test_get_list_users():
    status = pt.get_list_users()[0]
    my_id = pt.get_list_users()[1]
    assert status == 200
    assert my_id


def test_create_pet():
    status = pt.create_pet()[0]
    pet_id = pt.create_pet()[1]
    assert status == 200
    assert pet_id


def test_get_pet_photo(pet_photo='tests\\photo\\pet.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status = pt.get_pet_photo()[0]
    link = pt.get_pet_photo()[1]
    assert status == 200
    assert link


@pytest.mark.xfail
def test_pet_id():
    status = pt.get_pet_id()[0]
    id_pet = pt.get_pet_id()[1]
    name_pet = pt.get_pet_id()[2]
    type_pet = pt.get_pet_id()[3]
    owner_id = pt.get_pet_id()[4]
    owner_name = pt.get_pet_id()[5]
    assert status == 200
    assert id_pet == pt.create_pet()[1]
    assert name_pet
    assert type_pet == 'cat'
    assert owner_id == pt.get_token()[1]
    assert owner_name == "alena@mail.ru"


def test_get_pet_by_usr_id():
    status = pt.get_pet_by_user_id()[0]
    list_pets = pt.get_pet_by_user_id()[1]
    assert status == 200
    assert list_pets


def test_add_comment():
    status = pt.add_comment()[0]
    id_comment = pt.add_comment()[1]
    assert status == 200
    assert id_comment


def test_add_like():
    status = pt.add_like()
    assert status == 200


def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200
